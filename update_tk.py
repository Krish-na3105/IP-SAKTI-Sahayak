import json

with open("backend/data/tk.json", "r", encoding="utf-8") as f:
    old_data = f.read()

# Create block comment for old data
old_commented = "/* \n--- OLD SYNTHETIC DATA (COMMENTED OUT DUE TO INCOMPATIBLE SCHEMA) ---\n" + old_data + "\n*/\n\n"

# New factual data from PDF 3
new_data = [
    {
        "case_id": "1734/DEL/2007",
        "jurisdiction": "India",
        "patent_application_no": "1734/DEL/2007",
        "system_of_medicine": "Ayurveda",
        "ingredients": ["Neem", "camphor"],
        "traditional_use": "Eczema/related conditions",
        "tkdl_reference_type": "Formulation documents",
        "examination_context": "Examiner raised novelty/inventive-step objections and Section 3(p).",
        "legal_issues": ["Section 3(p)", "Novelty", "Inventive step"],
        "outcome": "Application refused on 10 Mar 2014 after TKDL references and other documents.",
        "source_url": "https://www.tkdl.res.in/tkdl/langdefault/common/Examinarreport/reports/1734_DEL_2007.asp",
        "source_date": "2014-03-10",
        "verified_date": "2026-08-27",
        "authority_level": "official_public_TKDL_record"
    },
    {
        "case_id": "913/DEL/2006",
        "jurisdiction": "India",
        "patent_application_no": "913/DEL/2006",
        "system_of_medicine": "Ayurveda",
        "ingredients": ["Curcuma longa (turmeric)", "sandalwood"],
        "traditional_use": "Skin disorders/medical conditions",
        "tkdl_reference_type": "Prior art documents",
        "examination_context": "Examiner raised Section 3(p) and inventive-step objections based on TKDL prior art.",
        "legal_issues": ["Section 3(p)", "Inventive step"],
        "outcome": "Application abandoned.",
        "source_url": "https://www.tkdl.res.in/tkdl/LangFrench/common/Examinarreport/reports/913_DEL_2006.asp",
        "source_date": "Unknown",
        "verified_date": "2026-08-27",
        "authority_level": "official_public_TKDL_record"
    },
    {
        "case_id": "1294/CHENP/2010",
        "jurisdiction": "India",
        "patent_application_no": "1294/CHENP/2010",
        "system_of_medicine": "Ayurveda",
        "ingredients": ["Piper betle", "Dolichos biflorus"],
        "traditional_use": "Treatment of obesity",
        "tkdl_reference_type": "Formulation IDs (around 49 references)",
        "examination_context": "Examiner stated the claimed composition was traditionally known and raised Section 3(p).",
        "legal_issues": ["Section 3(p)"],
        "outcome": "Examination was under process at the page's reported status.",
        "source_url": "https://www.tkdl.res.in/tkdl/langdefault/common/Examinarreport/reports/1294_CHENP_2010.asp",
        "source_date": "Unknown",
        "verified_date": "2026-08-27",
        "authority_level": "official_public_TKDL_record"
    },
    {
        "case_id": "172/DEL/2007",
        "jurisdiction": "India",
        "patent_application_no": "172/DEL/2007",
        "system_of_medicine": "Ayurveda",
        "ingredients": ["Red ochre", "Psoralea corylifolia", "Eclipta prostrata", "sulphur"],
        "traditional_use": "Vitiligo",
        "tkdl_reference_type": "Multiple TKDL formulation IDs",
        "examination_context": "Claims treated as traditional knowledge / aggregation of known properties.",
        "legal_issues": ["Traditional knowledge", "Aggregation of properties"],
        "outcome": "Application refused.",
        "source_url": "https://www.tkdl.res.in/tkdl/langdefault/common/Examinarreport/reports/172_DEL_2007.asp",
        "source_date": "Unknown",
        "verified_date": "2026-08-27",
        "authority_level": "official_public_TKDL_record"
    },
    {
        "case_id": "2242/CHE/2008",
        "jurisdiction": "India",
        "patent_application_no": "2242/CHE/2008",
        "system_of_medicine": "Ayurveda",
        "ingredients": ["Adhatoda vasica", "Aegle marmelos", "Boerhaavia diffusa", "Ficus racemosa", "Lawsonia inermis", "Tamarindus indica"],
        "traditional_use": "Haemorrhagic/bleeding and urinary conditions",
        "tkdl_reference_type": "Traditional-medicine literature",
        "examination_context": "TKDL pre-grant opposition brought prior-art references to the examiner.",
        "legal_issues": ["Pre-grant opposition", "Prior art"],
        "outcome": "Page documents the cited traditional-medicine literature.",
        "source_url": "https://www.tkdl.res.in/tkdl/langdefault/common/Examinarreport/reports/2242_CHE_2008.asp",
        "source_date": "Unknown",
        "verified_date": "2026-08-27",
        "authority_level": "official_public_TKDL_record"
    },
    {
        "case_id": "1197/CHE/2006",
        "jurisdiction": "India",
        "patent_application_no": "1197/CHE/2006",
        "system_of_medicine": "Ayurveda/Unani",
        "ingredients": ["Glycyrrhiza glabra (licorice)"],
        "traditional_use": "Osteoarthritis, fracture, stiffness/joint and related conditions",
        "tkdl_reference_type": "Multiple Ayurveda/Unani texts",
        "examination_context": "TKDL pre-grant opposition brought the traditional-use references before the examiner.",
        "legal_issues": ["Pre-grant opposition"],
        "outcome": "References brought before examiner.",
        "source_url": "https://www.tkdl.res.in/tkdl/langdefault/common/Examinarreport/reports/1197_CHE_2006.asp",
        "source_date": "Unknown",
        "verified_date": "2026-08-27",
        "authority_level": "official_public_TKDL_record"
    },
    {
        "case_id": "20100203117",
        "jurisdiction": "USPTO",
        "patent_application_no": "20100203117",
        "system_of_medicine": "Ayurveda",
        "ingredients": ["Piper betle", "Dolichos biflorus", "Commiphora mukul", "Boerhaavia diffusa", "Tribulus terrestris", "Zingiber officinale"],
        "traditional_use": "Obesity and related activities",
        "tkdl_reference_type": "Several Ayurveda books cited",
        "examination_context": "USPTO examiner took cognizance of TKDL references.",
        "legal_issues": ["Prior art"],
        "outcome": "Applicant amended claims after the cited prior art.",
        "source_url": "https://www.tkdl.res.in/tkdl/langdefault/common/Examinarreport/reports/20100203117.asp",
        "source_date": "Unknown",
        "verified_date": "2026-08-27",
        "authority_level": "official_public_TKDL_record"
    },
    {
        "case_id": "EP1927361",
        "jurisdiction": "EPO",
        "patent_application_no": "EP1927361",
        "system_of_medicine": "Ayurveda/Unani",
        "ingredients": ["Aloe barbadensis (Aloe vera)"],
        "traditional_use": "Obesity",
        "tkdl_reference_type": "Several Ayurveda/Unani sources",
        "examination_context": "EPO examiner considered TKDL citations novelty-destroying for specified claims.",
        "legal_issues": ["Novelty"],
        "outcome": "Examination was still in process on the published page.",
        "source_url": "https://www.tkdl.res.in/tkdl/langdefault/common/Examinarreport/reports/EP1927361.asp",
        "source_date": "Unknown",
        "verified_date": "2026-08-27",
        "authority_level": "official_public_TKDL_record"
    },
    {
        "case_id": "EP2226071",
        "jurisdiction": "EPO",
        "patent_application_no": "EP2226071",
        "system_of_medicine": "Ayurveda",
        "ingredients": ["Citrus limon (lemon)"],
        "traditional_use": "Obesity/slimming",
        "tkdl_reference_type": "Five Ayurveda sources cited by TKDL third-party observations",
        "examination_context": "EPO examiner said the cited documents affected novelty/inventive step of specified claims.",
        "legal_issues": ["Novelty", "Inventive step"],
        "outcome": "Applicant later amended claims.",
        "source_url": "https://www.tkdl.res.in/tkdl/langdefault/common/Examinarreport/reports/EP2226071.asp",
        "source_date": "Unknown",
        "verified_date": "2026-08-27",
        "authority_level": "official_public_TKDL_record"
    }
]

new_json = json.dumps(new_data, indent=2)
new_commented = "// --- NEW FACTUAL TKDL DATA BELOW ---\n" + new_json

with open("backend/data/tk.jsonc", "w", encoding="utf-8") as f:
    f.write(old_commented + new_commented)

print("tk.jsonc created.")
