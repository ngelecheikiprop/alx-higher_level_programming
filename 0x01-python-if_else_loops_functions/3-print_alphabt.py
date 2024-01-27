#!/usr/bin/python3
for i in range(97, 123):
    if (i == ord('q') or i == ord('e')):
        i += 1
        continue
    print("{}".format(chr(i)), end="")
