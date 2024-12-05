#!/usr/bin/python3

import os
from collections import namedtuple


class Parser(object):
    def __init__(self, year, day):
        self.year = year
        self.day = day

    def get_numbers(self):
        with open(os.path.join("inputs", str(self.year), f"{self.day}.txt"), "r") as f:
            return [list(map(int, l.split())) for l in f.readlines()]

    def get_lines(self):
        with open(os.path.join("inputs", str(self.year), f"{self.day}.txt"), "r") as f:
            return list(filter(len, f.readlines()))

    def get_sections(self):
        with open(os.path.join("inputs", str(self.year), f"{self.day}.txt"), "r") as f:
            return f.read().split("\n\n")

    def get_sections_list(self):
        with open(os.path.join("inputs", str(self.year), f"{self.day}.txt"), "r") as f:
            return [s.strip("\n").split("\n") for s in f.read().split("\n\n")]


class ParserStub(object):
    def __init__(self, input):
        self.input = input

    def get_lines(self):
        return self.input.split("\n")

    def get_sections_list(self):
        return [s.strip("\n").split("\n") for s in self.input.split("\n\n")]
