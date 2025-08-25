import shutil, os
from textnode import TextNode, TextType



    
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
            
def main():
    source = "static" 
    destination = "public"
    if os.path.exists(destination): 
        shutil.rmtree(destination)
    os.makedirs(destination)    

    copy_content(source, destination)

if __name__ == "__main__":
    main()