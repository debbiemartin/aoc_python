from .. import utils

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def print_map(self):
        for y in range(min(c[1] for c in self.coords), max(c[1] for c in self.coords)+1):
            for x in range(min(c[0] for c in self.coords), max(c[0] for c in self.coords)+1):
                if (x,y) in self.coord_set:
                    print("#", end="")
                else:
                    print(".", end="")
            print("")

    def calculate(self):
        self.lines = self.parser.get_lines()

    def cross(self, p1, p2):
        return (p1[0] * p2[1]) - (p1[1] * p2[0])

    def manhattan_distance(self, p1, p2):
        return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

    def find_area(self, process_fn):
        points = [(0,0)]
        for line in self.lines:
            direction, count = process_fn(line)
            difference = (direction[0]*count, direction[1]*count)
            points.append(utils.add_coord(points[-1], difference))

        assert points[-1] == (0,0)
        area = 0
        perimeter = 0
        for i in range(len(points)):
            area += self.cross(points[i-1], points[i])
            perimeter += self.manhattan_distance(points[i], points[i-1])
        area = abs(area)
        interior = area//2 - perimeter//2 + 1

        return perimeter + interior

    def part_1(self):
        def process(line):
            dir_map = {"R": (1,0), "D": (0,-1), "L":(-1,0), "U":(0,1)}
            direction = dir_map[line.split()[0]]
            count = int(line.split()[1])

            return direction, count

        return self.find_area(process)

    def part_2(self):
        def process(line):
            dir_map = {"0": (1,0), "1": (0,-1), "2":(-1,0), "3":(0,1)}
            direction = dir_map[line.split()[2][-2]]
            count = int(line.split()[2][2:-2], 16)

            return direction, count

        return self.find_area(process)
