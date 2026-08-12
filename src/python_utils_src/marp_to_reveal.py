#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marp to Reveal.js Slide Compiler
Author: Antigravity AI
Description: Compiles Marp-compatible Markdown slide decks into gorgeous, self-contained, 
             interactive HTML presentations utilizing Reveal.js, Outfit/Inter Google Fonts, 
             and Tokyo Night Highlight.js syntax coloring. Works out-of-the-box with no Node.js dependency.
"""

import os
import re
import argparse

def parse_markdown_to_html(md_content):
    """
    Parses basic Markdown features commonly used in slide decks into standard HTML blocks.
    Protects code blocks from being corrupted by inline formatting rules.
    """
    code_blocks = []
    
    # 1. Protect and format multi-line code blocks first
    def protect_code_block(match):
        lang = match.group(1) or 'plaintext'
        code = match.group(2)
        # Escape HTML entities inside the code block to prevent browser DOM parsing issues
        code_escaped = code.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        html_block = f'<pre><code class="language-{lang}">{code_escaped}</code></pre>'
        placeholder = f'<!-- CODEBLOCK{len(code_blocks)} -->'
        code_blocks.append(html_block)
        return placeholder
    
    md_content = re.sub(r'```(\w*)\n(.*?)\n```', protect_code_block, md_content, flags=re.DOTALL)
    
    # 2. Headings (H1 to H4)
    md_content = re.sub(r'^#\s+(.+)$', r'<h1>\1</h1>', md_content, flags=re.MULTILINE)
    md_content = re.sub(r'^##\s+(.+)$', r'<h2>\1</h2>', md_content, flags=re.MULTILINE)
    md_content = re.sub(r'^###\s+(.+)$', r'<h3>\1</h3>', md_content, flags=re.MULTILINE)
    md_content = re.sub(r'^####\s+(.+)$', r'<h4>\1</h4>', md_content, flags=re.MULTILINE)
    
    # 3. Nested Lists Parser (Supports both ul and ol)
    lines = md_content.split('\n')
    new_lines = []
    indent_stack = [] # holds tuples of (indentation_level, list_type)
    
    for line in lines:
        match = re.match(r'^(\s*)(?:([\-\*])|(\d+\.))\s+(.+)$', line)
        if match:
            indent = len(match.group(1))
            list_type = 'ul' if match.group(2) else 'ol'
            item_text = match.group(4)
            
            if not indent_stack:
                new_lines.append(f'<{list_type}>')
                indent_stack.append((indent, list_type))
                new_lines.append(f'<li>{item_text}')
            elif indent > indent_stack[-1][0]:
                new_lines.append(f'<{list_type}>')
                indent_stack.append((indent, list_type))
                new_lines.append(f'<li>{item_text}')
            elif indent < indent_stack[-1][0]:
                while indent_stack and indent < indent_stack[-1][0]:
                    new_lines.append('</li>')
                    new_lines.append(f'</{indent_stack[-1][1]}>')
                    indent_stack.pop()
                if not indent_stack or indent > indent_stack[-1][0]:
                    new_lines.append(f'<{list_type}>')
                    indent_stack.append((indent, list_type))
                else:
                    new_lines.append('</li>')
                    if list_type != indent_stack[-1][1]:
                        new_lines.append(f'</{indent_stack[-1][1]}>')
                        new_lines.append(f'<{list_type}>')
                        indent_stack[-1] = (indent, list_type)
                new_lines.append(f'<li>{item_text}')
            else:
                new_lines.append('</li>')
                if list_type != indent_stack[-1][1]:
                    new_lines.append(f'</{indent_stack[-1][1]}>')
                    new_lines.append(f'<{list_type}>')
                    indent_stack[-1] = (indent, list_type)
                new_lines.append(f'<li>{item_text}')
        else:
            if indent_stack:
                while indent_stack:
                    new_lines.append('</li>')
                    new_lines.append(f'</{indent_stack[-1][1]}>')
                    indent_stack.pop()
            new_lines.append(line)
            
    if indent_stack:
        while indent_stack:
            new_lines.append('</li>')
            new_lines.append(f'</{indent_stack[-1][1]}>')
            indent_stack.pop()
            
    md_content = '\n'.join(new_lines)
    
    # 4. Inline formatting (bold, italic, code) - safe now
    md_content = re.sub(r'\*\*(.+?)\*\*|__(.+?)__', r'<strong>\1\2</strong>', md_content)
    md_content = re.sub(r'\*(.+?)\*|_(.+?)_', r'<em>\1\2</em>', md_content)
    
    def escape_inline_code(match):
        code_text = match.group(1)
        code_escaped = code_text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        return f'<code>{code_escaped}</code>'
        
    md_content = re.sub(r'`([^`\n]+)`', escape_inline_code, md_content)
    
    # 5. Restore protected code blocks
    for idx, html_block in enumerate(code_blocks):
        placeholder = f'<!-- CODEBLOCK{idx} -->'
        md_content = md_content.replace(placeholder, html_block)
        
    return md_content

def compile_marp_to_reveal(input_path, output_path):
    """
    Reads the input Marp markdown file, extracts YAML frontmatter/custom styles, 
    splits the content into slides, parses HTML, and saves the final HTML Reveal.js file.
    """
    if not os.path.exists(input_path):
        print(f"Error: El archivo de entrada '{input_path}' no existe.")
        return False
        
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Extract YAML frontmatter if present
    yaml_match = re.match(r'^---\n(.*?)\n---\n', content, flags=re.DOTALL)
    
    style_content = ""
    slide_title = "Presentación"
    if yaml_match:
        frontmatter = yaml_match.group(1)
        # Search for custom CSS style blocks: style: | ...
        style_match = re.search(r'style:\s*\|\n((?:\s{2,}.*\n?)+)', frontmatter)
        if style_match:
            raw_style = style_match.group(1)
            # Dedent the style block
            style_lines = raw_style.split('\n')
            non_empty_lines = [l for l in style_lines if l.strip()]
            if non_empty_lines:
                indent = len(non_empty_lines[0]) - len(non_empty_lines[0].lstrip())
                style_content = '\n'.join([l[indent:] if len(l) >= indent else l for l in style_lines])
        
        # Search for custom title property: title: ...
        title_match = re.search(r'^title:\s*(.+)$', frontmatter, flags=re.MULTILINE)
        if title_match:
            slide_title = title_match.group(1).strip().strip('"').strip("'")
            
        # Strip frontmatter from slides content
        slides_raw = content[yaml_match.end():]
    else:
        slides_raw = content
        
    # Split slides using the markdown page-break delimiter '---'
    slides_list = re.split(r'\n---\n', slides_raw)
    
    reveal_slides_html = ""
    for idx, slide_raw in enumerate(slides_list):
        slide_raw = slide_raw.strip()
        if not slide_raw:
            continue
            
        # Parse custom Marp slide directives/headers
        is_lead = False
        lines = slide_raw.split('\n')
        filtered_lines = []
        for line in lines:
            trimmed = line.strip()
            # Check for centered lead class directive
            if re.match(r'^(?:_class|class)\s*:\s*lead\s*$', trimmed):
                is_lead = True
            # Ignore marp footer declarations within individual slides (we handle it globally)
            elif trimmed.startswith('footer:'):
                pass
            else:
                filtered_lines.append(line)
        
        slide_body = '\n'.join(filtered_lines)
        slide_html = parse_markdown_to_html(slide_body)
        
        # Inject sections
        section_class = 'class="lead-slide"' if is_lead else ''
        reveal_slides_html += f'            <section {section_class}>\n{slide_html}\n            </section>\n\n'
        
    # Core Reveal.js HTML Template
    html_output = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <title>{slide_title} - Desarrollo de Software IV</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

    <!-- Reveal.js Base Stylesheets -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/reset.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/reveal.min.css">
    
    <!-- Tokyo Night Dark Theme for Code Syntax Resaltation -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/styles/tokyo-night-dark.min.css">

    <!-- Premium Google Typography -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800;900&family=Fira+Code:wght@400;500;600&display=swap" rel="stylesheet">

    <style>
        /* Modern Web Design Aesthetics & Layout Tokens */
        .reveal {{
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #0b0f19 0%, #111827 50%, #1e1b4b 100%);
            color: #f8fafc;
        }}
        
        .reveal .slides section {{
            font-family: 'Outfit', 'Inter', sans-serif;
            text-align: left;
            padding: 50px 70px;
            box-sizing: border-box;
            font-size: 22px;
        }}
        
        /* Centered Cover Slide Layout */
        .reveal .slides section.lead-slide {{
            text-align: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100%;
        }}
        
        /* Premium Typography Styles */
        .reveal h1, .reveal h2, .reveal h3, .reveal h4, .reveal h5, .reveal h6 {{
            font-family: 'Outfit', sans-serif;
            text-transform: none;
            color: #38bdf8;
            font-weight: 800;
            text-shadow: none;
        }}
        
        .reveal h1 {{
            font-size: 1.7em;
            margin-bottom: 12px;
            border-bottom: 2px solid #3b82f6;
            padding-bottom: 10px;
        }}
        
        .reveal .lead-slide h1 {{
            border-bottom: none;
            font-size: 2.5em;
            margin-bottom: 15px;
            color: #38bdf8;
        }}
        
        .reveal h2 {{
            font-size: 1.25em;
            color: #818cf8;
            font-weight: 700;
            margin-top: 0px;
        }}
        
        .reveal .lead-slide h2 {{
            font-size: 1.55em;
            color: #818cf8;
            margin-bottom: 30px;
        }}
        
        .reveal h3 {{
            font-size: 1.1em;
            color: #a78bfa;
        }}
        
        /* List and Text Formatting */
        .reveal p, .reveal li {{
            color: #cbd5e1;
            line-height: 1.6;
        }}
        
        .reveal ul {{
            list-style-type: square;
            margin-left: 1.5em;
        }}
        
        .reveal li {{
            margin-bottom: 12px;
        }}
        
        .reveal strong {{
            color: #f43f5e;
            font-weight: 600;
        }}
        
        .reveal em {{
            color: #fb7185;
            font-style: italic;
        }}
        
        .reveal footer {{
            font-size: 0.5em;
            color: #6b7280;
            position: absolute;
            bottom: 20px;
            right: 50px;
        }}
        
        /* Code Block Containers and Inlines */
        .reveal code {{
            font-family: 'Fira Code', monospace;
            background-color: #030712;
            color: #38bdf8;
            border-radius: 4px;
            padding: 2px 8px;
            font-size: 0.85em;
        }}
        
        .reveal pre {{
            background-color: #030712 !important;
            border: 1px solid #1f2937;
            border-radius: 10px;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.4);
            width: 100%;
            margin: 20px 0;
            box-sizing: border-box;
        }}
        
        .reveal pre code {{
            background-color: transparent;
            color: inherit;
            font-size: 0.8em;
            line-height: 1.55;
            padding: 18px;
            max-height: 520px;
        }}
        
        /* Control Nav Arrows & Progress Bar */
        .reveal .controls-arrow {{
            color: #38bdf8 !important;
        }}
        
        .reveal .progress span {{
            background-color: #38bdf8 !important;
        }}

        /* Custom style overrides parsed from Marp frontmatter */
        {style_content}
    </style>
</head>
<body>
    <div class="reveal">
        <div class="slides">
{reveal_slides_html}        </div>
    </div>

    <!-- Highlight.js and Reveal.js Libraries -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/highlight.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/reveal.js"></script>

    <script>
        // Initialize Highlight.js for code syntax coloring
        hljs.highlightAll();

        // Initialize Reveal.js with modern layout configurations
        Reveal.initialize({{
            hash: true,
            respondToHashChanges: true,
            history: true,
            transition: 'slide', // none/fade/slide/convex/concave/zoom
            transitionSpeed: 'default',
            backgroundTransition: 'fade',
            width: 960,
            height: 700,
            margin: 0.05,
            minScale: 0.2,
            maxScale: 2.0,
            plugins: []
        }});
    </script>
</body>
</html>
"""
    
    # Save the output HTML file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_output)
    
    print(f"Éxito: Presentación compilada correctamente en '{output_path}'.")
    return True

def main():
    parser = argparse.ArgumentParser(description="Compilador ligero de Marp Markdown a HTML Reveal.js")
    parser.add_argument("input", help="Ruta al archivo Markdown de entrada con la sintaxis de diapositivas.")
    parser.add_argument("-o", "--output", help="Ruta de salida para el archivo HTML. Por defecto usa el mismo nombre del archivo de entrada.")
    
    args = parser.parse_args()
    
    input_file = args.input
    output_file = args.output
    
    if not output_file:
        base, _ = os.path.splitext(input_file)
        output_file = base + ".html"
        
    compile_marp_to_reveal(input_file, output_file)

if __name__ == "__main__":
    main()
