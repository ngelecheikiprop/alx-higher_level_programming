#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    arg = dir(hidden_4)
    i = 0
    while (i < len(arg)):
        if (arg[i][:2] == "__"):
            i += 1
            continue
        print("{}".format(arg[i]), end="\n")
        i += 1
