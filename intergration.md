UDSL Developer Integration Guide (v1.0)
How to integrate the Universal Document Structure Layer into any AI model or pipeline

RenMetrix • LOOM Protocol

1. Introduction

UDSL (Universal Document Structure Layer) is a model-agnostic document architecture that enforces:

consistent structure

section intent

reasoning-mode compliance

tone routing

UX writing constraints

terminology stability

This guide explains how developers can integrate UDSL into:

ChatGPT (API or UI prompts)

Claude (API or UI)

Gemini (API or UI)

Perplexity (UI)

enterprise pipelines

multi-agent systems

RAG-based flows

custom LLM applications

2. Core Components You Must Load

Your integration must reference these files:

Layer	File	Description
Structure	/Definitions/structure/<doc_type>.yaml	Defines required/optional sections, order, length
Reasoning	/Definitions/reasoning_modes.yaml	Defines allowed reasoning patterns
Tone	/Definitions/tone_profiles.yaml	Defines voice, formality, and style
UX Rules	/Definitions/ux_rules.yaml	Defines scanning, bullet, CTA, readability rules
Terminology	/Definitions/terminology.md	Defines standard terms & banned synonyms

A compliant model must load (or be instructed to follow) all five layers.

3. Minimal Integration Template (All Models)

Use this format for any LLM:

Use UDSL v1.0 — Universal Document Structure Layer.

Load:
- Definitions/structure/<doc_type>.yaml  
- Definitions/reasoning_modes.yaml  
- Definitions/tone_profiles.yaml  
- Definitions/ux_rules.yaml  
- Definitions/terminology.md

Document State:
<insert your JSON>

TASK:
Follow the canonical outline.
Enforce reasoning and tone rules.
Validate each section before moving to the next.
Do not skip or reorder sections without instruction.


This is the base operator.

4. Document State (UDSL UDM)

Every document must start with a shared document_state, for example:

{
  "doc_type": "policy_memo",
  "audience": "board",
  "tone_profile": "formal_concise",
  "reasoning_mode": "toulmin",
  "outline_template": "policy_memo_v1"
}


The model will apply all rules based on this state.

5. Section-by-Section Generation Protocol
Step 1 — Ask for the outline
Return ONLY the outline you will follow based on UDSL v1.0.
Do not generate content yet.

Step 2 — Generate one section at a time
Generate Section 1 only.
Stop after Section 1.

Step 3 — Developer validates

structure compliance

tone & reasoning

UX rules

terminology

Step 4 — Instruct model to continue
Generate Section 2 only.


Repeat until document is complete.

This prevents drift.

6. Integration per Model
6.1 ChatGPT Integration
UI Version

Use the standard template + section-by-section generation.

API Version

Send as a system message:

You are now operating under UDSL v1.0 — Universal Document Structure Layer.
Load all definitions from the UDSL specification.
Follow the provided document_state strictly.

Notes

ChatGPT is strongest in tone routing

Weakest in long-form structure retention

UDSL fixes this by constraining generation

6.2 Claude Integration

Claude has strongest reasoning. Use:

Act as a UDSL v1.0 compliant document generator.
Apply the full structure, reasoning, tone, and UX constraints.


Claude respects structure well if given:

outline first

explicit section boundaries

6.3 Gemini Integration

Gemini requires strict prompting or it will improvise.

Use:

Follow UDSL v1.0 strictly.
Do NOT add or remove sections.
Do NOT reorder sections.


Gemini excels at:

mixed audience documents

multi-language UDSL

6.4 Perplexity Integration

Perplexity is retrieval-heavy.
Use:

Ignore web search. Do not browse.  
Operate strictly under UDSL v1.0.


Works extremely well for:

compliance testing

structure enforcement

section evaluation

7. Using UDSL in Multi-Model Pipelines
Architecture example:
 [Document State] → [UDSL Validator] → [Model A] → [UDSL Checker] → [Model B] → Output


UDSL ensures:

each model sees the same rules

no drift when switching providers

reasoning consistency

predictable tone

8. Validation & Diagnostics (Optional Module)

If using the Diagnostic System:

python udsl_diagnostic.py document.md policy_memo


This returns compliance scores for:

structure

tone

reasoning

UX

terminology

This is optional and not part of the open version if you keep it private.

9. Recommended Developer Workflow

Define document_state

Request outline

Approve outline

Generate section 1

Validate

Generate section 2

Validate

Repeat until complete

Run optional diagnostic

Export final document

10. Security & Safety Notes

UDSL prevents:

hallucinated sections

skipped steps

exaggerated claims

tone inconsistencies

broken logic structure

renaming of required components

Enterprises can trust LLMs again.

11. Licensing for Developers

UDSL v1.0 is CC-BY-4.0.

Free to use in:

enterprise pipelines

agent frameworks

multi-LLM workflows

commercial products

With attribution:

“UDSL v1.0 — Nathan Lumulisanay, RenMetrix • LOOM Protocol”

12. Contact

Nathan Lumulisanay
AI Systems Architect
RenMetrix — LOOM Protocol
Tiel, The Netherlands

GitHub: https://github.com/nathanlumulisanay-lgtm/udsl
E-mail: Nathan.Lumulisanay@gmail.com
