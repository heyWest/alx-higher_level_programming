#!/usr/bin/python3
def common_elements(set_1, set_2):
    final = [i if i in set_2 for i in set_1]
    return final
