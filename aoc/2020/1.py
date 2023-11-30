#!/usr/bin/python3

import itertools
from functools import reduce


class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def _find_number_prod(self, count):
        for numvars in itertools.permutations(self.numbers, count):
            if sum(numvars) == 2020:
                return reduce((lambda x, y: x * y), numvars)

    def calculate(self):
        lines = self.parser.get_lines()
        self.numbers = list(map(lambda x: int(x), lines))

    def part_1(self):
        return self._find_number_prod(2)

    def part_2(self):
        return self._find_number_prod(3)
