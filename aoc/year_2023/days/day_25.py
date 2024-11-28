from collections import defaultdict, deque
from itertools import combinations
import networkx


class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
        lines = self.parser.get_lines()

        self.wires = set()
        self.graph = networkx.DiGraph()
        for l in lines:
            from_conn = l.split(": ")[0]
            to_conns = l.split(": ")[1].split()
            self.wires.add(from_conn)
            for to_conn in to_conns:
                self.wires.add(to_conn)
                self.graph.add_edge(from_conn, to_conn, capacity=1.0)
                self.graph.add_edge(to_conn, from_conn, capacity=1.0)


    def part_1(self):
        wire_a = list(self.wires)[0]
        for wire_b in (x for x in self.wires if x != wire_a):
            cut_value, (left, right) = networkx.minimum_cut(self.graph, wire_a, wire_b)
            if cut_value == 3:
                return len(left) * len(right)

    def part_2(self):
        pass
