#!/usr/bin/python3
import sys
if __name__ == "__main__":
    no_of_elements = len(sys.argv) - 1
    if no_of_elements == 0:
        print("{} arguments.".format(no_of_elements))
    elif no_of_elements == 1:
        print("{} argument:".format(no_of_elements))
    else:
        print("{} arguments:".format(no_of_elements))
    for i in (range(1, no_of_elements + 1)):
        print("{}: {}".format(i, sys.argv[i]))
