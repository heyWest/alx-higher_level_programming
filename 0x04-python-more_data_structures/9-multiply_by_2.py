#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return a_dictionary.update((key, val*2) for key, val in a_dictionary.items())
