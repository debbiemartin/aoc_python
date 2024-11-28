from .. import utils
import heapq

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def valid_dirs(self, coord, directions):
        def is_valid(d):
            new_coord = utils.add_coord(coord, d)
            return (0<=new_coord[0]<=self.xmax and 0<=new_coord[1]<=self.ymax)

        return list(filter(is_valid, directions))

    def calculate(self):
        self.lines = self.parser.get_lines()
        self.ymax = len(self.lines) - 1
        self.xmax = len(self.lines[0]) - 1

    def shortest_len(self):
        visited = {}
        shortest_len = None

        queue = [(0, (0,0), d, 1) for d in self.valid_dirs((0,0), [(1,0), (0,1), (-1,0), (0,-1)])]

        while len(queue) > 0:
            length, coord, direction, direction_count = heapq.heappop(queue)
            if (coord, direction, direction_count) in visited:
                #if visited[(coord, direction, direction_count)] <= length:
                #    continue
                continue
            visited[(coord, direction, direction_count)] = length

            next_coord = utils.add_coord(coord, direction)
            new_length = int(self.lines[next_coord[1]][next_coord[0]]) + length

            if next_coord == (self.xmax, self.ymax):
                if not self.min_directions or direction_count >= self.min_directions:
                    # minimise over all dir, count
                    if not shortest_len:
                        shortest_len = new_length
                    shortest_len = min(shortest_len, new_length)
                    continue

            if self.min_directions and direction_count < self.min_directions:
                directions = [direction]
            else:
                if direction[0] != 0:
                    directions = [direction, (0,1), (0,-1)]
                else:
                    directions = [direction, (1,0), (-1,0)]

            if direction_count >= self.max_directions:
                directions.remove(direction)

            for d in self.valid_dirs(next_coord, directions):
                heapq.heappush(queue, (new_length, next_coord, d, (1 if d != direction else direction_count + 1)))

        return shortest_len

    def part_1(self):
        self.min_directions = None
        self.max_directions = 3
        return self.shortest_len()

    def part_2(self):
        self.min_directions = 4
        self.max_directions = 10
        return self.shortest_len()
