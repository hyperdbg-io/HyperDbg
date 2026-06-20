import os
import sys

SEARCH_TEXT = "<WindowsTargetPlatformVersion>"

def search_files(root_dir):
    matches_found = False

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    for line_num, line in enumerate(f, start=1):
                        if SEARCH_TEXT in line:
                            print(f"File : {filepath}")
                            print(f"Line {line_num}: {line.rstrip()}")
                            print("-" * 60)
                            matches_found = True
            except (PermissionError, OSError) as e:
                print(f"[Skipped] {filepath} — {e}", file=sys.stderr)

    if not matches_found:
        print("No matches found.")

if __name__ == "__main__":
    start_dir = os.getcwd() + "/.."
    print(f"Searching in: {start_dir}\n")
    search_files(start_dir)