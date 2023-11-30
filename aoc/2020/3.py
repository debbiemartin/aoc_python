#!/usr/bin/python3

from functools import reduce
import math

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def count_trees(self, slope):
        # find the set of y coords up front in case increment != 1:
        coords = list([(i * slope[0], i * slope[1]) for i in range(math.ceil(len(treemap)/slope[1]))])
        treecount = sum(1 for x, y in coords if treemap[y][x % len(treemap[y])])
        return treecount

    def calculate(self):
        lines = self.parser.get_lines()

        # tree map is 2 d list i.e. treemap[y][x] == treepresentbool
        global treemap
        treemap = [list(map(lambda x: x == "#", line.strip("\n"))) for line in lines]

    def part_1(self):
        return self.count_trees((3, 1))

    def part_2(self):
        # tuple of (right, down) increments
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        return reduce((lambda x, y: x * y), [self.count_trees(slope) for slope in slopes])
