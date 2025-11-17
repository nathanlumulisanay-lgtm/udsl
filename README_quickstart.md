# UDSL v1.0 — Universal Document Structure Layer
A model-agnostic standard for generating consistent, multi-section, long-form documents using AI.

Part of the RenMetrix • LOOM Protocol  
Author: Nathan Lumulisanay

---

## 🚀 What is UDSL?

UDSL (Universal Document Structure Layer) is a AI-native document architecture that enables Large Language Models (LLMs) to generate structured, hierarchical, and consistent long-form documents.

LLMs generate tokens — not documents.  
UDSL provides the missing layer:

- a shared structure ontology  
- reasoning mode enforcement  
- tone & style routing  
- UX-writing constraints  
- a cross-model integration protocol  
- integrity + metadata system

UDSL is **not** a content generator.  
It is a **structure engine** that any LLM can follow.

---

## 📁 Repository Structure
UDSL/
├─ Definitions/ # Structure, reasoning, tone, UX rules
│ ├─ structure/
│ ├─ reasoning_modes.yaml
│ ├─ tone_profiles.yaml
│ ├─ ux_rules.yaml
│ └─ Definitions_Index.yaml
│
├─ Integration/ # ChatGPT, Claude, Gemini, Perplexity mappings
├─ Examples/ # Input/output examples per document type
├─ Metadata/ # Checksums, proof-of-origin, integrity data
├─ Schemas/ # JSON schema for automated tooling
├─ generate_checksum.py # Integrity generator
├─ spec.md # Full technical specification (UDSL v1.0)
└─ README.md # (this file)


---

## 🧩 Core Concepts

### **1. Structure Layer**
Defines mandatory, optional, and conditional sections per document type.  
Located in: `Definitions/structure/`

### **2. Reasoning Schema Layer**
Toulmin, deductive, inductive, scenario and decision models.  
Located in: `Definitions/reasoning_modes.yaml`

### **3. Tone & Style Routing**
Controls formality, voice, density, and reading level.  
Located in: `Definitions/tone_profiles.yaml`

### **4. UX Writing Rules**
Scannability, bullet-logic, CTA quality, paragraph limits.  
Located in: `Definitions/ux_rules.yaml`

### **5. Multi-Model Integration**
Ensures ChatGPT, Claude, Gemini, and Perplexity interpret UDSL consistently.  
Located in: `Integration/`

---

## ⚡ Quick Start (for AI Models or Pipelines)

To generate a UDSL-compliant document:


Use UDSL v1.0 — Universal Document Structure Layer.
Document type: <doc_type>
Audience: <audience>
Tone profile: <tone_profile>
Reasoning mode: <reasoning_mode>

Follow all definitions in:

Definitions/structure/<doc_type>.yaml

Definitions/reasoning_modes.yaml

Definitions/tone_profiles.yaml

Definitions/ux_rules.yaml


UDSL enforces:

- outline order  
- section intent  
- reasoning completeness  
- tone consistency  
- UX constraints  
- terminology stability  

---

## 📘 Examples

Examples for all major document types are available in `/Examples/`:

- business_report  
- policy_memo  
- mixed_audience  
- model_comparison  
- technical_document  
- educational_module  

Each example includes:

- `input_udsl.json` — document state  
- `output.md` — generated example  
- `notes.md` — evaluation notes  

---

## 🔍 Integrity & Metadata

UDSL includes a reproducible integrity system.

Run:



python generate_checksum.py


This updates:

- `Definitions_Index.yaml`
- `Integration_Index.yaml`
- `metadata.json`
- `proof_of_origin.txt`

---

## 📜 License

UDSL v1.0 is released under **CC-BY-4.0**.  
You are free to use, modify, and distribute with attribution:

**“UDSL v1.0 — Nathan Lumulisanay, RenMetrix • LOOM Protocol”**

“UDSL is an independent, model-agnostic standard.
All references to AI models (e.g., ChatGPT, Claude, Gemini, Perplexity)
are compatibility descriptions only.
These companies do not endorse or certify this standard.”
---

## 🌐 Keywords (AI Discovery)

Universal Document Structure Layer  
AI document engine  
Document ontology  
LLM structure protocol  
Reasoning schema  
Model-agnostic framework  
Long-form document standard




