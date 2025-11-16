import os
import hashlib

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CHECKSUM_FILE = os.path.join(ROOT, "checksums.txt")

def sha256_of_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

if __name__ == "__main__":
    if not os.path.exists(CHECKSUM_FILE):
        print("No checksums.txt found. Run generate_checksums.py first.")
        exit(1)

    # Load expected checksums
    expected = {}
    with open(CHECKSUM_FILE, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("  ")
            if len(parts) == 2:
                checksum, filename = parts
                expected[filename] = checksum

    failed = []
    for filename, recorded_checksum in expected.items():
        fullpath = os.path.join(ROOT, filename)
        if not os.path.exists(fullpath):
            failed.append((filename, "MISSING"))
            continue

        current = sha256_of_file(fullpath)
        if current != recorded_checksum:
            failed.append((filename, "CHANGED"))

    if not failed:
        print("All files verified successfully.")
    else:
        print("Checksum mismatches found:")
        for f, issue in failed:
            print(f" - {f}: {issue}")
