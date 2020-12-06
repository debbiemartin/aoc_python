#!/usr/bin/python3

from functools import reduce

def find_total(reduce_fn):
    """
    Find total qualifying fields over all groups in filetxt. 
       reduce_fn - Used to reduce the list of strings for each group.
    """
    lettersets = [reduce(reduce_fn, group.split("\n")) for group in filetxt.split("\n\n")]
    return sum(len(l) for l in lettersets)

with open("6/input.txt", "r") as f:
    # read into a string var - will split on blank lines easier than with list
    filetxt = f.read()

print("PART 1:")
print(find_total(lambda a, b: set(a) | set(b)))

print("PART 2:")
print(find_total(lambda a, b: set(a) & set(b)))