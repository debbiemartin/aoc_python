import pytest
from aoc.year_2024.days.day_21 import Day
from aoc.input_parser import ParserStub

LINES = """029A
980A
179A
456A
379A"""


def test_conversion():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.convert_numerical_to_directional("0", "A") == ["<A"])
    assert (d.convert_numerical_to_directional("2", "0") == ["^A"])
    assert (d.convert_numerical_to_directional("9", "2") == [">^^A", "^^>A"])
    assert (d.convert_numerical_to_directional("A", "9") == ["vvvA"])
    assert (d.convert_numerical_to_directional("3", "A") == ["^A"])
    assert (d.convert_numerical_to_directional("7", "3") == ["<<^^A", "^^<<A"])
    assert (d.convert_numerical_to_directional("9", "7") == [">>A"])
    assert (d.convert_numerical_to_directional("A", "9") == ["vvvA"])


def test_patterns():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.get_pattern_len("029A", 1) == 28)
    assert (d.get_pattern_len("029A", 2) == 68)
    assert (d.get_pattern_len("980A", 2) == 60)
    assert (d.get_pattern_len("179A", 2) == 68)
    assert (d.get_pattern_len("456A", 2) == 64)
    assert (d.get_pattern_len("379A", 1) == 28)
    assert (d.get_pattern_len("379A", 2) == 64)


def test_part_1():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.part_1() == 126384)


def test_part_2():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.part_2() == 154115708116294)
