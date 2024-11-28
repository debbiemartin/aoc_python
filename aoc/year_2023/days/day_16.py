from .. import utils

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def beam(self, coord, direction):
        while 0 <= coord[0] < self.xmax and 0 <= coord[1] < self.ymax:
            if (coord, direction) in self.energised:
                break
            self.energised.add((coord, direction))
            char = self.map[coord[1]][coord[0]]
            if char == ".":
                pass
            elif char == "/":
                dir_map = {(1,0): (0,-1), (0,1): (-1,0), (-1,0):(0,1), (0,-1):(1,0)}
                direction = dir_map[direction]
            elif char == "\\":
                dir_map = {(1,0): (0,1), (0,1): (1,0), (-1,0):(0,-1), (0,-1):(-1,0)}
                direction = dir_map[direction]
            elif char == "|":
                if direction[0] != 0:
                    self.beam(utils.add_coord(coord,(0,1)), (0,1))
                    self.beam(utils.add_coord(coord,(0,-1)), (0,-1))
                    break
            elif char == "-":
                if direction[1] != 0:
                    self.beam(utils.add_coord(coord,(1,0)), (1,0))
                    self.beam(utils.add_coord(coord,(-1,0)), (-1,0))
                    break
            coord = utils.add_coord(coord, direction)

    def calculate(self):
        self.map = self.parser.get_lines()
        self.energised = set()
        self.ymax = len(self.map)
        self.xmax = len(self.map[0])

    def energised_count(self, coord, direction):
        self.energised = set()
        self.beam(coord, direction)
        return len(set(e[0] for e in self.energised))

    def part_1(self):
        return self.energised_count((0,0), (1,0))

    def part_2(self):
        max_left = max(self.energised_count((0,y), (1,0)) for y in range(self.ymax))
        max_right = max(self.energised_count((self.xmax-1,y), (-1,0)) for y in range(self.ymax))
        max_down = max(self.energised_count((x,0), (0,1)) for x in range(self.xmax))
        max_up = max(self.energised_count((x,self.ymax-1), (0,-1)) for x in range(self.xmax))

        return max((max_left, max_right, max_down, max_up))
