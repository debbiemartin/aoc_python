#!/usr/bin/python3

from collections import namedtuple


class Day(object):
    do_inst = {
        "nop": lambda i, a, val: (i + 1, a),
        "acc": lambda i, a, val: (i + 1, a + val),
        "jmp": lambda i, a, val: (i + val, a),
    }
    def __init__(self, parser):
        self.parser = parser

    def run(self, inst_to_change=-1):
        visited = set() # already-visited instructions
        acc, i = 0, 0

        while i not in visited and i != len(self.instructions):
            visited.add(i)
            # change the name of the inst if specified
            name = self.instructions[i].name
            name = (name if (i != inst_to_change or name == "acc") else ("nop" if name == "jmp" else "jmp"))
            i, acc = self.do_inst[name](i, acc, self.instructions[i].val)

        return (i == len(self.instructions), acc)


    def calculate(self):
        lines = self.parser.get_lines()

        Inst = namedtuple("Inst", ["name", "val"])
        self.instructions = list(map(lambda i: Inst(i.split(" ")[0], int(i.split(" ")[1])), lines))

    def part_1(self):
        finished, acc = self.run(self.instructions)
        return acc

    def part_2(self):
        for i, inst in enumerate(self.instructions):
            if self.instructions[i].name == "acc":
                continue
            finished, acc = self.run(i)
            if finished:
                return acc
