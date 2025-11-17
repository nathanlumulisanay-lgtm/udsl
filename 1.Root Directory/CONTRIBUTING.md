# 🤝 Contributing to UDSL (Universal Document Structure Layer)

Thank you for your interest in contributing to **UDSL v1.0** —  
a model-agnostic document structure standard for AI.

UDSL is maintained as part of the **RenMetrix — LOOM Protocol**  
and aims to be an open, transparent, auditable standard for  
long-form AI document generation.

This guide explains how to contribute, propose changes, report issues,  
and extend the standard in a consistent and safe way.

---

# 1. Code of Conduct

All contributors are expected to follow:

- respectful communication  
- clarity in technical proposals  
- no vendor bias (UDSL is model-agnostic)  
- no promotion of proprietary systems  
- citations required for research or claims  

UDSL is a **neutral standard**, not tied to any AI provider.

---

# 2. Ways to Contribute

You can contribute by:

### ✔ Improving documentation  
- clarifying definitions  
- adding examples  
- fixing structure descriptions  
- refining tone/UX rules  
- adding reasoning scenarios  

### ✔ Extending UDSL  
- proposing new doc_types  
- adding new reasoning modes  
- improving tone profiles  
- adding UX rules  
- adding terminology expansions  

### ✔ Validator contributions  
- new scoring rules  
- new test cases  
- bug fixes  
- CLI improvements  
- integrations for CI/CD  

### ✔ Research contributions  
- whitepapers  
- comparisons of LLM behaviour  
- evaluation datasets  
- multilingual adaptations  

---

# 3. Repository Structure (must be followed)

All contributions must respect the canonical directory structure:

docs/ → specification PDFs, architecture, developer guide
definitions/ → YAML/MD canonical definitions
integration/ → model integration profiles
validator/ → scoring model, CLI, examples
examples/ → UDSL-compliant example documents
scripts/ → utilities (checksums, build)
releases/ → public release artifacts (v1.0+)


Do NOT modify structure without proposal and approval.

---

# 4. Contribution Process

To propose changes:

### 1️⃣ Open an Issue  
Include:
- what you want to change  
- why it matters  
- evidence or examples  
- impact on compliance  

### 2️⃣ Discuss  
The issue will be discussed publicly.

### 3️⃣ Submit a Pull Request  
Follow the pull-request template.

Every PR must:

- reference an Issue  
- include tests or examples (if relevant)  
- update documentation if behaviour changes  
- NOT break backward compatibility of v1.0  
- NOT modify canonical definitions without approval  

---

# 5. Rules for Modifying Canonical Definitions

The following files are **protected** and must not be changed lightly:



definitions/structure.yaml
definitions/structure_matrix.yaml
definitions/reasoning_schemas.yaml
definitions/style_presets.yaml
definitions/ux_rules.yaml
definitions/terminology.md
definitions/Definitions_Index.yaml


For changes to these files, you **must**:

- open a formal proposal issue  
- justify the change with examples  
- provide backward compatibility notes  
- increment UDSL version only after approval  
- update validator and documentation accordingly  

UDSL versioning follows:



MAJOR.MINOR.PATCH


Example: `1.0.1` (patch), `1.1.0` (new doc_type), `2.0.0` (breaking change).

---

# 6. Adding New Doc Types (policy, technical, academic etc.)

To add a new doc_type:

1. Add a new YAML file in `definitions/structure/`  
2. Update `structure_matrix.yaml`  
3. Add examples under `examples/`  
4. Update validator scoring rules if needed  
5. Add documentation in `docs/`  
6. Submit PR with reasoning and use-cases  

---

# 7. Extending Reasoning, Tone, or UX Layers

Each layer must stay:

- consistent  
- minimal  
- clear  
- logically separated  

When adding:

- **reasoning modes** → justify with formal logic  
- **tone profiles** → provide examples  
- **UX rules** → explain expected improvements  
- **terminology entries** → include synonyms & preferred terms  

---

# 8. Running the Validator Before Commit

We require running the validator before committing major structure changes:

```bash
python validator/cli/udsl_validate.py --input examples/valid/example.md


All required sections must pass.

9. Licensing

All contributions are licensed under:

CC BY 4.0 — Attribution required

This ensures UDSL remains:

free

open

auditable

globally adoptable

10. Governance

UDSL is maintained by:

Nathan Lumulisanay
RenMetrix — LOOM Protocol

Major version decisions follow an open discussion process.

11. Contact

For proposals, enterprise integration or research collaborations:

📧 nathan.lumulisanay@gmail.com

Thank you for considering a contribution to UDSL.

Created and maintained by Nathan Lumulisanay.



