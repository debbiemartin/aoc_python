from collections import deque
from .. import utils

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
        self.rocks = set()
        lines = self.parser.get_lines()
        assert len(lines) == len(lines[0])
        self.max = len(lines)

        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char == "#":
                    self.rocks.add((x,y))
                if char == "S":
                    self.start = (x,y)

        assert self.start[0] == self.max // 2
        assert self.start[1] == self.max // 2

    def next_coords(self, coord):
        for direction in [(0,1), (1,0), (0,-1), (-1,0)]:
            ncoord = utils.add_coord(coord, direction)
            if ncoord in self.rocks:
                continue
            if ncoord[0] < 0 or ncoord[0] >= self.max or ncoord[1] < 0 or ncoord[1] >= self.max:
                continue
            yield ncoord

    def fill(self, start, steps):
        final = set()
        seen = set([start])
        queue = deque([(start, steps)])

        while queue:
            coord, n_steps = queue.popleft()

            if n_steps % 2 == 0:
                final.add(coord)
            if n_steps == 0:
                continue

            for next_coord in self.next_coords(coord):
                if not next_coord in seen:
                    seen.add(next_coord)
                    queue.append((next_coord, n_steps-1))

        return len(final)

    def part_1(self):
        return self.fill(self.start, 64)

    def part_2(self):
        steps = 26501365
        assert steps % self.max == self.max // 2

        max_inf = steps // self.max - 1

        odd_points = self.fill(self.start, self.max * 2 + 1)
        even_points = self.fill(self.start, self.max * 2)

        corners = (self.fill(c, self.max-1) for c in ((self.start[0], 0), (self.start[0], self.max-1), (0, self.start[1]), (self.max-1, self.start[1])))

        smalls = (self.fill(c, self.max // 2 - 1) for c in ((0, 0), (0, self.max-1), (self.max-1, 0), (self.max-1, self.max-1)))
        larges = (self.fill(c, self.max * 3 // 2 - 1) for c in ((0, 0), (0, self.max-1), (self.max-1, 0), (self.max-1, self.max-1)))

        answer = (
            ((max_inf // 2 * 2 + 1) ** 2) * odd_points +
            (((max_inf + 1) // 2 * 2) ** 2) * even_points +
            sum(corners) +
            (max_inf + 1) * sum(smalls) +
            (max_inf) * sum(larges)
        )

        return answer
