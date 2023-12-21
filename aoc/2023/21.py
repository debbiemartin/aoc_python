from collections import deque
import numpy as np
from .. import utils

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
        self.rocks = set()
        lines = self.parser.get_lines()
        assert len(lines) == len(lines[0])
        self.grid_size = len(lines)

        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char == "#":
                    self.rocks.add((x,y))
                if char == "S":
                    self.start = (x,y)

    def solve(self, steps):
        modulos = []
        coords = set([self.start])

        for i in range(1, 1 + steps):
            new_coords = set()
            for coord in coords:
                for direction in ((0,1), (1,0), (0,-1), (-1,0)):
                    ncoord = utils.add_coord(coord, direction)
                    if not (ncoord[0]%self.grid_size, ncoord[1]%self.grid_size) in self.rocks:
                        new_coords.add(ncoord)
            coords = new_coords

            if i % self.grid_size == steps % self.grid_size:
                modulos.append(len(coords))

            if len(modulos) == 3:
                x = np.array([0,1,2])
                y = np.array(modulos)
                poly = np.polyfit(x, y, deg=2)
                return np.polyval(poly, steps // self.grid_size)

        return len(coords)

    def part_1(self):
        return self.solve(64)

    def part_2(self):
        #return test(self.parser.get_lines(), 26501365)
        return self.solve(26501365)

