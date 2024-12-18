import pytest
from aoc.year_2024.days.day_18 import Day
from aoc.input_parser import ParserStub

LINES = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""


def test_part_1():
    d = Day(ParserStub(LINES))
    d.size = 6
    d.num_bytes = 12
    d.calculate()
    assert (d.part_1() == 22)


def test_part_1():
    d = Day(ParserStub(LINES))
    d.size = 6
    d.num_bytes = 12
    d.calculate()
    assert (d.part_2() == "6,1")
