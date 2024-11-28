from .. import utils
from collections import defaultdict

class Day(object):
    dirs = {
        "se": (1,-1),
        "e":  (2,0),
        "ne": (1,1),
        "nw": (-1,1),
        "w":  (-2,0),
        "sw": (-1,-1),
    }

    def __init__(self, parser):
        self.parser = parser

    @utils.memoize
    def get_neighbours(self, coord):
        return [utils.add_coord(coord, dirval) for dirval in self.dirs.values()]

    def get_initial(self, lines):
        tiles = defaultdict(lambda: 0)

        for line in lines:
            coord = (0,0)

            while len(line) > 0:
                for dirname, dirval in self.dirs.items():
                    if line.startswith(dirname):
                        coord = utils.add_coord(coord, dirval)
                        line = line[len(dirname):]

            # Flip it - 1->0, 0->1
            tiles[coord] = 1 - tiles[coord]

        # Make the initial to_check list: all black tiles and their neighbours
        to_check = set()
        for key, val in ((key, val) for (key, val) in tiles.items() if val == 1):
            to_check.add(key)
            for n in self.get_neighbours(key):
                to_check.add(n)

        return tiles, to_check

    def play_day(self):
        new_to_check = set()
        to_flip = []

        for tile in self.to_check:
            black_neighbours = sum(1 for n in self.get_neighbours(tile) if self.tiles[n] == 1)
            flip = ((self.tiles[tile] == 0 and black_neighbours == 2) or
                    (self.tiles[tile] == 1 and
                    (black_neighbours == 0 or black_neighbours > 2)))

            if flip:
                to_flip.append(tile)
                for n in self.get_neighbours(tile):
                    new_to_check.add(n)

        # Flip tiles simultaneously
        for tile in to_flip:
            self.tiles[tile] = 1 - self.tiles[tile]

        return new_to_check

    def calculate(self):
        self.tiles, self.to_check = self.get_initial(self.parser.get_lines())

    def part_1(self):
        return sum(1 for t in self.tiles.values() if t == 1)

    def part_2(self):
        for i in range(100):
            self.to_check = self.play_day()

        return sum(1 for t in self.tiles.values() if t == 1)
