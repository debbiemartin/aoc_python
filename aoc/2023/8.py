import math

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
        self.sections = self.parser.get_sections_list()
        self.rl = self.sections[0][0]
        self.nodes = {}
        for line in self.sections[1]:
            dests = line.split(" = ")[1].strip("()").split(", ")
            self.nodes[line.split(" = ")[0]] = dests

    def steps(self, node, match):
        i = 0
        while True:
            right = (self.rl[i % len(self.rl)] == "R")
            i += 1
            node = self.nodes[node][(1 if right else 0)]
            if match(node):
                return i

    def part_1(self):
        return self.steps(self.sections[1][0].split(" = ")[0], match=lambda x: x == "ZZZ")

    def part_2(self):
        ans = [self.steps(n, lambda x: x.endswith("Z")) for n in self.nodes.keys() if n.endswith("A")]

        return math.lcm(*ans)

