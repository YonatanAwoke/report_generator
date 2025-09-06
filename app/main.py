# app/main.py
from fastapi import FastAPI, UploadFile, HTTPException
from starlette.responses import FileResponse
import json
import os
from app.agents.report_agent import ReportAgent

app = FastAPI()
agent = ReportAgent()

# Ensure output folder exists
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.post("/generate-report")
async def generate_report(file: UploadFile):
    try:
        # Load JSON data from uploaded file
        data = json.load(file.file)
        file.file.close()

        # Generate unique PDF filename
        pdf_path = os.path.join(OUTPUT_DIR, "final_report.pdf")

        # Use ReportAgent to generate PDF
        agent.create_report(data, pdf_path)

        return FileResponse(pdf_path, media_type='application/pdf', filename='final_report.pdf')

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))