

class Day(object):
    NUMBERS = ["zero", "one", "two", "three", "four",
               "five", "six", "seven", "eight", "nine"]

    def __init__(self, parser):
        self.parser = parser
        self.allow_words = False

    def number(self, l):
        if l[0].isnumeric():
            return int(l[0])

        if not self.allow_words:
            return

        for n, number in enumerate(self.NUMBERS):
            if l.startswith(number):
                return n

    def first_num(self, l):
        for i, char in enumerate(l):
            if n := self.number(l[i:]):
                return n

    def last_num(self, l):
        for i in range(len(l)-1, -1, -1):
            if n := self.number(l[i:]):
                return n

    def calculate(self):
        self.lines = self.parser.get_lines()

    def part_1(self):
        calibrations = (int(f"{self.first_num(l)}{self.last_num(l)}")
                        for l in self.lines if l)
        return sum(calibrations)

    def part_2(self):
        self.allow_words = True
        calibrations = (int(f"{self.first_num(l)}{self.last_num(l)}")
                        for l in self.lines if l)
        return sum(calibrations)

###############################################################################
# TESTING                                                                     #
###############################################################################


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


class ParserStub(object):
    def __init__(self, input):
        self.input = input

    def get_lines(self):
        return self.input.split("\n")


class Test(object):
    def __init__(self):
        pass

    def test_part_1(self):
        d = Day(ParserStub(LINES_P1))
        d.calculate()
        assert (d.part_1() == 142)

    def test_part_2(self):
        d = Day(ParserStub(LINES_P2))
        d.calculate()
        assert (d.part_2() == 281)
