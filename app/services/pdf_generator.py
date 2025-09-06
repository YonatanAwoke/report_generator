# app/services/pdf_generator.py
from weasyprint import HTML

def generate_pdf_from_html(html_path, output_pdf_path):
    HTML(html_path).write_pdf(output_pdf_path)
    return output_pdf_path
