# 🔗 UDSL Integration Guide (v1.0)

This guide explains how to integrate UDSL into:

- ChatGPT  
- Claude  
- Gemini  
- Perplexity  
- custom LLMs  
- RAG pipelines  
- multi-model agents  
- enterprise AI platforms  
- SaaS & automation tools  

UDSL is **model-agnostic**: every AI system can follow UDSL as long as it uses the canonical definitions in `definitions/`.

---

# 1. Overview

UDSL is designed to be integrated into any AI pipeline that generates long-form documents.

Integration examples:

- prompting (manual use)
- system prompt injection
- agent frameworks
- template systems
- pre-generation validation
- post-generation scoring
- enterprise RAG workflows
- SaaS document generation

The directory contains:

integration/
├─ ChatGPT_profile.json
├─ Claude_profile.json
├─ Gemini_profile.json
├─ Perplexity_profile.json
└─ README.md ← this file


Each profile describes how the specific model should interact with UDSL.

---

# 2. Model-Agnostic Integration Principles

Regardless of model, UDSL requires:

1. **Document parameters**  
   - doc_type  
   - tone_profile  
   - reasoning_mode  
   - audience  
   - (optional) language

2. **Canonical structure enforcement**  
   Models must follow `structure.yaml` exactly.

3. **Reasoning mode enforcement**  
   Using `reasoning_schemas.yaml`.

4. **Tone routing**  
   Based on `style_presets.yaml`.

5. **UX rules**  
   Based on `ux_rules.yaml`.

6. **Terminology consistency**  
   Based on `terminology.md`.

---

# 3. Integration with ChatGPT

Profile: `ChatGPT_profile.json`

### Strengths:
- strong structure-following (when explicitly instructed)
- high responsiveness to reasoning-mode constraints
- good tone control

### Limitations:
- prone to over-elaboration in long documents
- sometimes adds extra headings unless told “DO NOT INVENT SECTIONS”

### Recommended system prompt:



You are an AI system that MUST follow the UDSL v1.0 standard.
Use the canonical structure from structure.yaml.
Use reasoning mode from reasoning_schemas.yaml.
Do NOT invent sections.


### Recommended parameters:

```json
{
  "doc_type": "policy_memo",
  "tone_profile": "formal_concise",
  "reasoning_mode": "toulmin",
  "audience": "board"
}

4. Integration with Claude

Profile: Claude_profile.json

Strengths:

excellent coherence in long documents

very strong reasoning performance

good adherence to hierarchical structure

Limitations:

may compress sections too aggressively

can merge multiple reasoning steps into one paragraph

Recommended prompt style:
Follow only the structure specified by UDSL v1.0.
Output sections EXACTLY as defined.
Apply reasoning schema without merging elements.

5. Integration with Gemini

Profile: Gemini_profile.json

Strengths:

strict formatting compliance

strong control over tone and UX writing

handles multilingual output very well

Limitations:

reasoning sometimes underdeveloped

can skip optional sections, even when relevant

Recommended prompt:
Follow the UDSL v1.0 canonical structure.
Explicitly include required reasoning elements.
Do not skip optional sections if relevant.

6. Integration with Perplexity

Profile: Perplexity_profile.json

Strengths:

excellent factual grounding

good extractive content quality

very strong for reports requiring citations

Limitations:

weaker on structured reasoning (Toulmin)

tends to shorten summaries too much

may simplify tone too heavily

Recommended guidance:
Follow UDSL v1.0 strictly.
Ensure all Toulmin reasoning elements are included.
Do not overcompress sections.

7. Integration with Custom / Local LLMs

UDSL can be integrated with:

Llama

Mistral

Falcon

Qwen

Grok

GPT-J

internal enterprise models

Integration method:

Add canonical definitions in your model’s system prompt

Restrict structural output with explicit headings

Post-validate using UDSL Validator

Use deterministic decoding for consistency (low temperature)

8. Integration in RAG Pipelines

UDSL is compatible with:

LangChain

LlamaIndex

Haystack

custom RAG frameworks

Typical flow:

STEP 1: Retrieve knowledge
STEP 2: Insert UDSL document parameters
STEP 3: Apply UDSL canonical structure
STEP 4: Generate with model
STEP 5: Validate using UDSL Validator
STEP 6: Post-process using tone & UX rules


This ensures retrieval does not disrupt structure.

9. Integration with Agents (AI Orchestration)

UDSL works well with agent systems like:

GPTs

CrewAI

AutoGPT

BabyAGI

ReAct agents

Microsoft Copilot agents

Anthropic Worker agents

Agent roles:

Structure enforcer

Reasoning checker

Tone router

UX reviewer

Terminology normalizer

Agents can call the validator to check each draft.

🔟 Industry & Enterprise Integration Examples
🏛 Government / Public Policy

Forcing consistent “policy memo” structures

Enforcing evidence-based reasoning

Reducing outline drift in official documents

🏢 Corporate

Annual reports

Risk assessments

Compliance documentation

Board memos

⚖ Legal / Compliance

Standardized briefing notes

Auditable reasoning schemas

Meeting regulatory formatting requirements

🎓 Academia / Research

Structured papers

Technical briefs

Literature summaries

11. Integration Best Practices

Always specify:

{
  "doc_type": "...",
  "tone_profile": "...",
  "reasoning_mode": "...",
  "audience": "..."
}


Always include in the prompt:

“Follow the canonical structure defined in UDSL v1.0. Do NOT invent sections.”

Always validate after generation.

Always version your UDSL definitions.

12. Vendor Independence Disclaimer

UDSL is independent and not affiliated with any LLM vendor.

References to ChatGPT, Claude, Gemini or Perplexity indicate compatibility only.
No endorsement, partnership or certification is implied.

13. License

Released under CC BY 4.0.
Attribution required:

“UDSL v1.0 — Lumulisanay, RenMetrix — LOOM Protocol”