#!/usr/bin/python3

import re

class BoardingStringSyntaxError(Exception):
    def __init__(self, str):
        self.str = str

    def __str__(self):
        return f"String {self.str} for col or row is not of the correct format"

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    @staticmethod
    def get_index(poschar, negchar, str):
        # Sanitise the string
        r = re.compile(f"^[{poschar}{negchar}]+$")
        m = r.match(str)
        if not m:
            raise BoardingStringSyntaxError(str)

        return sum(1 << (len(str) - i - 1) for i in range(len(str))
                    if str[i] == poschar)

    def get_id(self, pass_str):
        row = self.get_index("B", "F", pass_str[:7])
        col = self.get_index("R", "L", pass_str[7:])
        return row * 8 + col

    def calculate(self):
        lines = self.parser.get_lines()

        self.ids = [self.get_id(line.strip("\n")) for line in lines]

    def part_1(self):
        # Get max ID for input list
        max_id = max(self.ids)
        return max_id

    def part_2(self):
        # Find the ID which is not present, but +-1 IDs are i.e. go between min + 1 and max
        id_set = set(self.ids)
        for i in range(min(self.ids), max(self.ids)):
            if i not in id_set:
                return i
