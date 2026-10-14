# Internship Match Helper

A small, beginner-friendly Python CLI that ranks sample internships against student skills. It runs locally with mock data, so no paid API or secret key is needed.

## Problem

Students often see many internship listings and need a quick way to identify roles that match the skills they already have.

## What it does

- Reads student and internship records from JSON.
- Normalizes skill names for case-insensitive matching.
- Calculates a simple match percentage from required skills.
- Lists matched and missing skills.
- Writes ranked results to a JSON output file.
- Uses a local mock API module so the demo works offline.

> This is a prototype for learning and demonstration, not a production job recommendation service. Match scores only reflect overlap with the sample required skills.

## Requirements

- Python 3.10 or newer
- No third-party Python packages

## Setup

### Windows PowerShell

```powershell
git clone https://github.com/Tanmay-Tiwaricyber/internship-match-helper-hackindia-skill.git
cd internship-match-helper
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### macOS / Linux

```bash
git clone https://github.com/Tanmay-Tiwaricyber/internship-match-helper-hackindia-skill.git
cd internship-match-helper
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Replace `YOUR-USERNAME` with your GitHub username after you create the repository. If you already downloaded this project as a ZIP, extract it and `cd` into the extracted folder instead of running `git clone`.

## Run

From the project root:

```bash
python main.py --input data/sample_students.json --output output/matches.json
```

Expected terminal output resembles:

```text
Processed 2 student(s).
Results written to: output/matches.json
- Aarav Sharma: 4 ranked match(es)
- Meera Singh: 4 ranked match(es)
```

The generated file is `output/matches.json`. A sample output is also included at `output/sample_matches.json`.

## Project structure

```text
internship-match-helper/
├── main.py
├── processor.py
├── mock_api.py
├── requirements.txt
├── .env.example
├── .gitignore
├── data/
│   └── sample_students.json
├── output/
│   └── sample_matches.json
└── tests/
    └── test_processor.py
```

## Input format

The input JSON contains `students` and `internships` lists. Each student has an `id`, `name`, and `skills` list. Each internship has an `id`, `title`, `company`, `location`, and `required_skills` list.

## Test

```bash
python -m unittest discover -s tests -v
```

## API and secrets

The current version uses `mock_api.py`; it does not call a live external API and does not need credentials. `.env.example` contains placeholders only. Never commit a real `.env` file, API key, token, or password.

## Limitations and next steps

- Matching is based only on skill overlap.
- Sample internships are fictional mock records.
- A future version could add a real internship API, user interface, persistence, and stronger ranking.

## Submission checklist

- [ ] Create a public GitHub repository.
- [ ] Push all project files except `.venv/` and `.env`.
- [ ] Open the repository in a private/incognito window to check public access.
- [ ] Follow the README commands from a fresh clone.
- [ ] Review the specific HackIndia event's submission rules, demo/video requirements, and deadline.
- [ ] Paste the public repository URL into the official submission form.
