#!/usr/bin/python3

import os
from collections import namedtuple


class Parser(object):
    def __init__(self, year, day):
        self.year = year
        self.day = day

    def get_lines(self):
        with open(os.path.join("inputs", str(self.year), f"{self.day}.txt"), "r") as f:
            return list(filter(len, f.read().split("\n")))

    def get_sections(self):
        with open(os.path.join("inputs", str(self.year), f"{self.day}.txt"), "r") as f:
            return f.read().split("\n\n")

    def get_sections_list(self):
        with open(os.path.join("inputs", str(self.year), f"{self.day}.txt"), "r") as f:
            return [s.strip("\n").split("\n") for s in f.read().split("\n\n")]
