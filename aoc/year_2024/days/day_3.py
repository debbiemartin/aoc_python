import re


class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
        self.input = self.parser.get_lines()
        self.pattern = re.compile(r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))")

    def get_sum(self, switch=False):
        sum = 0
        do = True
        for line in self.input:
            instructions = self.pattern.findall(line)
            for i in instructions:
                if i[0].startswith("mul"):
                    if not switch or do:
                        sum += int(i[1])*int(i[2])
                elif i[0].startswith("don't"):
                    do = False
                else:
                    assert i[0].startswith("do")
                    do = True
        return sum

    def part_1(self):
        return self.get_sum(False)

    def part_2(self):
        return self.get_sum(True)
