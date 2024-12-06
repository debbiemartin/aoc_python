from ... import utils


class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
        lines = self.parser.get_lines()
        self.obstacles = set()
        self.ymax = len(lines)
        self.xmax = len(lines[0])
        self.direction = (0, -1)
        for y in range(self.ymax):
            for x in range(self.xmax):
                if lines[y][x] == "#":
                    self.obstacles.add((x, y))
                elif lines[y][x] == "^":
                    self.start = (x, y)

    def walk(self, current, direction):
        visited = set()
        visited.add((current, direction))
        turn_right = {(0, -1): (1, 0), (1, 0): (0, 1),
                      (0, 1): (-1, 0), (-1, 0): (0, -1)}
        while True:
            try_next = utils.add_coord(current, direction)
            if try_next[0] < 0 or try_next[0] >= self.xmax or try_next[1] < 0 or try_next[1] >= self.ymax:
                # off grid
                break
            if try_next in self.obstacles:
                # turn instead
                direction = turn_right[direction]
                continue
            if (try_next, direction) in visited:
                return None
            current = try_next
            visited.add((try_next, direction))
        return set(v[0] for v in visited)

    def part_1(self):
        return len(self.walk(self.start, self.direction))

    def part_2(self):
        loops = 0
        path = self.walk(self.start, self.direction)
        for point in path:
            self.obstacles.add(point)
            visited = self.walk(self.start, self.direction)
            if not visited:
                loops += 1
            self.obstacles.remove(point)

        return loops
