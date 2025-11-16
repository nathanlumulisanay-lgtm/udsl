# 🧪 UDSL Validator — Official Guide (v1.0)

The UDSL Validator ensures that any document — human-written or LLM-generated — is fully compliant with the **Universal Document Structure Layer (UDSL v1.0)**.

It checks:

- structure  
- reasoning  
- tone & style  
- UX rules  
- terminology consistency  
- completeness  
- audience alignment  

The validator produces a **JSON report** suitable for automated QA, CI/CD pipelines, enterprise quality gateways, and research comparisons.

---

# 1. What the Validator Does

The validator examines a document against the canonical definitions in:

definitions/structure.yaml
definitions/structure_matrix.yaml
definitions/reasoning_schemas.yaml
definitions/style_presets.yaml
definitions/ux_rules.yaml
definitions/terminology.md
validator/scoring_model.yaml
validator/compliance_schema.json


Outputs include:

- a global **UDSL compliance score**  
- detection of missing or extra sections  
- reasoning completeness score  
- tone/style alignment score  
- UX scoring  
- terminology flags  
- critical issues  

---

# 2. Validator Output Format (JSON)

Example output:

```json
{
  "udsl_compliance_score": 84,
  "structure": {
    "in_outline": true,
    "missing": ["executive_summary"],
    "extra": []
  },
  "reasoning": {
    "mode": "toulmin",
    "score": 78,
    "missing_elements": ["warrant"]
  },
  "tone": {
    "score": 90,
    "issues": []
  },
  "ux": {
    "score": 72,
    "issues": ["long_paragraphs"]
  },
  "terminology": {
    "issues": ["inconsistent term: stakeholder(s)"]
  },
  "critical_issues": [],
  "suggestions": [
    "Add a warrant to support the main claim.",
    "Shorten long paragraphs for better scannability."
  ]
}


This format is stable and intended for:

dashboards

QA tools

internal policy gateways

enterprise document review systems

3. Validator Components

The validator consists of four major components:

validator/
│
├─ scoring_model.yaml
├─ compliance_schema.json
├─ examples/
│    ├─ valid/
│    └─ invalid/
└─ cli/
     └─ udsl_validate.py

✔ scoring_model.yaml

Defines how points are awarded/deducted.

✔ compliance_schema.json

Defines the expected structure of the validation output.

✔ examples/

Useful for testing validator implementations.

✔ cli/udsl_validate.py

Reference Python CLI validator.

4. How to Use the CLI Validator

You can run the reference validator locally:

python validator/cli/udsl_validate.py --input draft.md


Optional arguments:

--format json       # default
--format text       # human-friendly summary

--strict            # fail if any required element is missing
--verbose           # show intermediate checks


Example (text mode):

UDSL Validation Report
----------------------
Structure: PASS (1 missing section)
Reasoning: PARTIAL (warrant missing)
Tone: PASS
UX: Needs improvement (long paragraphs)
Terminology: PASS

Overall score: 84/100

5. Programmatic Usage (Python Reference)
from udsl_validator import validate

result = validate(
    text=document_text,
    doc_type="policy_memo",
    tone_profile="formal_concise",
    reasoning_mode="toulmin",
    audience="board"
)

print(result["udsl_compliance_score"])


Note: This API shape is provided for teams implementing their own validators.

6. How Validation Works (Internals)

Validation is performed in five phases:

6.1 Structure Validation

Compares document sections to:

required

optional

conditional

From structure.yaml.

Checks:

missing sections

unexpected sections

ordering issues

6.2 Reasoning Validation

Applies reasoning schema rules from:

definitions/reasoning_schemas.yaml


Example: Toulmin requires:

claim

grounds

warrant

backing

Missing items reduce the reasoning score.

6.3 Tone & Style Validation

Checks:

sentence length

formality

voice

tone alignment

style violations

From style_presets.yaml.

6.4 UX Writing Validation

Checks:

scannability

paragraph density

heading clarity

CTAs

transitions

From ux_rules.yaml.

6.5 Terminology Validation

Matches text against:

official glossary

preferred terms

discouraged terms

synonyms

From terminology.md.

7. Enterprise Integration

The validator can be integrated into:

✔ CI/CD

Fail builds if documents do not pass UDSL.

✔ Internal approval workflows

Policy memos, reports, or risk assessments must meet minimum scores.

✔ Multi-model LLM evaluation

Compare ChatGPT vs Claude vs Gemini vs Perplexity.

✔ Document governance systems

Ensure consistent structure across departments.

✔ SaaS (planned)

A REST API version of the validator is planned for 2026.

Example:

POST /validate

8. Extending the Validator

Teams may customize:

doc_types

tone profiles

UX rules

reasoning schemas

scoring thresholds

All extensions must remain compatible with:

compliance_schema.json

9. Testing the Validator

Use the built-in examples:

validator/examples/valid/
validator/examples/invalid/


To test implementation correctness:
python validator/cli/udsl_validate.py --input validator/examples/valid/policy_memo_example.md

10. Contributing

Contributions to the validator are welcome:

new scoring models

new example sets

new doc_types

bug reports

test suites

See CONTRIBUTING.md.

11. License

The validator is released under:

CC BY 4.0 — Attribution required:

“UDSL v1.0 — Lumulisanay, RenMetrix — LOOM Protocol”

12. Contact

For validator questions or enterprise adoption support:

📧 nathan.lumulisanay@gmail.com