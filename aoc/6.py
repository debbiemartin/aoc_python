#!/usr/bin/python3

from . import utils
from functools import reduce

def find_total(reduce_fn):
    """
    Find total qualifying fields over all groups in filetxt. 
       reduce_fn - Used to reduce the list of strings for each group.
    """
    lettersets = [reduce(reduce_fn, group.split("\n")) for group in sections]
    return sum(len(l) for l in lettersets)

def main():
    global sections
    sections = utils.get_sections(6)
    
    print("PART 1:")
    print(find_total(lambda a, b: set(a) | set(b)))
    
    print("PART 2:")
    print(find_total(lambda a, b: set(a) & set(b)))