# UDSL v1.0 — First Public Release
Date: November 2025  
Author: Nathan Lumulisanay  
Project: RenMetrix — LOOM Protocol  
Standard: Universal Document Structure Layer (UDSL)

---

## 🚀 Summary
UDSL v1.0 is the world’s first AI-native, model-agnostic document structure standard.  
It defines a canonical set of rules, layers, and validation procedures that ensure LLM-generated documents are:

- structurally consistent  
- explainable  
- auditable  
- multi-model stable  
- compliant across ChatGPT, Claude, Gemini, and Perplexity  

This release includes the full standard, canonical definitions, validator tools, integration profiles, and reference examples.

---

## 📂 Included in This Release
### 1. Core Specification
- UDSL_Core_Spec_v1.0.pdf  
- UDSL_Architecture_arXiv_Ready.pdf  
- UDSL_AI_Usage_Directive_v1.0.pdf  
- UDSL_Specification_v1.0_Expanded.pdf  

### 2. Canonical Definitions
- structure.yaml  
- structure_matrix.yaml  
- reasoning_modes.yaml  
- tone_profiles.yaml  
- ux_rules.yaml  
- terminology.md  
- Definitions_Index.yaml  

### 3. Validator Toolkit
- scoring_model.yaml  
- compliance_schema.json  
- udsl_validate.py  
- valid & invalid examples  

### 4. Integration Profiles
- ChatGPT_profile.json  
- Claude_profile.json  
- Gemini_profile.json  
- Perplexity_profile.json  

### 5. Examples
- policy memo  
- business report  
- technical report  
- model comparison sets  

### 6. Integrity Files
- checksums_sha256.txt  

---

## 🛠 Improvements in v1.0
- Full five-layer UDSL architecture  
- Complete canonical YAML/MD definition set  
- Standardized reasoning schemas  
- Validator scoring model  
- Cross-model integration  
- Minimal and expanded diagrams  
- Automated build + checksums (scripts included)  

---

## 🔒 Integrity & Verification
Use the included scripts:

generate_checksums.py
verify_checksums.py
build_release_zip.py


---

## 📣 Citation
Lumulisanay, N. (2025). *UDSL — Universal Document Structure Layer (v1.0).*  
RenMetrix — LOOM Protocol.

A machine-readable citation file (`CITATION.cff`) is included.

---

## 📄 License
Released under **CC BY 4.0**.  
Attribution required:  
“UDSL v1.0 — Lumulisanay, RenMetrix — LOOM Protocol”

---

## 🌐 Notes
This version is intended for broad public adoption, academic referencing, cross-model compatibility research, and integration within SaaS/LangChain/enterprise pipelines.


