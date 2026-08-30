import json

fees_data = {
  "currency": "INR",
  "notice": "Official IP Costs — India (2026). Physical filing attracts 10% additional fee. Patent fees may additionally depend on specification pages, claims and other proceedings.",
  "patent": {
    "application": {
      "individual_startup_small_educational": 1600,
      "other": 8000
    },
    "early_publication": {
      "individual_startup_small_educational": 2500,
      "other": 12500
    },
    "examination": {
      "individual_startup_small_educational": 4000,
      "other": 20000
    },
    "expedited_examination": {
      "individual_startup_small_educational": 8000,
      "other": 60000
    },
    "inventor_form_8": {
      "individual_startup_small_educational": 800,
      "other": 4000
    },
    "physical_surcharge_percent": 10
  },
  "trademark": {
    "tm_a_efile": {
      "individual_startup_small": 4500,
      "other": 9000
    },
    "tm_a_physical": {
      "individual_startup_small": 5000,
      "other": 10000
    },
    "opposition_rectification_efile": 1800,
    "opposition_rectification_physical": 2000,
    "review_petition_efile": 2700,
    "review_petition_physical": 3000,
    "expedited_registration": {
      "individual_startup_small": 20000,
      "other": 40000
    },
    "well_known_request": 100000,
    "tm_a_note": "per mark, per class"
  }
}

with open("backend/data/fees.json", "w", encoding="utf-8") as f:
    json.dump(fees_data, f, indent=2)

print("fees.json updated.")
