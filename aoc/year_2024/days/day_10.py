from ... import utils


class Day(object):
    def __init__(self, parser):
        self.parser = parser
        self.trails = 0
        self.ends = 0

    def step(self, coord, ends, search=1):
        for increment in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            neighbour = utils.add_coord(coord, increment)
            if self.grid.get(neighbour) == search:
                if search == 9:
                    self.trails += 1
                    if neighbour not in ends:
                        ends.add(neighbour)
                        self.ends += 1
                    continue

                self.step(neighbour, ends, search+1)

    def calculate(self):
        self.grid = {
            (x, y): int(char)
            for y, line in enumerate(self.parser.get_lines())
            for x, char in enumerate(line.strip())
            if char != "."
        }

        for (x, y), char in self.grid.items():
            if char == 0:
                self.step((x, y), set(), search=1)

    def part_1(self):
        return self.ends

    def part_2(self):
        return self.trails
