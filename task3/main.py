import sys
from print_dir_structure import print_dir_structure

def main():
    if len(sys.argv) < 2:
        print("Missing command line argument with directory path!")
        return

    print_dir_structure(sys.argv[1])


if __name__ == '__main__':
    main()