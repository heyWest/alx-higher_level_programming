#!/usr/bin/python3
if __name == "__main__":
    import sys
    var = len(sys.argv) - 1

    if var == 0:
        print("{} arguments:".format(var))
    elif var == 1:
        print("{} argument:".format(var))
    else:
        print("{} arguments:".format(var))
    if var >= 1:
        var = 0
        for arg in sys.argv:
            if var != 0:
                print("{}: {}".format(var, arg))
            var += 1
