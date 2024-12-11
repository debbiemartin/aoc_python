import pytest
from aoc.year_2024.days.day_11 import Day
from aoc.input_parser import ParserStub

LINES = """125 17"""


def test_part_1():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.part_1() == 55312)
