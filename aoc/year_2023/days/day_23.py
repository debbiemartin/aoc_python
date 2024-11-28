from .. import utils
from collections import deque

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
        lines = self.parser.get_lines()
        self.start = (lines[0].index("."), 0)
        self.end = (lines[-1].index("."), len(lines)-1)

        self.path = set()
        self.slopes = dict()
        dirs = {">": (1,0), "<": (-1,0), "^": (0,-1), "v": (0,1)}

        for y, l in enumerate(lines):
            for x, char in enumerate(l):
                if char == ".":
                    self.path.add((x,y))
                elif char in dirs.keys():
                    self.slopes[(x,y)] = dirs[char]
                    self.path.add((x,y))

    def walk_until_junction(self, coord, visited):
        new_coords = [coord]
        walk = 0
        while len(new_coords) == 1:
            coord = new_coords[0]
            if coord == self.end:
                return walk, [self.end]

            walk += 1
            visited.add(coord)

            if coord in self.slopes:
                # we have to go in that direction
                new_coords = [utils.add_coord(coord, self.slopes[coord])]
            else:
                new_coords = (utils.add_coord(coord, d) for d in ((0,1), (1,0), (0,-1), (-1,0)))

            new_coords = list(filter(lambda x: x in self.path and not x in visited, new_coords))

        return walk, new_coords

    def longest_path(self):
        queue = deque([(self.start, 0, set([self.start]))])
        end = -1 * 10**6

        while queue:
            coord, walk_len, visited = queue.pop()
            if coord == self.end:
                end = max(end, walk_len)
                continue

            junction_len, new_coords = self.walk_until_junction(coord, visited) # adds to visited
            for new_coord in new_coords:
                new_walk_len = walk_len + junction_len
                queue.appendleft((new_coord, new_walk_len, visited.copy()))

        return end

    def part_1(self):
        return self.longest_path()

    def part_2(self):
        self.slopes = {}
        return self.longest_path()
