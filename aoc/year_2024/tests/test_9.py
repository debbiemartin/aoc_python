import pytest
from aoc.year_2024.days.day_9 import Day
from aoc.input_parser import ParserStub

LINES = """2333133121414131402"""


def test_part_1():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.part_1() == 1928)


def test_part_2():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.part_2() == 2858)
