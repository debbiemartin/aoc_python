class Day(object):
    def __init__(self, parser):
        self.parser = parser

    @staticmethod
    def ways_to_win(time, record):
        for t in range(1, time):
            if (time-t) * t > record:
                min_time = t
                break
        for t in range(time-1, 1, -1):
            if (time-t) * t > record:
                max_time = t
                break
        return max_time - min_time + 1

    def calculate(self):
        lines = self.parser.get_lines()
        self.times = lines[0].split(":")[1].strip().split()
        self.records = lines[1].split(":")[1].strip().split()

    def part_1(self):
        prod = 1
        for time, record in zip(self.times, self.records):
            prod = prod * self.ways_to_win(int(time), int(record))

        return prod

    def part_2(self):
        time = int("".join(self.times))
        record = int("".join(self.records))

        return self.ways_to_win(time, record)
