import pytest
from aoc.year_2024.days.day_6 import Day
from aoc.input_parser import ParserStub

LINES = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


def test_part_1():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.part_1() == 41)


def test_part_2():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.part_2() == 6)
