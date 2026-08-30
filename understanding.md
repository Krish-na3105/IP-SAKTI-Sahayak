# Project Understanding & Implementation Log

## Overview
This document summarizes our investigation and the data injection process for the IP-SAKTI Sahayak application, an AI-powered Ayurvedic IP & Compliance Navigator.

## Source Data Mapping & Extraction

### 1. Trademarks Guidelines (PDF 1)
- **Target:** `backend/data/legal.json`
- **Extracted Data:** Sections 2, 9, 11, 12, 13, 18, 20-23, 25, 28-29, 30-35, 47 & 57 of the Trade Marks Act 1999. Also extracted rules related to Ayurveda-specific interpretations (e.g., how Ayurvedic brands are assessed under the general TM framework and may be subject to AYUSH rules).

### 2. Official IP Costs (PDF 2)
- **Target:** `backend/data/fees.json`
- **Extracted Data:** Comprehensive fee schedule for Trademarks (TM-A e-filing/physical, Opposition, Review, Expedited) and Patents (Form 1, 9, 18, 18A, 8) mapping 'Individual/Startup/Small Enterprise' vs 'Others'.
- **Bug Fix:** Fixed an existing logic bug in `frontend/src/app/cost/page.tsx` where Educational Institutions were incorrectly grouped with Small Enterprises for Trademark TM-A filing fees. The logic now properly charges Educational Institutions the ₹9,000 "Other" fee for Trademarks while keeping the discounted ₹1,600 fee for Patents.

### 3. TKDL Publicly Verifiable Examples (PDF 3)
- **Target:** `backend/data/tk.jsonc` (Renamed from `tk.json` to allow comments)
- **Extracted Data:** 9 factual patent examination cases involving TKDL citations across India, EPO, and USPTO jurisdictions. 
- **Modifications:** 
  - Updated the backend Python parser (`app/main.py`) to support `.jsonc` by stripping comments using regular expressions before passing to `json.loads`.
  - Added a block comment in `tk.jsonc` preserving the old synthetic data (since its schema `formulation_name` etc. was incompatible with the new `case_id` factual schema).
  - Updated the frontend Knowledge Base page (`src/app/knowledge/page.tsx`) to render the new patent case schema accurately without breaking the UI.

### 4. Guidelines for Ayush Related Inventions (PDF 4)
- **Target 1:** `backend/data/patents.json` (Real-world Granted Patents)
  - Replaced the synthetic data with real granted patents mentioned in the guidelines, such as "Smart Wearable device", "Herbal sanitary pad", "A novel antimicrobial polyherbal composition", and the "AYUSH-64" anti-malarial drug.
- **Target 2:** `backend/data/legal.json` (Legal & Policy Guidelines)
  - Extracted Sections 2 and 3(a)-3(p) of the Patents Act, Section 6 of the Biological Diversity Act, and Guiding Principles 1-6 for the assessment of Ayush patent applications.

## Conclusion
All JSON files were fully overwritten with factual, official data from the provided source PDFs, effectively purging the previous AI-generated synthetic demonstration data. The application is now running with factually accurate reference materials for IP costs, TKDL evidence, Ayurvedic patent guidelines, and trademarks.