# app/agents/report_agent.py
from app.services.json_validator import ReportInput
from app.agents.gemini_client import GeminiClient
from app.services.html_renderer import render_html
from app.services.pdf_generator import generate_pdf_from_html
import tempfile, os
import json
import matplotlib.pyplot as plt
import io
import base64

def save_line_chart_to_base64(x, y):
    img_buffer = io.BytesIO()
    plt.figure(figsize=(6,3))
    plt.plot(x, y, marker='o')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(img_buffer, format='png')
    plt.close()
    img_buffer.seek(0)
    base64_str = base64.b64encode(img_buffer.read()).decode('utf-8')
    return f"data:image/png;base64,{base64_str}"

class ReportAgent:
    def __init__(self):
        self.gemini = GeminiClient()

    def create_report(self, json_data, output_pdf_path):
        # Validate JSON
        validated = ReportInput(**json_data).dict()

        for section in validated['sections']:
            if section['type'] == 'text':
                data = section.get('data', None)
                if data:
                    # Build a proper prompt for Gemini using the section data
                    prompt = (
                        f"Write a professional and concise section titled '{section['title']}' "
                        f"for a company report. Use the following structured data:\n"
                        f"{json.dumps(data, indent=2)}\n"
                        "Make it suitable for a formal PDF report."
                    )
                    section['content'] = self.gemini.generate_text(prompt)
                else:
                    # If no data, keep a placeholder
                    section['content'] = f"Data not provided for section '{section['title']}'."

            elif section['type'] == 'chart':
                chart_info = section.get('content', {})
                chart_type = chart_info.get('chart_type', 'line')
                
                if chart_type == 'line':
                    image_path = save_line_chart_to_base64(chart_info.get('x', []), chart_info.get('y', []))
                    section['image_path'] = image_path

        # Render HTML
        tmp_html = os.path.join(tempfile.gettempdir(), "report.html")
        render_html(validated, tmp_html)

        # Generate PDF
        return generate_pdf_from_html(tmp_html, output_pdf_path)