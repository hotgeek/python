import sys


def main(argc, argv):
    if argc != 2:
        print("USage Error: %s path_name" % argv[1])
        sys.exit(-1)

    with open(argv[1], "r") as f_handle:
        for line in f_handle:
            print(line, end='')

main(len(sys.argv), sys.argv)