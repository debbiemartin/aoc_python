from collections import defaultdict
import math
from ... import utils


class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
        self.antennas = defaultdict(list)
        lines = [l.strip() for l in self.parser.get_lines()]
        self.xmax = len(lines[0])
        self.ymax = len(lines)
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char == ".":
                    continue
                self.antennas[char].append((x, y))

    def get_antinodes(self, pos_fn):
        antinodes = set()
        for antenna, positions in self.antennas.items():
            # All possible pairs
            for a, b in ((a, b) for idx, a in enumerate(positions) for b in positions[idx + 1:]):
                for pos in pos_fn(a, b):
                    assert (self.in_grid(pos))
                    antinodes.add(pos)
        return antinodes

    def in_grid(self, pos):
        return 0 <= pos[0] < self.xmax and 0 <= pos[1] < self.ymax

    def part_1(self):
        def twice_distance(a, b):
            pos_a = (2*a[0]-b[0], 2*a[1]-b[1])
            if self.in_grid(pos_a):
                yield pos_a

            pos_b = (2*b[0]-a[0], 2*b[1]-a[1])
            if self.in_grid(pos_b):
                yield pos_b

        antinodes = self.get_antinodes(twice_distance)

        return len(antinodes)

    def part_2(self):
        def any_in_line(a, b):
            diff = (a[0]-b[0], a[1]-b[1])
            # simplify into smallest increment
            gcd = math.gcd(diff[0], diff[1])
            diff_plus = (int(diff[0]/gcd), int(diff[1]/gcd))
            diff_minus = (-1*diff_plus[0], -1*diff_plus[1])

            # doesn't matter which point we choose but choose same for +-
            pos = a
            while (self.in_grid(pos)):
                yield pos
                pos = utils.add_coord(pos, diff_plus)

            pos = a
            while (self.in_grid(pos)):
                yield pos
                pos = utils.add_coord(pos, diff_minus)

        antinodes = self.get_antinodes(any_in_line)

        return len(antinodes)
