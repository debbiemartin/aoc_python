import pytest
from aoc.year_2023.days.day_1 import Day
from aoc.input_parser import ParserStub

LINES_P1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

LINES_P2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


def test_part_1():
    d = Day(ParserStub(LINES_P1))
    d.calculate()
    assert (d.part_1() == 142)


def test_part_2():
    d = Day(ParserStub(LINES_P2))
    d.calculate()
    assert (d.part_2() == 281)
