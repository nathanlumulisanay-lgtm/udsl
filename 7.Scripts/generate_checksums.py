import os
import hashlib

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

OUTPUT_FILE = os.path.join(ROOT, "checksums.txt")

def sha256_of_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def collect_files(root):
    for base, _, files in os.walk(root):
        for f in files:
            # skip the checksum file itself
            if f == "checksums.txt":
                continue
            yield os.path.join(base, f)

if __name__ == "__main__":
    entries = []
    for filepath in collect_files(ROOT):
        checksum = sha256_of_file(filepath)
        rel = os.path.relpath(filepath, ROOT)
        entries.append(f"{checksum}  {rel}")

    entries.sort()

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write("\n".join(entries))

    print(f"Generated {OUTPUT_FILE} with {len(entries)} entries.")
