import shutil, os
from textnode import TextNode, TextType
from generator import generator_page



    
def copy_content(source, destination):
    static_path = os.listdir(source)
    for i in static_path:
        sub_path = os.path.join(source, i)
        sub_path1 = os.path.join(destination, i)
        if os.path.isfile(sub_path):
            shutil.copy(sub_path, sub_path1) 
            print(f"Copied file: {sub_path} to {destination}")
        elif os.path.isdir(sub_path):
            os.makedirs(sub_path1, exist_ok=True)
            copy_content(sub_path, sub_path1)

def generator_pages(dir_path_content, template_path, dest_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path_for_file = os.path.join(dest_path, filename)
        if os.path.isfile(from_path):
            if filename.endswith(".md"):
                dest_path_for_file = dest_path_for_file.replace(".md", ".html")
                generator_page(from_path, template_path, dest_path_for_file)
        elif os.path.isdir(from_path):
            generator_pages(from_path, template_path, dest_path_for_file)  


def main():
    source = "static" 
    destination = "public"
    content_dir = "content"
    template_file = "template.html"
    if os.path.exists(destination): 
        shutil.rmtree(destination)
    os.makedirs(destination)    

    print("Copying static files")
    copy_content(source, destination)
    
    print("\n Generating Markdown pages")
    generator_pages(content_dir, template_file, destination)

if __name__ == "__main__":
    main()