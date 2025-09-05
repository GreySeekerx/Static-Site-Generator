import os
import shutil
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    for line in markdown:
        if line.startswith('#'):
            return line.lstrip("#").strip()
    
    raise Exception("No header")

def generate_page(from_path, template_path, dest_path, basepath):
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

    # Replace hardcoded absolute paths with the configurable basepath
    page_html = page_html.replace('href="/', f'href="{basepath}')
    page_html = page_html.replace('src="/', f'src="{basepath}')


    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    
    with open(dest_path, "w") as f:
        f.write(page_html)
        
    print("Page generated successfully!")


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path_for_file = os.path.join(dest_dir_path, filename)
        
        if os.path.isfile(from_path):
            if from_path.endswith(".md"):
                dest_path_for_file = dest_path_for_file.replace(".md", ".html")
                generate_page(from_path, template_path, dest_path_for_file, basepath)
        
        elif os.path.isdir(from_path):
            generate_pages_recursive(from_path, template_path, dest_path_for_file, basepath)
