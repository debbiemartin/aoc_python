import itertools

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def shortest_path(self, g1, g2):
        unexpanded_path = (abs(g1[0]-g2[0]) + abs(g1[1]-g2[1]))
        cols = sum(1 for c in self.empty_cols if g1[1] < c < g2[1] or g2[1] < c < g1[1])
        rows = sum(1 for r in self.empty_rows if g1[0] < r < g2[0] or g2[0] < r < g1[0])
        return unexpanded_path + (self.factor-1) * cols + (self.factor-1) * rows

    def calculate(self):
        lines = self.parser.get_lines()
        self.galaxies = list((x, y) for y, line in enumerate(lines) for x, char in enumerate(line) if char == "#")
        self.empty_rows = set(row for row in range(len(lines)) if not any(row == x for (x,y) in self.galaxies))
        self.empty_cols = set(col for col in range(len(lines[0])) if not any(col == y for (x,y) in self.galaxies))

    def sum_paths(self):
        return sum(
            self.shortest_path(g1, g2)
            for g1, g2 in [
                (a, b) for idx, a in enumerate(self.galaxies) for b in self.galaxies[idx + 1:]
            ]
        )

    def part_1(self):
        self.factor = 2
        return self.sum_paths()

    def part_2(self):
        self.factor = 1000000
        return self.sum_paths()
