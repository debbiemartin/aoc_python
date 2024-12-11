from ... import utils


class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
        self.stones = [int(x) for x in self.parser.get_lines()[0].split()]

    def blink(self, stone):
        if stone == 0:
            return [1]

        s = str(stone)
        if len(s) % 2 == 0:
            return [int(s[:len(s)//2]), int(s[len(s)//2:])]

        return [stone * 2024]

    @utils.memoize
    def blink_recursive(self, stone, remaining):
        if remaining == 0:
            return 1
        else:
            return sum(self.blink_recursive(s, remaining-1) for s in self.blink(stone))

    def part_1(self):
        return sum(self.blink_recursive(s, 25) for s in self.stones)

    def part_2(self):
        return sum(self.blink_recursive(s, 75) for s in self.stones)
