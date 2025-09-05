import os
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path_for_file = os.path.join(dest_dir_path, filename)
        
        if os.path.isfile(from_path):
            if from_path.endswith(".md"):
                dest_dir_path = os.path.dirname(dest_path_for_file)
                if dest_dir_path != "":
                    os.makedirs(dest_dir_path, exist_ok=True)
                dest_path_for_file = dest_path_for_file.replace(".md", ".html")
                generate_page(from_path, template_path, dest_path_for_file)
        
        elif os.path.isdir(from_path):
            generate_pages_recursive(from_path, template_path, dest_path_for_file)

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating pages recursively...")
    generate_pages_recursive(
        dir_path_content,
        template_path,
        dir_path_public
    )

if __name__ == "__main__":
    main()
