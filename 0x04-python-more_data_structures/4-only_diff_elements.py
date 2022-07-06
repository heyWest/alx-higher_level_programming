#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if len(set_1) > len(set_2):
        final = list(filter(lambda x: x not in set_2, set_1))
    else:
        final = list(filter(lambda x: x not in set_1, set_2))
    return final
