import pytest
from aoc.year_2024.days.day_3 import Day
from aoc.input_parser import ParserStub

LINES_P1 = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
LINES_P2 = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""


def test_part_1():
    d = Day(ParserStub(LINES_P1))
    d.calculate()
    assert (d.part_1() == 161)


def test_part_2():
    d = Day(ParserStub(LINES_P2))
    d.calculate()
    assert (d.part_2() == 48)
