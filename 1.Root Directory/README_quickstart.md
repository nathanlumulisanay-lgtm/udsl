# 🚀 UDSL Quickstart (v1.0)

This guide is for **developers**, **AI power-users**, **researchers**, and **QA teams** who want to:

- Generate UDSL-compliant documents  
- Validate AI output against the UDSL standard  
- Integrate UDSL into pipelines, assistants, or SaaS tools  

UDSL = **Universal Document Structure Layer**  
A model-agnostic architecture for consistent, explainable, auditable AI-generated documents.

---

# 1️⃣ Core Concepts

Every UDSL-compliant document is defined by **five parameters**:

| Parameter | Purpose | Example |
|----------|----------|---------|
| `doc_type` | Defines the document’s outline | `policy_memo`, `technical_report`, `business_case` |
| `tone_profile` | Controls stylistic voice | `formal_concise`, `neutral_academic` |
| `reasoning_mode` | Controls how reasoning structures appear | `toulmin`, `deductive`, `inductive`, `scenario` |
| `audience` | Tunes tone, density & UX | `board`, `general_public`, `expert` |
| `language` | (Optional) Preferred language | `en`, `nl`, `es`, `ar`, etc. |

All parameters map directly to the **canonical YAML/MD files** inside `definitions/`.

---

# 2️⃣ Generate a UDSL-Compliant Document (LLM Prompt)

Use this prompt in **ChatGPT, Claude, Gemini, Perplexity, or any LLM**:

> **You are an AI system that MUST follow the UDSL v1.0 standard.**  
> doc_type = `policy_memo`  
> tone_profile = `formal_concise`  
> reasoning_mode = `toulmin`  
> audience = `board`  
>  
> Follow the canonical outline defined in `structure.yaml`, and apply reasoning rules from `reasoning_schemas.yaml`.  
> Do NOT invent your own structure.  
> Always output in sections exactly as required by UDSL.

To switch the document type, just change `doc_type`.

---

# 3️⃣ Programmatic Generation Example (Python)

```python
from udsl import generate_document

doc = generate_document(
    doc_type="policy_memo",
    tone_profile="formal_concise",
    reasoning_mode="toulmin",
    audience="board",
    content="Summarize the environmental impact of urban heat islands."
)

print(doc)
Note: The Python library is not published yet — this snippet shows the expected API shape for integrations.
4️⃣ Validate an AI-Generated Document (Basic Flow)

You can construct a UDSL validator using the provided schemas:
definitions/structure.yaml
definitions/reasoning_schemas.yaml
definitions/style_presets.yaml
definitions/ux_rules.yaml
definitions/terminology.md
validator/scoring_model.yaml

A typical validation process:

Step 1 — Parse

Split the document into sections.

Step 2 — Compare

Compare sections to structure.yaml

Evaluate reasoning using reasoning_schemas.yaml

Check tone/style with style_presets.yaml

Apply UX constraints from ux_rules.yaml

Enforce terminology rules via terminology.md

Step 3 — Score

Apply the rules in validator/scoring_model.yaml.

5️⃣ Example Validation Output
{
  "udsl_compliance_score": 82,
  "structure": {
    "in_outline": true,
    "missing_elements": ["executive_summary"]
  },
  "reasoning": {
    "mode": "toulmin",
    "compliance_score": 75
  },
  "tone": {
    "compliance_score": 90
  },
  "ux": {
    "scannability_ok": true
  },
  "terminology": {
    "issues": []
  }
}
This is representative output — UX/terminology rules are customizable per implementation.

6️⃣ CLI Validator (Reference Implementation)

UDSL includes a reference CLI validator:
validator/cli/udsl_validate.py

Usage:
python udsl_validate.py --input my_doc.md
Outputs JSON compliance results.

7️⃣ Compare Multiple LLMs (Side-by-Side)

You can compare different model outputs via:
examples/comparison/

Includes formats for:

ChatGPT

Claude

Gemini

Perplexity

Useful for research & benchmark testing.

8️⃣ SaaS / API Integration (Preview)

UDSL can be turned into a SaaS validator API:

POST /validate
{
  "doc_type": "policy_memo",
  "text": "LLM output here",
  "tone_profile": "formal_concise",
  "reasoning_mode": "toulmin",
  "audience": "board"
}

Response:
{
  "udsl_compliance_score": 87,
  "critical_issues": [],
  "suggestions": []
}

9️⃣ Troubleshooting

❗ My LLM ignores the required structure
→ Add: “Do NOT invent your own structure”
→ Ensure doc_type is supported in structure.yaml

❗ Tone is too informal
→ Use a stricter tone_profile
→ Check style_presets.yaml

❗ Reasoning missing
→ Explicitly set reasoning_mode = toulmin (or another)

❗ Too long or messy output
→ Set audience to board or executive
→ These profiles enforce conciseness

🔟 Where to go next?

See README_full.md for the complete UDSL explanation

See README_enterprise.md for organizational adoption

See validator/ to build your own quality gate

See integration/ for model-specific profiles

📄 License

UDSL is released under CC BY 4.0
Attribution required:

“UDSL v1.0 — Lumulisanay, RenMetrix — LOOM Protocol”

🙌 Acknowledgements

UDSL v1.0 was developed using multi-model synthesis across
ChatGPT, Claude, Gemini and Perplexity, combined with original
architectural design by Nathan Lumulisanay (RenMetrix — LOOM Protocol).
