# Redrob Intelligent Candidate Ranking System

## Overview

This project ranks candidates for the Redrob Intelligent Candidate Discovery & Ranking Challenge.

The system analyzes candidate profiles, skills, experience, education, and behavioral signals to identify the top 100 candidates for the target job description.

## Features

* Load 100,000 candidate records
* Extract candidate features
* Calculate skill and experience scores
* Detect suspicious or honeypot profiles
* Rank candidates by overall fit
* Generate submission CSV
* Validate output before submission

## Project Structure

```text
redrob-ranker/
│
├── data/
│   ├── candidates.jsonl.gz
│   ├── sample_candidates.json
│
├── config/
│   ├── skill_weights.json
│
├── src/
│   ├── data_loader.py
│   ├── feature_engineering.py
│   ├── candidate_scorer.py
│   ├── honeypot_detector.py
│   ├── rank_candidates.py
│   ├── generate_submission.py
│
├── output/
│   ├── submission.csv
│
├── validate_submission.py
├── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python src/rank_candidates.py
```

## Output

The system generates:

```text
output/submission.csv
```

## Author

Devanath

## Challenge

Redrob Intelligent Candidate Discovery & Ranking Challenge 2026
