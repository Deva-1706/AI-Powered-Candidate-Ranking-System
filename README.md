# AI-Powered Candidate Ranking System

## Overview

Built a Python-based candidate ranking system that processes 100,000 candidate profiles, performs feature engineering, calculates candidate suitability scores, ranks top candidates, and generates validated recruitment recommendations.

## Features

* Load and process 100,000 candidate profiles
* Feature engineering based on experience, education, and skills
* Automated candidate scoring engine
* Candidate ranking and selection
* CSV submission generation
* Submission validation support

## Technologies Used

* Python
* JSON
* CSV
* Data Engineering
* Feature Engineering

## Project Workflow

### V1 - Project Setup

✅ Complete

### V2 - Data Loading

✅ Complete

### V3 - Schema Analysis

✅ Complete

### V4 - Feature Engineering

✅ Complete

### V5 - Scoring Engine

✅ Complete

### V6 - Ranking System

✅ Complete

### V7 - Submission Generator

✅ Complete

### V8 - Validation

✅ Complete

## Project Structure

```text
AI-Powered-Candidate-Ranking-System/

├── config/
│   └── skill_weights.json

├── src/
│   ├── data_loader.py
│   ├── feature_engineering.py
│   ├── candidate_scorer.py
│   ├── rank_candidates.py
│   ├── generate_submission.py
│   └── honeypot_detector.py

├── README.md
├── requirements.txt
└── .gitignore
```

## Run Commands

```bash
python src/data_loader.py
python src/rank_candidates.py
python src/generate_submission.py
```

## Results

* Candidates Processed: 100,000
* Submission Generated: Yes
* Validation Passed: Yes

## Dataset

Dataset files are not included in this repository due to size limitations and challenge restrictions.

Required files:

* candidates.jsonl
* sample_candidates.json

Place these files inside the `data/` folder before running the project.

## Future Improvements

* Machine Learning Based Ranking
* Recruiter Signal Analysis
* GitHub Activity Scoring
* Explainable AI Recommendations
* Streamlit Dashboard

## Author

Devanath N
