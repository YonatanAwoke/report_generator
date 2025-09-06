
# run.py
import json
from app.agents.report_agent import ReportAgent
import argparse

def main():
    parser = argparse.ArgumentParser(description='Generate a report from a JSON file.')
    parser.add_argument('input_file', help='The path to the input JSON file.')
    parser.add_argument('--output_file', default='output/final_report.pdf', help='The path to the output PDF file.')
    args = parser.parse_args()

    with open(args.input_file, 'r') as f:
        data = json.load(f)

    agent = ReportAgent()
    output_path = agent.create_report(data, args.output_file)
    print(f"Report generated successfully: {output_path}")

if __name__ == '__main__':
    main()
