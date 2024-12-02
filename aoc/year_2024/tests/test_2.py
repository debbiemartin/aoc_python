import pytest
from aoc.year_2024.days.day_2 import Day
from aoc.input_parser import ParserStub

LINES = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


def test_safe():
    safe = [(0, True), (1, False), (2, False),
            (3, False), (4, False), (5, True)]

    d = Day(ParserStub(LINES))
    for l, s in safe:
        assert (d.is_safe(d.lines[l]) == s)


def test_part_1():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.part_1() == 2)


def test_safe_tolerate():
    safe = [(0, True), (1, False), (2, False),
            (3, True), (4, True), (5, True)]

    d = Day(ParserStub(LINES))
    for l, s in safe:
        print(l, s)
        assert (d.is_safe(d.lines[l], True) == s)


def test_part_2():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.part_2() == 4)
