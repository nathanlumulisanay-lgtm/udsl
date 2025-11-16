import os
import zipfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUTPUT = os.path.join(ROOT, "UDSL_Public_v1.0.zip")

EXCLUDES = {
    ".git",
    ".github",
    "checksums.txt",
    "scripts"
}

def should_exclude(path):
    for ex in EXCLUDES:
        if ex in path.split(os.sep):
            return True
    return False

if __name__ == "__main__":
    with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED) as zipf:
        for base, dirs, files in os.walk(ROOT):
            if should_exclude(base):
                continue
            for f in files:
                full = os.path.join(base, f)
                if should_exclude(full):
                    continue
                rel = os.path.relpath(full, ROOT)
                zipf.write(full, rel)

    print(f"Created release zip: {OUTPUT}")
