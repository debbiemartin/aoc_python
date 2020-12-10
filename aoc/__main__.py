import os 
import re
import importlib
import sys

def run_module(day):
    module = importlib.import_module(f"aoc.{day}")
    print(f"Day {day}:")
    module.main()


if len(sys.argv) == 2:
    run_module(sys.argv[1])
else:
    # Find out which days are present
    r = re.compile("(?P<day>[0-9]+).py")
    days = []
    for file in os.listdir("aoc"):
        m = r.match(file)
        if m:
            days.append(m.group("day"))
    
    for day in sorted(map(lambda x: int(x), days)):
        run_module(day)
        print() 