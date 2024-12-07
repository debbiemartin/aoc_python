from enum import Enum


class Operator(Enum):
    add = 0
    multiply = 1
    concatenate = 2


class Day(object):
    def __init__(self, parser):
        self.parser = parser
        self.operators = (Operator.add, Operator.multiply)

    def calculate(self):
        lines = self.parser.get_lines()
        self.tests = {
            int(l.split(":")[0]):
            [int(x) for x in l.split(":")[1].split()]
            for l in lines
        }

    def test(self, test_val, current, remaining, operator):
        if current > test_val:
            return False

        if operator == Operator.add:
            current += remaining[0]
        elif operator == Operator.multiply:
            current *= remaining[0]
        elif operator == Operator.concatenate:
            current = int(str(current)+str(remaining[0]))
        else:
            assert (False)

        if len(remaining) == 1:
            return current == test_val

        return any(
            self.test(test_val, current, remaining[1:], operator)
            for operator in self.operators
        )

    def part_1(self):
        return sum(
            test_val
            for test_val, numbers in self.tests.items()
            if self.test(test_val, 0, numbers, Operator.add)
        )

    def part_2(self):
        self.operators = (Operator.add, Operator.multiply,
                          Operator.concatenate)
        return sum(
            test_val
            for test_val, numbers in self.tests.items()
            if self.test(test_val, 0, numbers, Operator.add)
        )
