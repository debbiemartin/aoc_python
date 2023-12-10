from .. import utils

class Day(object):
    pipes = {
        "J": {(1, 0): (0, -1), (0, 1): (-1, 0)},
        "-": {(1, 0): (1, 0), (-1, 0): (-1, 0)},
        "L": {(-1, 0): (0, -1), (0, 1): (1, 0)},
        "|": {(0, 1): (0, 1), (0, -1): (0, -1)},
        "F": {(0, -1): (1, 0), (-1, 0): (0, 1)},
        "7": {(0, -1): (-1, 0), (1, 0): (0, 1)},

    }
    def __init__(self, parser):
        self.parser = parser

    def step(self, coord, direction):
        mapping = self.pipes.get(self.get_char(coord))
        if mapping:
            return mapping.get(direction)

    def get_char(self, coord):
        return self.lines[coord[1]][coord[0]]

    def calculate(self):
        self.lines = self.parser.get_lines()
        for y, line in enumerate(self.lines):
            try:
                x = line.index("S")
            except:
                continue

            start = (x, y)
            break

        start_dirs = []
        for d in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            if self.step(utils.add_coord(start, d), d):
                start_dirs.append(d)
        assert(len(start_dirs) == 2)

        coord = start
        self.visited = set(start)
        direction = start_dirs[0]
        i = 1
        while True:
            next_coord = utils.add_coord(coord, direction)
            if next_coord == start:
                self.loop_length = i
                break
            self.visited.add(next_coord)
            i += 1
            direction = self.step(next_coord, direction)
            coord = next_coord


    def part_1(self):
        return self.loop_length/2

    def part_2(self):
        # Add up inside/outside for each row
        inside_count = 0
        for y, line in enumerate(self.lines):
            inside = False
            unmatched = set()
            for x, char in enumerate(line):
                if (x, y) in self.visited:
                    #@@@ Note: should really replace S with the appropriate
                    #          char depending on start_dirs but there is no
                    #          inside ground to the right of it in the input
                    # F and J make |
                    # F and 7 cancel
                    # L and 7 make |
                    # L and J cancel
                    if char == "|":
                        inside = not inside
                    if char == "F":
                        if "J" in unmatched:
                            unmatched.remove("J")
                            inside = not inside
                        elif "7" in unmatched:
                            unmatched.remove("7")
                        else:
                            unmatched.add("F")
                    if char == "J":
                        if "F" in unmatched:
                            unmatched.remove("F")
                            inside = not inside
                        elif "L" in unmatched:
                            unmatched.remove("L")
                        else:
                            unmatched.add("J")
                    if char == "7":
                        if "L" in unmatched:
                            unmatched.remove("L")
                            inside = not inside
                        elif "F" in unmatched:
                            unmatched.remove("F")
                        else:
                            unmatched.add("7")
                    if char == "L":
                        if "7" in unmatched:
                            unmatched.remove("7")
                            inside = not inside
                        elif "J" in unmatched:
                            unmatched.remove("J")
                        else:
                            unmatched.add("L")
                elif inside:
                    inside_count += 1

        return inside_count
