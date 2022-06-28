#!/usr/bin/python3
def uppercase(s):
    for i in range(len(s)):
        if 97 <= ord(s[i]) <= 122:
            n = 32
        else:
            n = 0
        print("{:c}".format(ord(s[i]) - n), end='')
    print()
