class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def load(self, rounded):
        load = 0
        for r in rounded:
            load += self.ymax + 1 - r[1]
        return load

    def calculate(self):
        lines = self.parser.get_lines()
        self.ymax = len(lines) - 1
        self.xmax = len(lines[0]) - 1
        self.rounded = list()
        self.square = set()
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char == "O":
                    self.rounded.append((x,y))
                if char == "#":
                    self.square.add((x,y))

    def roll_north(self, rounded):
        rounded_final = list()
        rounded.sort(key=lambda x: x[1])
        for r in rounded:
            y = r[1]
            while y > 0 and (r[0], y-1) not in rounded_final and (r[0], y-1) not in self.square:
                y -= 1
            rounded_final.append((r[0], y))

        assert(len(set(rounded_final)) == len(rounded_final))

        return rounded_final


    def roll_south(self, rounded):
        rounded_final = list()
        rounded.sort(key=lambda x: x[1], reverse=True)
        for r in rounded:
            y = r[1]
            while y < self.ymax and (r[0], y+1) not in rounded_final and (r[0], y+1) not in self.square:
                y += 1
            rounded_final.append((r[0], y))
        assert(len(set(rounded_final)) == len(rounded_final))

        return rounded_final

    def roll_west(self, rounded):
        rounded_final = list()
        rounded.sort(key=lambda x: x[0])
        for r in rounded:
            x = r[0]
            while x > 0 and (x-1, r[1]) not in rounded_final and (x-1, r[1]) not in self.square:
                x -= 1
            rounded_final.append((x, r[1]))
        assert(len(set(rounded_final)) == len(rounded_final))

        return rounded_final

    def roll_east(self, rounded):
        rounded_final = list()
        rounded.sort(key=lambda x: x[0], reverse=True)
        for r in rounded:
            x = r[0]
            while x < self.xmax and (x+1, r[1]) not in rounded_final and (x+1, r[1]) not in self.square:
                x += 1
            rounded_final.append((x, r[1]))
        assert(len(set(rounded_final)) == len(rounded_final))

        return rounded_final

    def part_1(self):
        rounded = self.roll_north(self.rounded)

        return self.load(rounded)

    def print(self, rounded):
        for y in range(self.ymax+1):
            for x in range(self.xmax+1):
                if (x,y) in self.square:
                    print("#", end="")
                elif (x,y) in rounded:
                    print("O", end="")
                else:
                    print(".", end="")
            print()

    def part_2(self):
        rounded = self.rounded
        cache = []
        for i in range(1000000000):
            rounded = self.roll_north(rounded)
            rounded = self.roll_west(rounded)
            rounded = self.roll_south(rounded)
            rounded = self.roll_east(rounded)
            #self.print(rounded)

            cycle_length = 0
            if set(rounded) in cache:
                j = cache.index(set(rounded))
                print(f"cycle found: i {i}, j {j}")
                cycle_start = j
                cycle_length = i-cycle_start
                break

            cache.append(set(rounded))
            print(self.load(rounded))

        remainder = (1000000000-cycle_start-1) % cycle_length
        print([self.load(c) for c in cache])
        return self.load(cache[cycle_start+remainder])

