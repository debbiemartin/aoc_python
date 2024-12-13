
import re


class Machine(object):
    def __init__(self, a_dx, a_dy, b_dx, b_dy, x, y):
        self.a_dx = a_dx
        self.a_dy = a_dy
        self.b_dx = b_dx
        self.b_dy = b_dy
        self.x = x
        self.y = y

    def min_tokens(self):
        # Tokens is 3*x pushes + 1*y pushes
        possibles = []

        for n_a in range(101):
            if (self.x-(n_a*self.a_dx)) % self.b_dx != 0:
                continue

            n_b = (self.x-(n_a*self.a_dx)) // self.b_dx
            if (n_a * self.a_dy) + (n_b * self.b_dy) == self.y:
                possibles.append((n_a, n_b))

        if len(possibles) == 0:
            return None

        return min((3*a)+b for a, b in possibles)

    def min_tokens_offset(self, offset=10000000000000):
        x = self.x + offset
        y = self.y + offset
        b = (self.a_dy*x-self.a_dx*y) / \
            (self.a_dy*self.b_dx-self.b_dy*self.a_dx)
        a = (x-self.b_dx*b)/self.a_dx

        if b % 1 != 0 or a % 1 != 0:
            return None

        return int(3*a + b)


class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
        self.machines = []
        a_reg = re.compile(r"Button A: X\+(?P<x>[0-9]+), Y\+(?P<y>[0-9]+)")
        b_reg = re.compile(r"Button B: X\+(?P<x>[0-9]+), Y\+(?P<y>[0-9]+)")
        prize_reg = re.compile(r"Prize: X=(?P<x>[0-9]+), Y=(?P<y>[0-9]+)")

        for section in self.parser.get_sections_list():
            a = a_reg.match(section[0])
            b = b_reg.match(section[1])
            prize = prize_reg.match(section[2])

            self.machines.append(
                Machine(
                    int(a.group("x")),
                    int(a.group("y")),
                    int(b.group("x")),
                    int(b.group("y")),
                    int(prize.group("x")),
                    int(prize.group("y")),
                )
            )

    def part_1(self):
        return sum(t for t in (m.min_tokens() for m in self.machines) if t is not None)

    def part_2(self):
        return sum(t for t in (m.min_tokens_offset() for m in self.machines) if t is not None)
