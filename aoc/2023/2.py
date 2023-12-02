import re

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
        self.lines = self.parser.get_lines()

    def matches(self, line):
        return re.finditer(r"(\d+)\s([a-z]+)", line)

    def enough_cubes(self, line):
        maximums = {"red": 12, "green": 13, "blue": 14}
        for match in self.matches(line):
            groups = match.groups()
            if int(groups[0]) > maximums[groups[1]]:
                return False
        return True

    def part_1(self):
        possible_sum = 0
        for i, line in enumerate(self.lines):
            if self.enough_cubes(line):
                possible_sum += i+1

        return possible_sum

    def power(self, line, colour):
        return max(int(m.groups()[0]) for m in self.matches(line) if m.groups()[1] == colour)


    def part_2(self):
        power_sum = 0
        for line in self.lines:
            power_sum += self.power(line, "red") * self.power(line, "green") * self.power(line, "blue")

        return power_sum
