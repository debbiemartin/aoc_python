import os
import re
import importlib
import sys
from . import parser

def run_module(year, day):
    module = importlib.import_module(f"aoc.{year}.{day}")
    print(f"Day {day}:")
    p = parser.Parser(year, day)
    d = module.Day(p)
    d.calculate()

    print("PART 1:")
    print(d.part_1())
    print("PART 2:")
    print(d.part_2())


if len(sys.argv) == 3:
    run_module(sys.argv[1], sys.argv[2])
elif len(sys.argv) == 2:
    year = sys.argv[1]
    # Find out which days are present
    r = re.compile("(?P<day>[0-9]+).py")
    days = []
    for file in os.listdir(os.path.join("aoc", year)):
        m = r.match(file)
        if m:
            days.append(m.group("day"))

    for day in sorted(map(lambda x: int(x), days)):
        run_module(year, day)
        print()
