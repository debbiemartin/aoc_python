#!/usr/bin/python3

from functools import reduce


class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def find_total(self, reduce_fn):
        """
        Find total qualifying fields over all groups in filetxt.
           reduce_fn - Used to reduce the list of strings for each group.
        """
        lettersets = [reduce(reduce_fn, group.split("\n")) for group in self.sections]
        return sum(len(l) for l in lettersets)

    def calculate(self):
        self.sections = self.parser.get_sections()

    def part_1(self):
        return self.find_total(lambda a, b: set(a) | set(b))

    def part_2(self):
        return self.find_total(lambda a, b: set(a) & set(b))
