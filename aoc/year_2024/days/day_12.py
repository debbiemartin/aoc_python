from ... import utils


class Region(object):
    def __init__(self):
        self.coords = set()

    def contains(self, coord):
        return coord in self.coords

    def add(self, coord):
        self.coords.add(coord)

    @property
    def perimeter(self):
        p = 0
        for r in self.coords:
            # count neighbours in region
            neighbours = sum(1 for i in ((0, 1), (1, 0), (0, -1),
                             (-1, 0)) if utils.add_coord(r, i) in self.coords)
            p += (4-neighbours)

        return p

    @property
    def area(self):
        return len(self.coords)

    @property
    def sides(self):
        s = 0
        all_incs = [(1, 1), (1, 0), (1, -1), (0, -1),
                    (-1, -1), (-1, 0), (-1, 1), (0, 1)]

        def between(a, b):
            if (b-a) % 8 == 2:
                return (a+1) % 8
            if (a-b) % 8 == 2:
                return (a-1) % 8
            return None

        for r in self.coords:
            # count neighbours in region
            surrounding = [
                i
                for i, inc in enumerate(all_incs)
                if utils.add_coord(r, inc) in self.coords
            ]
            neighbours = [i for i in surrounding if i % 2 == 1]

            assert (0 <= len(neighbours) <= 4)

            if len(neighbours) == 0:
                s += 4
                continue

            if len(neighbours) == 1:
                s += 2
                continue

            if len(neighbours) == 2:
                # straight line
                if (neighbours[0]-neighbours[1]) % 8 == 4:
                    continue
                # L shape
                s += 2
                # if in between is in, remove a vertex
                if between(neighbours[0], neighbours[1]) in surrounding:
                    s -= 1
                continue

            if len(neighbours) == 3:
                s += 2
                for a, b in ((0, 1), (1, 2), (2, 0)):
                    if between(neighbours[a], neighbours[b]) in surrounding:
                        s -= 1

            if len(neighbours) == 4:
                s += 8 - len(surrounding)
                continue

        return s


class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def get_region(self, start, char):
        region = Region()
        region.add(start)

        queue = [start]
        while queue:
            coord = queue.pop()
            for increment in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                neighbour = utils.add_coord(coord, increment)
                if not (0 <= neighbour[0] < self.xmax and 0 <= neighbour[1] < self.ymax):
                    continue
                if self.lines[neighbour[1]][neighbour[0]] == char and not region.contains(neighbour):
                    region.add(neighbour)
                    queue.append(neighbour)

        self.regions.append(region)

    def calculate(self):
        self.lines = [l.strip() for l in self.parser.get_lines()]
        self.ymax = len(self.lines)
        self.xmax = len(self.lines[0])
        self.regions = []
        for y, line in enumerate(self.lines):
            for x, char in enumerate(line):
                if all(not r.contains((x, y)) for r in self.regions):
                    self.get_region((x, y), char)

    def part_1(self):
        return sum(r.area*r.perimeter for r in self.regions)

    def part_2(self):
        return sum(r.area*r.sides for r in self.regions)
