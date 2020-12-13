#!/usr/bin/python3

from . import utils

def main():
    lines = utils.get_lines(13)

    earliest_time = int(lines[0])
    buses = {index: int(bus) for index, bus in enumerate(lines[1].split(",")) if bus != "x"}
    
    
    print("PART 1:")
    def wait_time(bus):
        return bus - earliest_time % bus
    # Want the smallest modulo of earliest_time/busnum
    bus = min(buses.values(), key=wait_time)
    print(bus * wait_time(bus))
    
    print("PART 2:")
    # want to efficiently get first time such that:
    # all((time+index)%bus == 0 for index, bus in buses.items())
    
    # solve each bus in turn. The time test increment must then be the LCM of 
    # all solved buses.
    time, increment = 0, 1
    for index, bus in buses.items():
        # solve for this bus
        while True:
            time += increment
            if (time + index)%bus == 0:
                # LCM of increment and prime bus num is just the product
                increment = increment * bus
                break
    print(time)
        