#!/usr/bin/python3

from .. import utils
from collections import defaultdict

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def count_hops(self):
        counts = defaultdict(lambda: 0)

        # add diff between 0 for charging outlet
        counts[self.adapters[0]] = 1
        # add counts for each of the adapters:
        for i in range(len(self.adapters) - 1):
            counts[self.adapters[i + 1] - self.adapters[i]] += 1
        # add count for device (3 higher than highest adapter)
        counts[3] += 1

        return counts[1] * counts[3]

    @utils.memoize
    def count_paths(self, start):
        if start == self.adapters[-1]:
            # 1 possible hop to device
            return 1

        count = sum(
            self.count_paths(start + hop)
            for hop in range(1, 4)
            if start + hop in self.adapters
        )

        return count

    def calculate(self):
        self.adapters = sorted(map(lambda x: int(x), self.parser.get_lines()))

    def part_1(self):
        return self.count_hops()

    def part_2(self):
        return self.count_paths(0)
