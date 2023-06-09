#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    num_arguments = len(sys.argv) - 1
    if num_arguments == 0:
        print("0 arguments.")
    if num_arguments == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_arguments))
    for arg in range(num_arguments):
        print("{}: {}".format(arg + 1, sys.argv[arg + 1]))
