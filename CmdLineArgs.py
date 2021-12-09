import sys

def perform_copy(src_file, dest_file):
    f_src = None
    f_dest = None

    try:
        f_src = open(src_file, "r")
    except FileNotFoundError:
        print("Error: Source File Not found!!")
        return False
    except PermissionError:
        print("Permission denied to open source file in read mode")
        return False
    except:
        print("Exception occured--- f_src")
        return False

    try:
        f_dest = open(dest_file, "w")
    except PermissionError:
        return False
    except:
        print("Exception occured--- f_dest")
        return False

    for line in f_src:
        print(line, file=f_dest, end='')

    f_src.close()
    f_dest.close()

    return True

def main(argc, argv):

    if argc != 3:
        print("Usage Error: Correct Usage: ", argv[0],"source_file_path destination_file_path")
        sys.exit(-1)
    
    ret = perform_copy(argv[1], argv[2])
    if ret==True:
        print("1 File(s) Copied")
    else:
        print("Error: Copying source file to destination file")

    sys.exit(0)

main(len(sys.argv), sys.argv)