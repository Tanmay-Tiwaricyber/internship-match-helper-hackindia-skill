"""CLI entry point for Internship Match Helper."""
import argparse
import json
from pathlib import Path

from processor import build_matches


def read_json(path: Path):
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def write_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        file.write("\n")


def main():
    parser = argparse.ArgumentParser(
        description="Rank sample internships based on a student's skills."
    )
    parser.add_argument(
        "--input", default="data/sample_students.json",
        help="Path to input JSON (default: data/sample_students.json)"
    )
    parser.add_argument(
        "--output", default="output/matches.json",
        help="Path to output JSON (default: output/matches.json)"
    )
    args = parser.parse_args()

    payload = read_json(Path(args.input))
    matches = build_matches(payload)
    write_json(Path(args.output), matches)
    print(f"Processed {len(matches['students'])} student(s).")
    print(f"Results written to: {args.output}")
    for student in matches["students"]:
        print(f"- {student['student_name']}: {len(student['matches'])} ranked match(es)")


if __name__ == "__main__":
    main()
