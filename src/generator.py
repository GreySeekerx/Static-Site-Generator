

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