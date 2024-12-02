class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
        lines = self.parser.get_lines()
        self.lefts = [int(l.split()[0]) for l in lines]
        self.lefts.sort()
        self.rights = [int(l.split()[1]) for l in lines]
        self.rights.sort()

    def part_1(self):
        return sum(abs(r - l) for l, r in zip(self.lefts, self.rights))

    def part_2(self):
        return sum(l*self.rights.count(l) for l in self.lefts)
