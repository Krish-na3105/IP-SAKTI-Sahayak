from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from pathlib import Path
from datetime import date
import json, re, io

app = FastAPI(
    title="IP-SAKTI Sahayak API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

class Ingredient(BaseModel):
    name: str
    scientific_name: str = ""
    source: str = "Plant"
    source_location: str = "India"
    traditional_use: str = "Unknown"

class AssessmentIn(BaseModel):
    product_name: str
    description: str
    product_type: str = "Not Sure"
    ingredients: List[Ingredient] = []
    intended_use: str = "General wellness"
    claims: str = ""
    classical_formulation: str = "Unsure"
    developed_by_org: str = "Unsure"
    traditionally_known: str = "Unsure"
    biological_resource: str = "Unknown"
    commercial_use: str = "Unknown"
    ip_goals: List[str] = []

class ChatIn(BaseModel):
    question: str
    assessment: Optional[Dict[str, Any]] = None

def load_json(name):
    text = (DATA / name).read_text(encoding="utf-8")
    if name.endswith('.jsonc'):
        # Remove single line comments (//)
        text = re.sub(r'^\s*//.*$', '', text, flags=re.MULTILINE)
        # Remove block comments (/* */)
        text = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)
    return json.loads(text)

def classify(a: AssessmentIn):
    score = 70
    reasons=[]
    if a.product_type != "Not Sure":
        category=a.product_type
        confidence=82
    elif a.intended_use == "Therapeutic use":
        category="Likely Ayurvedic medicinal product pathway"
        confidence=72
        reasons.append("Therapeutic intent is a strong classification signal.")
    elif a.intended_use == "Cosmetic":
        category="Likely cosmetic pathway"
        confidence=78
    elif a.intended_use in ["Food/nutrition", "General wellness"]:
        category="Likely food/wellness pathway"
        confidence=70
    else:
        category="Additional information required"
        confidence=55
    reasons += [f"intended use: {a.intended_use}", f"formulation information: {a.classical_formulation}", "user-provided product and ingredient information"]
    if a.classical_formulation == "Yes": score -= 5
    if a.traditionally_known == "Yes": score -= 8
    if a.biological_resource == "Yes" and a.commercial_use == "Yes": score -= 6
    return {"category": category, "confidence": confidence, "reasons": reasons, "score": max(0,min(100,score))}

def assess(a: AssessmentIn):
    classification=classify(a)
    tk = "YELLOW" if a.classical_formulation == "Yes" or a.traditionally_known == "Yes" else ("YELLOW" if a.classical_formulation == "Unsure" or a.traditionally_known == "Unsure" else "GREEN")
    abs_flag = "YELLOW" if a.biological_resource == "Yes" and a.commercial_use == "Yes" and any(i.source_location == "India" for i in a.ingredients) else ("YELLOW" if a.biological_resource == "Unknown" or a.commercial_use == "Unknown" else "GREEN")
    prior = "YELLOW" if "Patent" in a.ip_goals else "GREY"
    trademark = "GREEN" if "Trademark" in a.ip_goals or a.product_name else "GREY"
    regulatory = 85 if a.product_type != "Not Sure" else 62
    ip = 75 if a.ip_goals else 55
    prior_score = 55 if prior == "YELLOW" else 75
    tk_score = 60 if tk == "YELLOW" else 82
    abs_score = 58 if abs_flag == "YELLOW" else 82
    tm_score = 90 if trademark == "GREEN" else 60
    overall=round((regulatory+ip+prior_score+tk_score+abs_score+tm_score)/6)
    roadmap=[]
    if a.product_type == "Not Sure": roadmap.append({"priority":"High","reason":"Classification needs additional product/regulatory information.","action":"Verify product classification"})
    if tk == "YELLOW": roadmap.append({"priority":"High","reason":"Traditional knowledge indicators need review.","action":"Review traditional-knowledge considerations"})
    if prior == "YELLOW": roadmap.append({"priority":"High","reason":"Patent protection was selected; prior-art review is needed.","action":"Conduct detailed prior-art search"})
    if abs_flag == "YELLOW": roadmap.append({"priority":"High","reason":"Indian biological resources and commercial use may warrant ABS review.","action":"Assess ABS requirements"})
    if trademark == "GREEN": roadmap.append({"priority":"Medium","reason":"A distinctive product/brand name may merit trademark review.","action":"Search trademark availability"})
    roadmap.append({"priority":"Medium","reason":"AI output is preliminary and should be verified where required.","action":"Consult a qualified IP/regulatory professional if required"})
    return {
        "classification": classification,
        "health_score":{"overall":overall,"breakdown":{"Regulatory Clarity":regulatory,"IP Readiness":ip,"Prior-Art Risk":prior_score,"Traditional Knowledge Risk":tk_score,"ABS Review":abs_score,"Trademark Opportunity":tm_score}},
        "flags":{"regulatory":"GREEN" if regulatory>=75 else "YELLOW","ip":"GREEN" if ip>=70 else "YELLOW","prior_art":prior,"traditional_knowledge":tk,"abs":abs_flag,"trademark":trademark},
        "top_issues":[x for x in ["Traditional knowledge review","ABS assessment","Prior-art search"] if ((x.startswith("Traditional") and tk=="YELLOW") or (x.startswith("ABS") and abs_flag=="YELLOW") or (x.startswith("Prior") and prior=="YELLOW"))][:3],
        "roadmap":roadmap,
        "disclaimer":"AI-assisted preliminary assessment. Not legal advice. Verify applicable requirements with the relevant authority or qualified professional before filing or commercializing."
    }

@app.get("/api/health")
def health(): return {"status":"ok","service":"IP-SAKTI Sahayak"}

@app.get("/api/demo-scenarios")
def scenarios(): return load_json("demo_scenarios.json")

@app.post("/api/assessment")
def create_assessment(a: AssessmentIn): return assess(a)

@app.get("/api/patents")
def patents(q: str = ""):
    rows=load_json("patents.json")
    terms=[x.lower() for x in re.findall(r"[a-zA-Z]+", q) if len(x)>2]
    for r in rows:
        hay=(r["title"]+" "+" ".join(r["ingredients"])+" "+r["purpose"]+" "+r["technical_features"]).lower()
        hits=sum(t in hay for t in terms)
        r["similarity"]=min(96,45+hits*13) if terms else 50
        r["why_matched"]="Matches one or more searched ingredients/concepts." if hits else "Included as a nearby synthetic demonstration record."
    return sorted(rows,key=lambda x:x["similarity"],reverse=True)

@app.get("/api/tk")
def tk(q: str = ""):
    rows=load_json("tk.jsonc"); terms=[x.lower() for x in re.findall(r"[a-zA-Z]+",q) if len(x)>2]
    for r in rows:
        hay=(r.get("case_id","")+" "+" ".join(r.get("ingredients",[]))+" "+r.get("traditional_use","")).lower(); hits=sum(t in hay for t in terms)
        r["confidence"]=min(95,50+hits*15) if terms else 50
    return sorted(rows,key=lambda x:x.get("confidence",0),reverse=True)

@app.get("/api/fees")
def fees(): return load_json("fees.json")

@app.post("/api/ask")
def ask(c: ChatIn):
    q=c.question.lower(); a=c.assessment or {}
    if "patent" in q:
        answer="Based on the information currently provided, patentability cannot be determined conclusively. Prior-art searching, novelty, inventive step and applicable exclusions need to be considered."
        why=["Traditional knowledge may be involved","Prior-art search is required","More technical information may be needed"]
    elif "abs" in q or "biodiversity" in q:
        answer="If the product uses Indian biological resources for commercial use, a further ABS assessment may be appropriate. This prototype is only a preliminary screen."
        why=["Indian biological-resource use was considered","Commercial use was considered","Traditional knowledge can affect the review"]
    elif "trademark" in q:
        answer="A distinctive brand identity may be relevant for trademark protection. Availability and class selection should be checked before filing."
        why=["Brand protection was considered","Trademark availability is not established by this prototype"]
    else:
        answer="I can help interpret the current assessment, but the answer should be grounded in retrieved evidence and structured rules. Try asking about patentability, traditional knowledge, ABS, classification, or trademark protection."
        why=[]
    return {"answer":answer,"why":why,"citations":[{"title":"IP-SAKTI V1 evidence layer","authority":"Prototype curated corpus","section":"Assessment context","last_verified":str(date.today()),"source_url":""}],"disclaimer":"AI-assisted informational guidance; not legal or regulatory advice."}

@app.get("/api/legal")
def legal(): return load_json("legal.json")

@app.post("/api/report")
def report(a: AssessmentIn):
    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet
    result=assess(a); buf=io.BytesIO(); doc=SimpleDocTemplate(buf,pagesize=A4,rightMargin=36,leftMargin=36,topMargin=36,bottomMargin=36); s=getSampleStyleSheet(); story=[Paragraph("IP-SAKTI Sahayak — Innovation Health Check",s['Title']),Paragraph(a.product_name,s['Heading2']),Paragraph(a.description,s['BodyText']),Spacer(1,12)]
    story += [Paragraph(f"Likely classification: {result['classification']['category']} ({result['classification']['confidence']}% confidence)",s['BodyText']),Paragraph(f"Overall readiness: {result['health_score']['overall']}/100",s['Heading2'])]
    data=[["Indicator","Score"]]+[[k,str(v)] for k,v in result['health_score']['breakdown'].items()]; t=Table(data); t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.5,colors.grey),('BACKGROUND',(0,0),(-1,0),colors.lightgrey)])); story += [Spacer(1,8),t,Spacer(1,12),Paragraph("Recommended next steps",s['Heading2'])]
    for x in result['roadmap']: story.append(Paragraph(f"• {x['priority']}: {x['action']} — {x['reason']}",s['BodyText']))
    story += [Spacer(1,12),Paragraph(result['disclaimer'],s['Italic'])]; doc.build(story); return {"filename":"ip-sakti-assessment.pdf","content":buf.getvalue().hex()}
