#!/usr/bin/env python3
"""
Walks the parent directory of this script (and all of its subdirectories)
looking for .vcxproj files.
"""

import os

TARGET_SDK_WDK_VERSION = "10.0.28000.0"

REPLACEMENTS = {
    "<WindowsTargetPlatformVersion>10.0</WindowsTargetPlatformVersion>": "<WindowsTargetPlatformVersion>" + TARGET_SDK_WDK_VERSION + "</WindowsTargetPlatformVersion>",
    "<WindowsTargetPlatformVersion>$(LatestTargetPlatformVersion)</WindowsTargetPlatformVersion>": "<WindowsTargetPlatformVersion>" + TARGET_SDK_WDK_VERSION + "</WindowsTargetPlatformVersion>",
}


def replace_in_file(filepath: str) -> bool:
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    original = content
    for old, new in REPLACEMENTS.items():
        content = content.replace(old, new)

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False


def main() -> None:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    target_root = os.path.dirname(script_dir) + "\\hyperdbg"

    print(f"Scanning for .vcxproj files under: {target_root}")

    changed_count = 0
    for root, _dirs, files in os.walk(target_root):
        for file in files:
            if file.endswith(".vcxproj"):
                filepath = os.path.join(root, file)
                if replace_in_file(filepath):
                    print(f"Updated: {filepath}")
                    changed_count += 1

    print(f"Done. {changed_count} file(s) updated.")


if __name__ == "__main__":
    main()
