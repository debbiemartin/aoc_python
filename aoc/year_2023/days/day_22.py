from collections import defaultdict, deque

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
        bricks = []
        lines = self.parser.get_lines()
        for l in lines:
            a, b = l.split("~")
            brick = tuple(int(x) for x in a.split(",")), tuple(int(x) for x in b.split(","))

            equals = [brick[0][x] == brick[1][x] for x in range(3)]
            assert(equals.count(False)) in (1,0) # if 0, just 1 cube brick

            coords = []
            assert(all(brick[1][x] >= brick[0][x] for x in range(2)))
            for x in range(brick[0][0], brick[1][0]+1):
                for y in range(brick[0][1], brick[1][1]+1):
                    for z in range(brick[0][2], brick[1][2]+1):
                        coords.append((x,y,z))

            bricks.append(coords)

        bricks.sort(key=lambda x: x[0][2])

        self.ground_bricks = []
        for i, coords in enumerate(bricks):
            supported = []
            while True:
                 new_coords = [(x,y,z-1) for x,y,z in coords]
                 if any(nc[2] < 1 for nc in new_coords):
                     # hit the floor
                     break

                 for i, g in enumerate(self.ground_bricks):
                     if any(nc in g["coords"] for nc in new_coords):
                         supported.append(i)

                 if len(supported) > 0:
                     break

                 coords = new_coords

            self.ground_bricks.append({"coords": coords, "supported": supported})
        self.supporting = set()
        for g in self.ground_bricks:
            if len(g["supported"]) == 1:
                self.supporting.add(g["supported"][0])

    def part_1(self):
        return len(self.ground_bricks) - len(self.supporting)

    def part_2(self):
        support_map = defaultdict(set)
        for i, g in enumerate(self.ground_bricks):
            for s in g["supported"]:
                support_map[s].add(i)

        total = 0
        for start in self.supporting:
            queue = deque([start])
            chain = set([start])
            while queue:
                s = queue.popleft()

                for ns in support_map[s]:
                    if ns not in chain and all(x in chain for x in self.ground_bricks[ns]["supported"]):
                        queue.append(ns)
                        chain.add(ns)
            total += len(chain)-1

        return total
