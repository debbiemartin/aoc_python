from collections import defaultdict
import numpy as np

class Day(object):
    start = "643719258"

    def __init__(self, parser):
        self.parser = parser
        self.mod = 1

    def move(self, current, nexts):
        # want to move the three cups after current
        next = current
        picked = []
        for _ in range(3):
            next = nexts[next]
            picked.append(next)

        # move current to point to the last picked's next
        nexts[current] = nexts[picked[2]]

        # work out dest
        dest = current
        while True:
            dest = (dest - 2) % self.mod + 1
            if dest not in picked:
                break

        # move dest to point to picked[0] and
        nexts[picked[2]] = nexts[dest]
        nexts[dest] = picked[0]

        current = nexts[current]

        return current, nexts

    def do_n_moves(self, nexts, current, n):
        for i in range(n):
            current, nexts = self.move(current, nexts)

        return nexts

    def calculate(self):
        self.cups = list(map(lambda x: int(x), self.start))

    def part_1(self):
        self.mod = 9
        nexts = {self.cups[i]: self.cups[(i + 1)%9] for i in range(9)}

        nexts = self.do_n_moves(nexts, self.cups[0], 100)

        # Make the string of the nexts circularly from 1 non-inclusive
        ret = ""
        curr = 1
        while True:
            curr = nexts[curr]
            if curr == 1:
                break
            ret += str(curr)

        return ret

    def part_2(self):
        self.mod = 1000000

        # Make the nexts array by padding up to a million
        nexts = [None] * (self.mod + 1)
        for i in range(len(self.cups)-1):
            nexts[self.cups[i]] = self.cups[i+1]
        nexts[self.cups[-1]] = len(self.cups) + 1

        for i in range(len(self.cups) + 1, self.mod):
            nexts[i] = i+1
        nexts[self.mod] = self.cups[0]

        nexts = self.do_n_moves(np.array(nexts), self.cups[0], 10000000)

        return nexts[1] * nexts[nexts[1]]


