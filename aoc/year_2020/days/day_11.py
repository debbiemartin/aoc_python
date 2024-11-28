#!/usr/bin/python3

import itertools
from collections import namedtuple

class Seat(object):
    def __init__(self):
        self.n_adj = 0
        self.filled = False
        self.neighbours = []
        self.to_check = True

    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)


class SeatSim(object):
    """
    Seat simulator. Iterates the seat map in time intervals.
    """
    def __init__(self, lines, part2=False):
        self.seatmap = {}
        self.part2 = part2

        self.lines = lines
        self.YMAX = len(lines)
        self.XMAX = len(lines[0])
        for coord in (
            (x, y) for y, line in enumerate(lines)
            for x in range(len(line)) if line[x] == "L"
        ):
            self.seatmap[coord] = Seat()
        self.neighbour_incrs = set(itertools.permutations([-1,-1,0,1,1], 2))

        # Work out each seat's neighbours up front
        for coord, seat in self.seatmap.items():
            if part2:
                for n in self.neighbour_incrs:
                    # find line of sights - make sure we don't leave the grid
                    ncoord = coord
                    while (ncoord[0] >= 0 and ncoord[0] <= self.XMAX and
                           ncoord[1] >= 0 and ncoord[1] <= self.YMAX):
                        ncoord = self.add_coord(ncoord, n)
                        if ncoord in self.seatmap:
                            seat.add_neighbour(ncoord)
                            break
            else:
                # Nearest neighbours
                for neighbour in (self.add_coord(n, coord) for n in self.neighbour_incrs):
                    if neighbour in self.seatmap:
                        seat.add_neighbour(neighbour)

    def __str__(self):
        str = ""
        for y in range(self.YMAX):
            for x in range(self.XMAX):
                str += (
                    "." if (x,y) not in self.seatmap else
                    ("#" if self.seatmap[(x,y)].filled else "L")
                )
            str += "\n"

        return str

    def add_coord(self, coord1, coord2):
        return (coord1[0] + coord2[0], coord1[1] + coord2[1])

    def _iterate(self):
        changes = []

        for coord, seat in self.seatmap.items():
            # don't process floor space
            if not seat.to_check:
                continue

            # Empty or fill seat depending on number adjacent
            if ((seat.filled and
                (seat.n_adj >= 5 or seat.n_adj == 4 and not self.part2)) or
                (not seat.filled and seat.n_adj == 0)):
                changes.append(coord)

            seat.to_check = False

        # Apply the changes to seatmap
        for coord in changes:
            seat = self.seatmap[coord]
            seat.filled = not seat.filled

            for neighbour in seat.neighbours:
                self.seatmap[neighbour].n_adj += (1 if seat.filled else -1)
                self.seatmap[neighbour].to_check = True

        return len(changes) != 0

    def iterate_until_static(self):
        while True:
            #print(self) # for debug
            if not self._iterate():
                break

        return sum(1 for seat in self.seatmap.values() if seat.filled)

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
        self.lines = self.parser.get_lines()

    def part_1(self):
        s = SeatSim(self.lines)
        return s.iterate_until_static()

    def part_2(self):
        s = SeatSim(self.lines, True)
        return s.iterate_until_static()
