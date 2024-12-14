import pytest
from aoc.year_2024.days.day_14 import Day
from aoc.input_parser import ParserStub

LINES = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""


def test_part_1():
    d = Day(ParserStub(LINES))
    d.xmax = 11
    d.ymax = 7
    d.calculate()
    assert (d.part_1() == 12)


def test_part_2():
    d = Day(ParserStub(LINES))
    d.xmax = 11
    d.ymax = 7
    d.calculate()
    d.part_2()
