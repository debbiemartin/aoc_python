import pytest
from aoc.year_2024.days.day_12 import Day
from aoc.input_parser import ParserStub

LINES_A = """AAAA
BBCD
BBCC
EEEC"""


def test_part_1_a():
    d = Day(ParserStub(LINES_A))
    d.calculate()
    assert (d.part_1() == 140)


LINES_B = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""


def test_part_1_b():
    d = Day(ParserStub(LINES_B))
    d.calculate()
    assert (d.part_1() == 772)


LINES_LARGE = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""


def test_part_1_c():
    d = Day(ParserStub(LINES_LARGE))
    d.calculate()
    assert (d.part_1() == 1930)


def test_part_2_a():
    d = Day(ParserStub(LINES_A))
    d.calculate()
    assert (d.part_2() == 80)


def test_part_2_b():
    d = Day(ParserStub(LINES_B))
    d.calculate()
    assert (d.part_2() == 436)


LINES_C = """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""


def test_part_2_c():
    d = Day(ParserStub(LINES_C))
    d.calculate()
    assert (d.part_2() == 236)


LINES_D = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""


def test_part_2_d():
    d = Day(ParserStub(LINES_D))
    d.calculate()
    assert (d.part_2() == 368)


def test_part_2_e():
    d = Day(ParserStub(LINES_LARGE))
    d.calculate()
    assert (d.part_2() == 1206)
