import re
from collections import defaultdict
from functools import reduce


class Day(object):
    def __init__(self, parser):
        self.parser = parser
        self.xmax = 101
        self.ymax = 103

    def calculate(self):
        self.robots = []
        pattern = re.compile(
            r"p=(?P<x>[0-9]+),(?P<y>[0-9]+) v=(?P<vx>-?[0-9]+),(?P<vy>-?[0-9]+)")
        for l in self.parser.get_lines():
            m = pattern.match(l)
            self.robots.append(tuple(int(g) for g in m.groups()))

    def get_halves(self, val):
        return (
            (0, int((val-1)/2)),
            (int((val+1)/2), self.xmax)
        )

    def part_1(self):
        # 100 secs simulation
        final = defaultdict(int)
        for (x, y, vx, vy) in self.robots:
            final[(x+vx*100) % self.xmax, (y+vy*100) % self.ymax] += 1

        # calc 4 quadrants
        segs = [0, 0, 0, 0]
        for (x, y), count in final.items():
            if x < (self.xmax-1)/2:
                if y < (self.ymax-1)/2:
                    segs[0] += count
                elif y > (self.ymax-1)/2:
                    segs[1] += count
            elif x > (self.xmax-1)/2:
                if y < (self.ymax-1)/2:
                    segs[2] += count
                elif y > (self.ymax-1)/2:
                    segs[3] += count
        return reduce(lambda a, b: a * b, segs)

    def part_2(self):
        step = 0
        while True:
            step += 1
            final = defaultdict(int)
            for (x, y, vx, vy) in self.robots:
                final[(x+vx*step) % self.xmax, (y+vy*step) % self.ymax] += 1

            if any(
                all(
                    final.get((x+dx, y+dy))
                    for dx, dy in
                    [(-1, 1), (0, 1), (1, 1), (-1, 0),
                     (1, 0), (-1, -1), (0, -1), (1, -1)]
                )
                for x, y in final.keys()
            ):
                break

        for y in range(self.ymax):
            print("".join(
                str(final.get((x, y)) or ".")
                for x in
                range(self.xmax))
            )
        return step
