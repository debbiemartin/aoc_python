import pytest
from aoc.year_2024.days.day_8 import Day
from aoc.input_parser import ParserStub

LINES = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""


def test_part_1():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.part_1() == 14)


def test_part_2():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.part_2() == 34)
