import os
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    header = False
    for line in markdown:
        if line.startswith('#'):
            return line.lstrip("#").strip()
    
    raise Exception("No header")

def generator_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path) as f:
        markdown_text = f.read()
    
    with open(template_path) as f:
        html_text = f.read()
        
    
    processed_markdown = markdown_text.splitlines()
    title = extract_title(processed_markdown)
    html_node = markdown_to_html_node(markdown_text)
    final_html = html_node.to_html()

    page_html = html_text.replace("{{ Title }}", title)
    page_html = page_html.replace("{{ Content }}", final_html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    
    with open(dest_path, "w") as f:
        f.write(page_html)
        
    print("Page generated")