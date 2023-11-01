#!/usr/bin/python3
for c in range(ord('a'), ord('z') + 1):
    if (c == 'e') or (c == 'q'):
        continue
    print("{}".format(chr(c)),  end='')
