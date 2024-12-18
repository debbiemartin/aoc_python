import pytest
from aoc.year_2024.days.day_17 import Day, Machine
from aoc.input_parser import ParserStub

LINES = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""


def test_machine_a():
    m = Machine([2, 6], {"A": 0, "B": 0, "C": 9})
    m.run_program()
    assert m.B == 1


def test_machine_b():
    m = Machine([5, 0, 5, 1, 5, 4], {"A": 10, "B": 0, "C": 0})
    m.run_program()
    assert m.out == [0, 1, 2]


def test_machine_c():
    m = Machine([0, 1, 5, 4, 3, 0], {"A": 2024, "B": 0, "C": 0})
    m.run_program()
    assert m.out == [4, 2, 5, 6, 7, 7, 7, 7, 3, 1, 0]
    assert m.A == 0


def test_machine_d():
    m = Machine([1, 7], {"A": 0, "B": 29, "C": 0})
    m.run_program()
    assert m.B == 26


def test_machine_e():
    m = Machine([4, 0], {"A": 0, "B": 2024, "C": 43690})
    m.run_program()
    assert m.B == 44354


def test_part_1():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.part_1() == "4,6,3,5,6,3,5,2,1,0")


LINES_B = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""


def test_part_2():
    d = Day(ParserStub(LINES_B))
    d.calculate()
    assert (d.part_2() == 117440)
