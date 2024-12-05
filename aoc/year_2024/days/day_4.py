from ... import utils


class Day(object):
    DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0),
                  (1, 1), (1, -1), (-1, 1), (-1, -1))

    def __init__(self, parser):
        self.parser = parser
        self.lines = self.parser.get_lines()
        self.y_max = len(self.lines)
        self.x_max = len(self.lines[0].strip())

    def get_char(self, coord, direction=(0, 0), num=0):
        new_coord = (coord[0] + direction[0]*num, coord[1] + direction[1]*num)
        if 0 <= new_coord[0] < self.x_max and 0 <= new_coord[1] < self.y_max:
            return self.lines[new_coord[1]][new_coord[0]]
        else:
            return None

    def is_xmas(self, coord, direction):
        test = ""
        for i in range(4):
            char = self.get_char(coord, direction, i)
            if not char:
                return False
            test += char

        return test == "XMAS"

    def is_crossmas(self, coord):
        # (-1,1), (1,-1)
        if not self.get_char(coord) == "A":
            return False
        diagonal_1 = (self.get_char(coord, (1, 1), 1),
                      self.get_char(coord, (-1, -1), 1))
        if not diagonal_1 in (("M", "S"), ("S", "M")):
            return False
        diagonal_2 = (self.get_char(coord, (1, -1), 1),
                      self.get_char(coord, (-1, 1), 1))
        if not diagonal_2 in (("M", "S"), ("S", "M")):
            return False
        return True

    def calculate(self):
        pass

    def part_1(self):
        count = 0
        for x in range(self.x_max):
            for y in range(self.y_max):
                count += sum(
                    self.is_xmas((x, y), d) for d in self.DIRECTIONS)
        return count

    def part_2(self):
        return sum(self.is_crossmas((x, y)) for x in range(1, self.x_max) for y in range(1, self.y_max))
