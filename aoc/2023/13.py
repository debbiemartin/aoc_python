class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def v_match(self, x1, x2, y, rocks):
        left = (x1, y) in rocks
        right = (x2, y) in rocks
        return (0 if left == right else 1)

    def h_match(self, x, y1, y2, rocks):
        above = (x, y1) in rocks
        below = (x, y2) in rocks
        return (0 if above == below else 1)

    def get_reflection(self, xmax, ymax, rocks, diff_expected):
        # vertical mirrors
        cols = list(range(xmax))
        for col in range(xmax-1):
           diff = sum(self.v_match(x1, x2, y, rocks) for y in range(ymax) for x1, x2 in zip(cols[col::-1], cols[col+1:]))
           if diff == diff_expected:
               return col+1

        # horizontal mirrors
        rows = list(range(ymax))
        for row in range(ymax-1):
           diff = sum(self.h_match(x, y1, y2, rocks) for x in range(xmax) for y1, y2 in zip(rows[row::-1], rows[row+1:]))
           if diff == diff_expected:
               return (row+1)*100

        assert(False)

    def calculate(self):
        self.sections = self.parser.get_sections_list()

    def get_score(self, diff_expected=0):
        score = 0
        for pattern in self.sections:
             rocks = set()
             for y, line in enumerate(pattern):
                 for x, char in enumerate(line):
                     if char == "#":
                         rocks.add((x,y))
             score += self.get_reflection(len(pattern[0]), len(pattern), rocks, diff_expected=diff_expected)

        return score

    def part_1(self):
        return self.get_score()

    def part_2(self):
        return self.get_score(diff_expected=1)
