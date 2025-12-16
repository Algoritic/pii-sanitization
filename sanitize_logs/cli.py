import sys
import argparse
from pathlib import Path
from sanitize_logs.sanitizer import sanitize_text

def main():
    parser = argparse.ArgumentParser(
        description="Sanitize logs by masking PII. Always outputs a _safe copy."
    )
    parser.add_argument(
        "files",
        nargs="+",
        help="File(s) to sanitize. Multiple files allowed."
    )
    parser.add_argument(
        "--in-place",
        action="store_true",
        help="Overwrite the original file(s) with sanitized output."
    )
    args = parser.parse_args()

    for file_path in args.files:
        path = Path(file_path)
        if not path.exists():
            print(f"Error: File '{file_path}' not found.", file=sys.stderr)
            continue

        content = path.read_text()
        sanitized = sanitize_text(content)

        if args.in_place:
            path.write_text(sanitized)
            print(f"[OVERWRITTEN] {path}")
        else:
            new_name = path.parent / f"{path.stem}_safe{path.suffix}"
            new_name.write_text(sanitized)
            print(f"[CREATED] {new_name}")

if __name__ == "__main__":
    main()