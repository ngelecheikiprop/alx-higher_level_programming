#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = []
    arg = sys.argv
    leng = len(arg)
    i = 0
    if leng == 1:
        print("{} arguments.".format(leng - 1), end="\n")
    elif leng == 0:
        print("{} argument".format(leng - 1), end="\n")
    else:
        print("{} argument".format(leng - 1), end="\n")
    i = 1
    while (i < leng):
        print("{}: {}".format(i, arg[i]), end="\n")
        i+=1