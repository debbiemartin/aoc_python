import math

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
        lines = self.parser.get_lines()
        self.num_winning = []
        for i, line in enumerate(lines):
            winning, numbers = line.split(": ")[1].split(" | ")
            winning = set(int(w.strip()) for w in winning.split())
            numbers = set(int(n.strip()) for n in numbers.split())
            self.num_winning.append(len(winning.intersection(numbers)))

    def score(self, n):
        return int(math.pow(2, n-1)) if n > 0 else 0

    def part_1(self):
        return sum(self.score(n) for n in self.num_winning)

    def part_2(self):
        copies = [1 for _ in range(len(self.num_winning))]
        for i, n in enumerate(self.num_winning):
            for j in range(i+1, i+1+n):
                if j < len(copies):
                    copies[j] += copies[i]

        return sum(copies)

