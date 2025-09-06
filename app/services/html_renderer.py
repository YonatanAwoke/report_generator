# app/services/html_renderer.py
from jinja2 import Environment, FileSystemLoader

def render_html(report_data, output_html_path):
    env = Environment(loader=FileSystemLoader("app/templates"))
    template = env.get_template("report_template.html")
    html = template.render(**report_data)
    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(html)
    return output_html_path
