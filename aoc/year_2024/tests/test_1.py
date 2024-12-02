import pytest
from aoc.year_2024.days.day_1 import Day

LINES = """3   4
4   3
2   5
1   3
3   9
3   3"""


class ParserStub(object):
    def __init__(self, input):
        self.input = input

    def get_lines(self):
        return self.input.split("\n")


def test_part_1():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.part_1() == 11)


def test_part_2():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.part_2() == 31)
