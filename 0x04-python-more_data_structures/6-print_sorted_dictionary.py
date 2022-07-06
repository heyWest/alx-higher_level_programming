#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = list(a_dictionary.keys()).sort()
    for i in new_dict:
        print("{}: {}".format(i, a_dictionary.get(i)))
