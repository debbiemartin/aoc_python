#!/usr/bin/python3

from . import utils
import itertools
from functools import reduce

def find_number_prod(count, numbers):
    for numvars in itertools.permutations(numbers, count):
        if sum(numvars) == 2020:
            return reduce((lambda x, y: x * y), numvars)
            
def main():
    lines = utils.get_lines(1)
    numbers = list(map(lambda x: int(x), lines))
    
    print("PART 1:")
    print(find_number_prod(2, numbers))
    
    print("PART 2:")
    print(find_number_prod(3, numbers))   