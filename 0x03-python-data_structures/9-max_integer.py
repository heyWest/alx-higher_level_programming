#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    int max_ = 0
    for i in my_list:
        if i > max_:
            max_ = i
    return max_
