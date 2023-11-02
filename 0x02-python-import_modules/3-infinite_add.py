#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = []
    arg = sys.argv
    leng = len(arg)
    i = 1
    sum = 0
    while (i < leng):
        sum += int(arg[i])
        i += 1
    print("{}".format(sum), end="\n")
