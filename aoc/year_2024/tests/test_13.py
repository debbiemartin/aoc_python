import pytest
from aoc.year_2024.days.day_13 import Day, Machine
from aoc.input_parser import ParserStub

LINES = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""


def test_machine_a():
    m = Machine(94, 34, 22, 67, 8400, 5400)
    assert m.min_tokens_offset(0) == 280


def test_machine_b():
    m = Machine(26, 66, 67, 21, 12748, 12176)
    assert m.min_tokens() == None


def test_machine_c():
    m = Machine(17, 86, 84, 37, 7870, 6450)
    assert m.min_tokens() == 200


def test_machine_d():
    m = Machine(69, 23, 27, 71, 18641, 10279)
    assert m.min_tokens() == None


def test_part_1():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.part_1() == 480)


def test_machine_a_offset():
    m = Machine(94, 34, 22, 67, 8400, 5400)
    assert m.min_tokens_offset() == None


def test_machine_b_offset():
    m = Machine(26, 66, 67, 21, 12748, 12176)
    assert m.min_tokens_offset() != None


def test_machine_c_offset():
    m = Machine(17, 86, 84, 37, 7870, 6450)
    assert m.min_tokens_offset() == None


def test_machine_d_offset():
    m = Machine(69, 23, 27, 71, 18641, 10279)
    assert m.min_tokens_offset() != None
