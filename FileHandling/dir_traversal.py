import os, sys

def dir_traversal(dir_path):
    for file_name in os.listdir(dir_path):        
        if os.path.isdir(os.path.join(dir_path, file_name)):
            print("D -> ", file_name)
            dir_traversal(os.path.join(dir_path, file_name))
        else:
            print("\t F->", file_name)
    
        


def main():
    dir_traversal("C:\\Users\\rborkar\\Python")
    sys.exit(0)

main()
