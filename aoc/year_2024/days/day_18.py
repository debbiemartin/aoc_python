import heapq
from ... import utils


class Day(object):
    def __init__(self, parser):
        self.parser = parser
        self.size = 70
        self.num_bytes = 1024

    def calculate(self):
        self.obstacles = [
            (int(l.split(",")[0]), int(l.split(",")[1]))
            for l in self.parser.get_lines()
        ]
        self.space = set(
            (x, y)
            for x in range(self.size+1)
            for y in range(self.size+1)
        )
        for i in range(self.num_bytes):
            self.space.remove(self.obstacles[i])

    def shortest_path(self, space):
        visited = set()
        shortest_len = None

        queue = [(0, (0, 0))]

        while len(queue) > 0:
            length, coord = heapq.heappop(queue)
            if coord == (self.size, self.size):
                return length

            if coord in visited:
                continue
            visited.add(coord)

            for d in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                next_coord = utils.add_coord(coord, d)
                if not next_coord in visited and coord in space:
                    heapq.heappush(queue, (length+1, next_coord))

    def part_1(self):
        return self.shortest_path(self.space.copy())

    def part_2(self):
        space = self.space.copy()

        for i in range(self.num_bytes, len(self.obstacles)):
            space.remove(self.obstacles[i])
            if not self.shortest_path(space):
                return f"{self.obstacles[i][0]},{self.obstacles[i][1]}"
