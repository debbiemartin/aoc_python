from collections import defaultdict
from ... import utils

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
        lines = self.parser.get_lines()
        self.space = set()
        self.walls = set()

        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char == "E":
                    self.end = (x, y)
                    self.space.add(self.end)
                elif char == "S":
                    self.start = (x, y)
                elif char == ".":
                    self.space.add((x, y))
                elif char == "#":
                    self.walls.add((x, y))

        self.path = {self.start: 0}
        coord = self.start

        ds = [d for d in directions if utils.add_coord(
            coord, d) in self.space]
        assert (len(ds) == 1)
        d = ds[0]

        while True:
            for next_d in (next_d for next_d in directions if not next_d == (-1*d[0], -1*d[1])):
                next_coord = utils.add_coord(coord, next_d)
                if next_coord in self.space:
                    self.path[next_coord] = self.path[coord] + 1
                    if next_coord == self.end:
                        return
                    coord = next_coord
                    d = next_d
                    break
            else:
                assert False

    def part_1(self):
        self.cheats = defaultdict(lambda: 0)

        for coord, dist in self.path.items():
            for d in directions:
                two_d = (2*d[0], 2*d[1])
                if utils.add_coord(coord, d) in self.walls and utils.add_coord(coord, two_d) in self.space:
                    jump_dist = self.path.get(utils.add_coord(coord, two_d))
                    if jump_dist and jump_dist > dist+2:
                        self.cheats[jump_dist-dist-2] += 1

        return sum(val for item, val in self.cheats.items() if item >= 100)

    def part_2(self):
        self.cheats = defaultdict(lambda: 0)

        for coord, dist in self.path.items():
            for jump_coord, jump_dist in self.path.items():
                diff = abs(jump_coord[0]-coord[0])+abs(jump_coord[1]-coord[1])
                if diff <= 20 and jump_dist > dist+diff:
                    self.cheats[jump_dist-dist-diff] += 1

        return sum(val for item, val in self.cheats.items() if item >= 100)
