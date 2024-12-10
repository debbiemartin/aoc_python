import pytest
from aoc.year_2024.days.day_10 import Day
from aoc.input_parser import ParserStub

LINES_SINGLE = """0123
1234
8765
9876"""


def test_single():
    d = Day(ParserStub(LINES_SINGLE))
    d.calculate()
    assert (d.part_1() == 1)


LINES = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""


def test_part_1():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.part_1() == 36)


def test_part_2():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.part_2() == 81)
