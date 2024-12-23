from ... import utils
from collections import defaultdict


class Day(object):
    numerical = {
        "0": (1, 0), "A": (2, 0), "1": (0, 1), "2": (1, 1), "3": (2, 1),
        "4": (0, 2), "5": (1, 2), "6": (2, 2), "7": (0, 3), "8": (1, 3), "9": (2, 3)
    }
    directional = {
        "<": (0, 0), "v": (1, 0), ">": (2, 0), "^": (1, 1), "A": (2, 1)
    }

    def __init__(self, parser):
        self.parser = parser

    @utils.memoize
    def increment_to_dirs(self, coord, last_coord, forbidden):
        x = last_coord[0]
        y = last_coord[1]
        dx = coord[0]-last_coord[0]
        dy = coord[1]-last_coord[1]

        if dy == 0:
            ystr = None
        elif dy > 0:
            ystr = "^" * dy
        else:
            ystr = "v" * abs(dy)

        if dx == 0:
            xstr = None
        elif dx > 0:
            xstr = ">" * dx
        else:
            xstr = "<" * abs(dx)

        if not xstr and not ystr:
            return ["A"]
        elif xstr and not ystr:
            return [xstr + "A"]
        elif not xstr and ystr:
            return [ystr + "A"]
        else:
            strings = []
            if (x+dx, y) != forbidden:
                strings.append(xstr + ystr + "A")
            if (x, y+dy) != forbidden:
                strings.append(ystr + xstr + "A")
            return strings

    @utils.memoize
    def get_directional_recursive(self, char, last_char, recursions):
        strings = self.increment_to_dirs(
            self.directional[char],
            self.directional[last_char],
            (0, 1)
        )

        if recursions == 1:
            return min(len(s) for s in strings)

        def get_len_str(s):
            count = 0
            last_c = "A"
            for c in s:
                count += self.get_directional_recursive(
                    c, last_c, recursions-1)
                last_c = c
            return count

        return min(get_len_str(s) for s in strings)

    def convert_numerical_to_directional(self, char, last_char):
        return self.increment_to_dirs(
            self.numerical[char],
            self.numerical[last_char],
            (0, 0)
        )

    def get_pattern_len(self, string, num_recursions):
        def get_len_str(s):
            count = 0
            last_char_d = "A"
            for char_d in s:
                count += self.get_directional_recursive(
                    char_d, last_char_d, num_recursions)
                last_char_d = char_d
            return count

        count = 0
        last_char_n = "A"
        for char_n in string:
            strings = self.convert_numerical_to_directional(
                char_n, last_char_n
            )
            count += min(get_len_str(s) for s in strings)
            last_char_n = char_n

        return count

    def calculate(self):
        self.lines = [l.strip("\n") for l in self.parser.get_lines()]

    def part_1(self):
        return sum(self.get_pattern_len(l, 2)*int(l[:3]) for l in self.lines)

    def part_2(self):
        return sum(self.get_pattern_len(l, 25)*int(l[:3]) for l in self.lines)
