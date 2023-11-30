#!/usr/bin/python3

from collections import namedtuple

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
        lines = self.parser.get_lines()

        Password = namedtuple('Password', ['first', 'second', 'char', 'password'])
        linetuples = [tuple(line.split(" ")) for line in lines]
        self.passwords = [
            Password(int(range.split("-")[0]), int(range.split("-")[1]), char.strip(":"), password)
            for range, char, password in linetuples
        ]

    def valid_part_1(self, p):
        count = p.password.count(p.char)
        return count >= p.first and count <= p.second

    def part_1(self):
        numvalid = sum(1 for p in self.passwords if self.valid_part_1(p))
        return numvalid

    def valid_part_2(self, p):
        return (p.password[p.first - 1] == p.char) ^ (p.password[p.second - 1] == p.char)

    def part_2(self):
        numvalid = sum(1 for p in self.passwords if self.valid_part_2(p))
        return numvalid
