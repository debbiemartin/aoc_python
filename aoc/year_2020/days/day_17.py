#!/usr/bin/python3

from .. import utils
import itertools
from collections import namedtuple

class Cube(object):
    def __init__(self, coord, n_dimensions):
        self.n_adj = 0
        self.neighbours = []
        self.active = False
        self.to_check = True
        combs = [-1, 1] * n_dimensions + [0] * (n_dimensions - 1)
        self.neighbour_incrs = set(itertools.permutations(combs, n_dimensions))
        self.add_neighbours(coord)

    def add_neighbours(self, coord):
        for neighbour in (utils.add_coord(n, coord) for n in self.neighbour_incrs):
            self.neighbours.append(neighbour)

    def set_active(self, active):
        self.active = active

class ConwaySim(object):
    """
    Conway cube simulator. Iterates the map in time intervals. Adds a new cube
    if necessary for any cubes which become active. This allows for infinite
    grid.
    """
    def __init__(self, n_dimensions, lines):
        self.grid = {}
        self.n_dimensions = n_dimensions

        # Add all cubes to the grid. If a cube is active, add its neighbours
        # as well
        for coord, active in (
            (self._make_coord(x, y), line[x] == "#") for y, line in enumerate(lines)
            for x in range(len(line)) if line[x] == "#" or line[x] == "."
        ):
            self._add_cube(coord)

            self.grid[coord].set_active(active)

            if active:
                for n in self.grid[coord].neighbours:
                    self._add_cube(n)

        # Work out the initial number of active neighbours for each cube
        for coord, cube in self.grid.items():
            cube.n_adj = sum(
                1 for n in cube.neighbours
                if (n in self.grid and self.grid[n].active))

    def _add_cube(self, coord):
        if coord not in self.grid:
            self.grid[coord] = Cube(coord, self.n_dimensions)

    def _make_coord(self, x, y):
        coord = [0] * self.n_dimensions
        coord[0] = x
        coord[1] = y
        return tuple(coord)

    def _iterate(self):
        changes = []

        # Check all cubes in the grid which have been marked to check - either
        # on cube initialization or if a neighbour has changed
        for coord, cube in self.grid.items():
            if not cube.to_check:
                continue

            # Empty or fill seat depending on number adjacent
            if ((cube.active and
                (cube.n_adj != 2 and cube.n_adj != 3)) or
                (not cube.active and cube.n_adj == 3)):
                changes.append(coord)

            cube.to_check = False

        # Apply the changes to grid
        for coord in changes:
            cube = self.grid[coord]
            cube.set_active(not cube.active)

            for neighbour in cube.neighbours:
                if neighbour not in self.grid:
                    self.grid[neighbour] = Cube(neighbour, self.n_dimensions)
                self.grid[neighbour].n_adj += (1 if cube.active else -1)
                self.grid[neighbour].to_check = True

        return len(changes) != 0

    def iterate(self, num):
        for i in range(num):
            self._iterate()

        return sum(1 for cube in self.grid.values() if cube.active)

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
        self.lines = self.parser.get_lines()

    def part_1(self):
        s = ConwaySim(3, self.lines)
        return s.iterate(6)

    def part_2(self):
        s = ConwaySim(4, self.lines)
        return s.iterate(6)
