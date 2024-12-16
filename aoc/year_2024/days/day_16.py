import heapq
from ... import utils


class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
        self.walls = set()
        for y, line in enumerate(self.parser.get_lines()):
            for x, char in enumerate(line):
                if char == "#":
                    self.walls.add((x, y))
                if char == "S":
                    self.start = (x, y)
                if char == "E":
                    self.end = (x, y)

        queue = [
            (0, self.start, (1, 0))
        ]
        heapq.heapify(queue)
        self.visited = {}
        while queue:
            score, coord, d = heapq.heappop(queue)
            if (coord, d) in self.visited:
                continue
            self.visited[(coord, d)] = score

            if coord == self.end:
                self.final_score = score
                self.final_d = d
                break

            # check forward, L, R
            for next_coord, next_d, step in ((utils.add_coord(coord, d), d, 1), (coord, (d[1], d[0]), 1000), (coord, (-1*d[1], -1*d[0]), 1000)):
                if next_coord not in self.walls:
                    heapq.heappush(queue, (score + step, next_coord, next_d))

    def part_1(self):
        return self.final_score

    def path_plot(self, coord, d, score):
        self.path.add(coord)
        if coord == self.start:
            return

        # step before
        prev_coord = utils.add_coord(coord, (-1*d[0], -1*d[1]))
        prev_score = self.visited.get((prev_coord, d))
        if prev_score == score - 1:
            self.path_plot(prev_coord, d, prev_score)

        # rotate before
        for prev_d in ((d[1], d[0]), (-1*d[1], -1*d[0])):
            prev_score = self.visited.get((coord, prev_d))
            if prev_score == score - 1000:
                self.path_plot(coord, prev_d, prev_score)

    def part_2(self):
        self.path = set()
        self.path_plot(self.end, self.final_d, self.final_score)

        # for y in range(len(self.parser.get_lines())):
        #     for x in range(len(self.parser.get_lines()[0])):
        #         if (x, y) in self.walls:
        #             print("#", end="")
        #         elif (x, y) == self.end:
        #             print("E", end="")
        #         elif (x, y) == self.start:
        #             print("S", end="")
        #         elif (x, y) in self.path:
        #             print("O", end="")
        #         else:
        #             print(".", end="")
        #     print()

        return len(self.path)
