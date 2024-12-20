import pytest
from aoc.year_2024.days.day_20 import Day
from aoc.input_parser import ParserStub

LINES = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""


def test_part_1():
    d = Day(ParserStub(LINES))
    d.calculate()
    d.part_1()
    assert d.cheats == {
        2: 14, 4: 14, 6: 2, 8: 4, 10: 2,
        12: 3, 20: 1, 36: 1, 38: 1, 40: 1, 64: 1
    }


def test_part_2():
    d = Day(ParserStub(LINES))
    d.calculate()
    d.part_2()
    assert d.cheats[50] == 32
    assert d.cheats[52] == 31
    assert d.cheats[54] == 29
    assert d.cheats[56] == 39
    assert d.cheats[58] == 25
    assert d.cheats[60] == 23
    assert d.cheats[62] == 20
    assert d.cheats[64] == 19
    assert d.cheats[66] == 12
    assert d.cheats[68] == 14
    assert d.cheats[70] == 12
    assert d.cheats[72] == 22
    assert d.cheats[74] == 4
    assert d.cheats[76] == 3
