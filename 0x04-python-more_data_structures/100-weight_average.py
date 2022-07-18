#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        acc = 0
        var = 0
        for x in my_list:
            acc += x[0] * x[1]
            var += x[1]
        return (acc / var)
    return 0
