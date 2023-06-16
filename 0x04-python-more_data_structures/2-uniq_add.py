#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (only once for each integer).
    """
    unique_set = set()
    total_sum = 0
    for num in my_list:
        if num not in unique_set:
            total_sum += num
            unique_set.add(num)
    return total_sum
