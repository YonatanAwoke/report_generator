# AI Report Generator

This project is an AI report generator that converts structured JSON into a branded 20-page PDF using HTML/CSS + WeasyPrint and Gemini for text generation.

## Setup

1. Install the dependencies:
```bash
pip install -r requirements.txt
```

2. Set the `GEMINI_API_KEY` environment variable:
```bash
export GEMINI_API_KEY="your_gemini_key"
```

## Run

To run the FastAPI server:
```bash
uvicorn app.main:app --reload
```

Then, you can send a POST request to `http://127.0.0.1:8000/generate-report` with a JSON file to generate a report.
