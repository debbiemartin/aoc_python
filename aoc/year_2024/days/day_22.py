from ... import utils
from collections import defaultdict


class Day(object):
    def __init__(self, parser):
        self.parser = parser

    @utils.memoize
    def secret(self, x):
        x = ((x << 6) ^ x) % 2**24
        x = ((x >> 5) ^ x) % 2**24
        x = ((x << 11) ^ x) % 2**24

        return x

    def calculate(self):
        self.nums = [int(l) for l in self.parser.get_lines()]
        self.sum_secret = 0
        self.sequences = defaultdict(lambda: {})
        for n, num in enumerate(self.nums):
            sequence = []
            for i in range(2000):
                num = self.secret(num)
                if i > 0:
                    sequence.append((num % 10) - (prev_num % 10))
                    if len(sequence) > 4:
                        sequence.pop(0)
                    if len(sequence) == 4 and n not in self.sequences[tuple(sequence)]:
                        self.sequences[tuple(sequence)][n] = num % 10
                prev_num = num

            self.sum_secret += num

    def part_1(self):
        return self.sum_secret

    def part_2(self):
        return max(sum(d.values()) for d in self.sequences.values())
