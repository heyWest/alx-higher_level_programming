#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        for i in range(x):
            temp = my_list[i]
            counter += 1
        return counter
    except:
        return counter
