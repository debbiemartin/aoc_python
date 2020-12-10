#!/usr/bin/python3

from . import utils
from functools import reduce
import math

def count_trees(slope):
    # find the set of y coords up front in case increment != 1:
    coords = list([(i * slope[0], i * slope[1]) for i in range(math.ceil(len(treemap)/slope[1]))])
    treecount = sum(1 for x, y in coords if treemap[y][x % len(treemap[y])])
    return treecount
    
def main():
    lines = utils.get_lines(3)
        
    # tree map is 2 d list i.e. treemap[y][x] == treepresentbool   
    global treemap 
    treemap = [list(map(lambda x: x == "#", line.strip("\n"))) for line in lines]
    
    print("PART 1:")
    print(count_trees((3, 1)))
    
    print("PART 2:")
    # tuple of (right, down) increments
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    print(reduce((lambda x, y: x * y), [count_trees(slope) for slope in slopes]))