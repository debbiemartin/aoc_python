import pytest
from aoc.year_2024.days.day_22 import Day
from aoc.input_parser import ParserStub

LINES = """1
10
100
2024"""


def test_secret():
    d = Day(ParserStub(LINES))
    assert (d.secret(123) == 15887950)
    assert (d.secret(15887950) == 16495136)
    assert (d.secret(16495136) == 527345)
    assert (d.secret(527345) == 704524)
    assert (d.secret(704524) == 1553684)
    assert (d.secret(1553684) == 12683156)
    assert (d.secret(12683156) == 11100544)
    assert (d.secret(11100544) == 12249484)
    assert (d.secret(12249484) == 7753432)
    assert (d.secret(7753432) == 5908254)


def test_part_1():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.part_1() == 37327623)


LINES_B = """1
2
3
2024"""


def test_part_2():
    d = Day(ParserStub(LINES_B))
    d.calculate()
    assert (d.part_2() == 23)
