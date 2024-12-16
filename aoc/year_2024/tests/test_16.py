import pytest
from aoc.year_2024.days.day_16 import Day
from aoc.input_parser import ParserStub

LINES_A = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""


def test_part_1_a():
    d = Day(ParserStub(LINES_A))
    d.calculate()
    assert (d.part_1() == 7036)


LINES_B = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""


def test_part_1_b():
    d = Day(ParserStub(LINES_B))
    d.calculate()
    assert (d.part_1() == 11048)


def test_part_2_a():
    d = Day(ParserStub(LINES_A))
    d.calculate()
    assert (d.part_2() == 45)


def test_part_2_b():
    d = Day(ParserStub(LINES_B))
    d.calculate()
    assert (d.part_2() == 64)
