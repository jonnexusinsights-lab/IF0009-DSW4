#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Markdown to PDF Converter
Author: Antigravity AI
Description: Compiles standard Markdown documents into beautiful, print-ready PDF files.
             Features automatic dependency resolution, customizable themes, elegant headers/footers,
             and proper page numbering out-of-the-box. Pure Python-based, no external system binaries required.
"""

import os
import sys
import subprocess
import argparse

# --- AUTOMATIC DEPENDENCY CHECK & RESOLUTION ---
def resolve_dependencies():
    """
    Checks if required libraries are installed. If not, attempts to install them via pip.
    """
    required_packages = {
        "markdown": "markdown",
        "xhtml2pdf": "xhtml2pdf"
    }
    
    missing_packages = []
    for module_name, pip_name in required_packages.items():
        try:
            __import__(module_name)
        except ImportError:
            missing_packages.append(pip_name)
            
    if missing_packages:
        print("Advertencia: Faltan dependencias críticas de Python para realizar la conversión.")
        print(f"Instalando paquetes faltantes automáticamente: {', '.join(missing_packages)}...")
        try:
            subprocess.run(
                [sys.executable, "-m", "pip", "install", *missing_packages],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE
            )
            print("¡Instalación de dependencias completada con éxito!\n")
        except subprocess.CalledProcessError as e:
            print(f"Error al instalar las dependencias automáticamente: {e.stderr.decode().strip()}", file=sys.stderr)
            print("Por favor, instale las dependencias manualmente ejecutando: pip install markdown xhtml2pdf", file=sys.stderr)
            sys.exit(1)

# Run dependency check before importing packages
resolve_dependencies()

# Now it is safe to import markdown and xhtml2pdf
import markdown
from xhtml2pdf import pisa

# --- THEMES & CSS STYLING ---
THEMES = {
    "modern": """
        @page {
            size: letter;
            margin: 2.5cm;
            @frame footer {
                -pdf-frame-content: footer_content;
                bottom: 1.2cm;
                margin-left: 2.5cm;
                margin-right: 2.5cm;
                height: 1cm;
            }
        }
        body {
            font-family: Helvetica, Arial, sans-serif;
            color: #1e293b;
            font-size: 10.5pt;
            line-height: 1.6;
        }
        h1 {
            font-size: 24pt;
            color: #0f172a;
            margin-top: 0;
            margin-bottom: 12pt;
            border-bottom: 2px solid #3b82f6;
            padding-bottom: 6pt;
        }
        h2 {
            font-size: 16pt;
            color: #1e293b;
            margin-top: 22pt;
            margin-bottom: 10pt;
            border-bottom: 1px solid #e2e8f0;
            padding-bottom: 4pt;
        }
        h3 {
            font-size: 13pt;
            color: #2563eb;
            margin-top: 16pt;
            margin-bottom: 8pt;
        }
        h4 {
            font-size: 11pt;
            color: #475569;
            margin-top: 12pt;
            margin-bottom: 6pt;
        }
        p {
            margin-bottom: 10pt;
            text-align: justify;
        }
        ul, ol {
            margin-bottom: 12pt;
            padding-left: 20pt;
        }
        li {
            margin-bottom: 5pt;
        }
        code {
            font-family: Courier, monospace;
            font-size: 9pt;
            background-color: #f1f5f9;
            color: #0f172a;
            padding: 1px 3px;
        }
        pre {
            font-family: Courier, monospace;
            font-size: 8.5pt;
            background-color: #f8fafc;
            border: 1px solid #cbd5e1;
            padding: 8pt;
            margin-bottom: 14pt;
        }
        blockquote {
            border-left: 4px solid #2563eb;
            padding-left: 10pt;
            margin-left: 0;
            color: #475569;
            background-color: #eff6ff;
            margin-bottom: 14pt;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 15pt;
        }
        th {
            background-color: #f1f5f9;
            font-weight: bold;
            border: 1px solid #cbd5e1;
            padding: 6pt;
            text-align: left;
        }
        td {
            border: 1px solid #e2e8f0;
            padding: 6pt;
        }
        hr {
            border: 0;
            border-top: 1px solid #cbd5e1;
            margin: 20pt 0;
        }
    """,
    "academic": """
        @page {
            size: letter;
            margin: 1in;
            @frame footer {
                -pdf-frame-content: footer_content;
                bottom: 0.5in;
                margin-left: 1in;
                margin-right: 1in;
                height: 0.5in;
            }
        }
        body {
            font-family: Times, "Times New Roman", serif;
            color: #000000;
            font-size: 11pt;
            line-height: 1.5;
        }
        h1 {
            font-size: 20pt;
            color: #000000;
            margin-top: 0;
            margin-bottom: 12pt;
            text-align: center;
            font-weight: bold;
        }
        h2 {
            font-size: 14pt;
            color: #000000;
            margin-top: 20pt;
            margin-bottom: 8pt;
            font-weight: bold;
        }
        h3 {
            font-size: 12pt;
            color: #000000;
            margin-top: 16pt;
            margin-bottom: 6pt;
            font-style: italic;
            font-weight: bold;
        }
        p {
            margin-bottom: 10pt;
            text-align: justify;
            text-indent: 0.25in;
        }
        ul, ol {
            margin-bottom: 10pt;
            padding-left: 25pt;
        }
        li {
            margin-bottom: 4pt;
        }
        code {
            font-family: Courier, monospace;
            font-size: 9.5pt;
            background-color: #f5f5f5;
        }
        pre {
            font-family: Courier, monospace;
            font-size: 9pt;
            background-color: #fafafa;
            border: 0.5px solid #999999;
            padding: 8pt;
            margin-bottom: 12pt;
        }
        blockquote {
            border-left: 2px solid #000000;
            padding-left: 12pt;
            margin-left: 20pt;
            margin-right: 20pt;
            color: #333333;
            margin-bottom: 12pt;
            font-style: italic;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 15pt;
        }
        th {
            border-top: 1.5px solid #000000;
            border-bottom: 1.5px solid #000000;
            font-weight: bold;
            padding: 5pt;
            text-align: left;
        }
        td {
            border-bottom: 0.5px solid #cccccc;
            padding: 5pt;
        }
        hr {
            border: 0;
            border-top: 0.5px solid #000000;
            margin: 15pt 0;
        }
    """
}

def convert_md_to_pdf(input_path, output_path, theme="modern", course_title="IF0009 - Desarrollo de Software IV"):
    """
    Converts a Markdown file into a formatted PDF using markdown and xhtml2pdf.
    """
    if not os.path.exists(input_path):
        print(f"Error: El archivo de entrada '{input_path}' no existe.", file=sys.stderr)
        sys.exit(1)

    # Read markdown content
    with open(input_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    # Convert Markdown to HTML with standard extensions for tables and code formatting
    html_body = markdown.markdown(
        md_text, 
        extensions=['extra', 'codehilite', 'toc', 'fenced_code']
    )

    # Obtain theme stylesheet
    css_style = THEMES.get(theme, THEMES["modern"])

    # Build full self-contained HTML document
    full_html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <style>
            {css_style}
        </style>
    </head>
    <body>
        <!-- Header / Footer Frame Content for xhtml2pdf pisa -->
        <div id="footer_content">
            <table style="width: 100%; border: none; font-size: 8.5pt; color: #64748b; font-family: Helvetica, Arial, sans-serif;">
                <tr>
                    <td style="border: none; text-align: left; padding: 0;">{course_title}</td>
                    <td style="border: none; text-align: right; padding: 0;">Página <pdf:pagenumber /> de <pdf:pagecount /></td>
                </tr>
            </table>
        </div>

        <!-- Rendered Markdown Body -->
        <div class="content">
            {html_body}
        </div>
    </body>
    </html>
    """

    # Open output PDF file in binary write mode
    with open(output_path, "w+b") as pdf_file:
        pisa_status = pisa.CreatePDF(full_html, dest=pdf_file)
        
    if not pisa_status.err:
        print(f"Éxito: Se ha generado el archivo PDF correctamente.")
        print(f" PDF: {os.path.abspath(output_path)}")
    else:
        print("Error: Ocurrió un fallo en el motor pisa al generar el PDF.", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="Compila archivos Markdown (.md) en documentos PDF estructurados y con diseño estético."
    )
    parser.add_argument(
        "-i", "--input", 
        required=True, 
        help="Ruta al archivo Markdown (.md) de entrada."
    )
    parser.add_argument(
        "-o", "--output", 
        help="Ruta donde se guardará el PDF resultante. Por defecto usa el mismo nombre del MD."
    )
    parser.add_argument(
        "-t", "--theme", 
        choices=list(THEMES.keys()), 
        default="modern", 
        help="Tema visual y de tipografía a aplicar en el PDF. (Por defecto: modern)"
    )
    parser.add_argument(
        "-c", "--course", 
        default="IF0009 - Desarrollo de Software IV", 
        help="Título o metadata para el pie de página del documento."
    )

    args = parser.parse_args()

    # Determine default output path if not specified
    output_path = args.output
    if not output_path:
        base_name, _ = os.path.splitext(args.input)
        output_path = base_name + ".pdf"

    convert_md_to_pdf(args.input, output_path, args.theme, args.course)

if __name__ == "__main__":
    main()
