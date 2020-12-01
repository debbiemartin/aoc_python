#!/usr/bin/python3

import itertools
from functools import reduce

def find_number_prod(count):
    for numvars in itertools.permutations(numbers, count):
        if sum(numvars) == 2020:
            return reduce((lambda x, y: x * y), numvars)

with open("1/input.txt", 'r') as f:
    lines = f.readlines()

numbers = [int(line.strip("\n")) for line in lines]

print("PART 1:")
print(f"found soln for 2 numbers: {find_number_prod(2)}")

print("PART 2:")
print(f"found soln for 3 numbers: {find_number_prod(3)}")
