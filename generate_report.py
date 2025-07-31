import markdown
import pdfkit
from datetime import datetime
import os

def read_technical_doc():
    """Read the technical documentation file."""
    with open('TECHNICAL_DOCUMENTATION.md', 'r', encoding='utf-8') as file:
        return file.read()

def generate_html_report(md_content):
    """Convert markdown content to HTML."""
    html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])
    
    # Add custom styling
    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Telco Churn Predictor - Technical Report</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 40px;
                color: #333;
            }}
            h1, h2, h3 {{
                color: #2c3e50;
            }}
            code {{
                background-color: #f8f9fa;
                padding: 2px 4px;
                border-radius: 4px;
                font-family: 'Courier New', monospace;
            }}
            pre {{
                background-color: #f8f9fa;
                padding: 15px;
                border-radius: 5px;
                overflow-x: auto;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 20px 0;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #f2f2f2;
            }}
            .generated-date {{
                color: #666;
                font-style: italic;
                margin-bottom: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="generated-date">Report generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>
        {html_content}
    </body>
    </html>
    """
    return styled_html

def save_report(html_content, output_format='html'):
    """Save the report in the specified format."""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    if output_format == 'html':
        output_file = f'report_{timestamp}.html'
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(html_content)
    elif output_format == 'pdf':
        output_file = f'report_{timestamp}.pdf'
        pdfkit.from_string(html_content, output_file)
    
    return output_file

def main():
    # Read the technical documentation
    md_content = read_technical_doc()
    
    # Generate HTML report
    html_content = generate_html_report(md_content)
    
    # Save as HTML
    html_file = save_report(html_content, 'html')
    print(f"HTML report generated: {html_file}")
    
    # Try to save as PDF if wkhtmltopdf is installed
    try:
        pdf_file = save_report(html_content, 'pdf')
        print(f"PDF report generated: {pdf_file}")
    except Exception as e:
        print("PDF generation failed. Make sure wkhtmltopdf is installed.")
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 