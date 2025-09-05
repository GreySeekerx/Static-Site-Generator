import os
import shutil
import sys
from gencontent import generate_pages_recursive

dir_path_static = "./static"
dir_path_docs = "./docs"
dir_path_content = "./content"
template_path = "./template.html"


def copy_files_recursive(from_dir, to_dir):
    """
    Recursively copies files from a source directory to a destination directory.

    Args:
        from_dir (str): The path to the source directory.
        to_dir (str): The path to the destination directory.
    """
    # Create the destination directory if it doesn't exist
    if not os.path.exists(to_dir):
        os.mkdir(to_dir)

    # Iterate over all items in the source directory
    for item in os.listdir(from_dir):
        from_path = os.path.join(from_dir, item)
        to_path = os.path.join(to_dir, item)

        # If the item is a file, copy it
        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)
        # If the item is a directory, make a recursive call
        elif os.path.isdir(from_path):
            copy_files_recursive(from_path, to_path)


def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    print("Deleting docs directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to docs directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    print("Generating pages recursively...")
    # The import for this function is missing in the original provided file.
    # Make sure to have `from gencontent import generate_pages_recursive` at the top of main.py
    # or define the function in this file.
    generate_pages_recursive(
        dir_path_content,
        template_path,
        dir_path_docs,
        basepath,
    )


if __name__ == "__main__":
    main()
