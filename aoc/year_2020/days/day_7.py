#!/usr/bin/python3

from .. import utils
import re
from collections import namedtuple


Edge = namedtuple("Edge", ["to", "weight", "parent"])

class Day(object):
    def __init__(self, parser):
        self.parser = parser
        self.graph = {}

    def calculate(self):
        """
        Parse the bag info into the global bag graph. This is a weighted
        undirected graph, however we do store the parent of each edge as an
        attribute. This pseudo-directed graph implementation allows us to be
        able to find neighbours in both directions.
        """
        lines = self.parser.get_lines()

        r = re.compile(r"^(?P<bagcol>[A-Za-z ]+) bags contain (?P<baglist>[0-9A-Za-z, ]+).$")
        rbag = re.compile(r"^(?P<num>[0-9]+) (?P<col>[A-Za-z ]+) bag[s]?$")
        for l in lines:
            m = r.match(l)
            assert(m is not None)
            if m.group("bagcol") not in self.graph:
                self.graph[m.group("bagcol")] = set()
            if m.group("baglist") == "no other bags":
                continue
            for bag in m.group("baglist").split(", "):
                mbag = rbag.match(bag)
                assert(mbag is not None)
                if mbag.group("col") not in self.graph:
                    self.graph[mbag.group("col")] = set()
                self.graph[mbag.group("col")].add(Edge(m.group("bagcol"), int(mbag.group("num")), False))
                self.graph[m.group("bagcol")].add(Edge(mbag.group("col"), int(mbag.group("num")), True))

    @utils.visited
    def count_parents(self, name):
        """
        Recursively count the number of bags which are parents to the specified
        bag. Track visited to ensure each bag counted maximum of once.
        """
        parents = [edge.to for edge in self.graph[name] if not edge.parent]

        count = sum(self.count_parents(p) for p in parents)

        return 1 + count # count self


    @utils.memoize
    def count_children_weighted(self, name):
        """
        Recursively count total number of bags contained within the specified bag
        i.e. total number of children, taking into account weight. Can be counted
        more than once so don't track which we've already processed.

        Uses children count cache for optimisation.
        """

        children = ((edge.to, edge.weight) for edge in self.graph[name] if edge.parent)
        count = sum(weight * (1 + self.count_children_weighted(c)) for c, weight in children)

        return count

    def part_1(self):
        return self.count_parents("shiny gold") - 1 # minus off the bag itself

    def part_2(self):
        return self.count_children_weighted("shiny gold")
