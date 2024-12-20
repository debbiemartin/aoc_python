from ... import utils


class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
        self.designs = self.parser.get_sections_list()[0][0].split(", ")
        self.towels = self.parser.get_sections_list()[1]

    @utils.memoize
    def possible_count(self, pattern):
        if pattern == "":
            return 1

        return sum(self.possible_count(pattern[len(d):]) for d in self.designs if pattern.startswith(d)) or 0

    def part_1(self):
        return sum(1 for t in self.towels if self.possible_count(t) != 0)

    def part_2(self):
        return sum(self.possible_count(t) for t in self.towels)
