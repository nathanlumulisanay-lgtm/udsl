import json
import yaml
import sys
import re

def load_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def load_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def extract_sections(text):
    return re.findall(r'^# (.+)', text, re.MULTILINE)

def validate_document(path):
    doc_text = load_text(path)
    sections = extract_sections(doc_text)

    compliance = {
        "udsl_compliance_score": 100,
        "structure": {"missing_sections": [], "unexpected_sections": []},
        "reasoning": {"missing_elements": []},
        "tone": {"issues": []},
        "ux": {"issues": []},
        "terminology": {"issues": []}
    }

    schema = load_yaml("../definitions/structure/policy_memo.yaml")
    required_sections = schema.get("outline", [])

    # STRUCTURE CHECK
    for sec in required_sections:
        if sec not in sections:
            compliance["structure"]["missing_sections"].append(sec)
            compliance["udsl_compliance_score"] -= 8

    for sec in sections:
        if sec not in required_sections:
            compliance["structure"]["unexpected_sections"].append(sec)
            compliance["udsl_compliance_score"] -= 3

    # REASONING CHECK (simple placeholder)
    if "Claim:" not in doc_text:
        compliance["reasoning"]["missing_elements"].append("claim")
        compliance["udsl_compliance_score"] -= 10

    if "Warrant:" not in doc_text:
        compliance["reasoning"]["missing_elements"].append("warrant")
        compliance["udsl_compliance_score"] -= 10

    return compliance

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python udsl_validate.py <document>")
        sys.exit(1)

    result = validate_document(sys.argv[1])
    print(json.dumps(result, indent=2))
