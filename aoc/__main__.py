import os
import re
import importlib
import sys
from . import input_parser
import argparse


def run_module(year, day):
    module = importlib.import_module(f"aoc.year_{year}.days.day_{day}")
    print(f"Day {day}:")
    p = input_parser.Parser(year, day)
    d = module.Day(p)
    d.calculate()

    print("PART 1:")
    print(d.part_1())
    print("PART 2:")
    print(d.part_2())


parser = argparse.ArgumentParser(description="")
parser.add_argument("year", help="AOC year to run", type=int)
parser.add_argument(
    "day",
    help="AOC day to run. If not supplied, runs all for the AOC year.",
    type=int,
    nargs="?"
)
args = parser.parse_args()

if args.day:
    run_module(args.year, args.day)
else:
    # Find out which days are present
    r = re.compile("day_(?P<day>[0-9]+).py")
    days = []
    for file in os.listdir(os.path.join("aoc", f"year_{args.year}", "days")):
        m = r.match(file)
        if m:
            days.append(m.group("day"))

    for day in sorted(map(lambda x: int(x), days)):
        run_module(args.year, day)
        print()
