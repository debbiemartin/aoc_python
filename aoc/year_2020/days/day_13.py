#!/usr/bin/python3

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
        lines = self.parser.get_lines()

        self.earliest_time = int(lines[0])
        self.buses = {index: int(bus) for index, bus in enumerate(lines[1].split(",")) if bus != "x"}

    def part_1(self):
        def wait_time(bus):
            return bus - self.earliest_time % bus
        # Want the smallest modulo of earliest_time/busnum
        bus = min(self.buses.values(), key=wait_time)
        return bus * wait_time(bus)

    def part_2(self):
        # want to efficiently get first time such that:
        # all((time+index)%bus == 0 for index, bus in buses.items())

        # solve each bus in turn. The time test increment must then be the LCM of
        # all solved buses.
        time, increment = 0, 1
        for index, bus in self.buses.items():
            # solve for this bus
            while True:
                time += increment
                if (time + index)%bus == 0:
                    # LCM of increment and prime bus num is just the product
                    increment = increment * bus
                    break
        return time

