from collections import defaultdict
import itertools as it


class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
        self.connections = defaultdict(lambda: set())
        for l in self.parser.get_lines():
            self.connections[l[0:2]].add(l[3:5])
            self.connections[l[3:5]].add(l[0:2])

    def part_1(self):
        threes = set()
        for computer, conn_set in self.connections.items():
            # go in pairs through the set
            for a, b in it.combinations(conn_set, 2):
                if b in self.connections[a]:
                    threes.add(frozenset([a, b, computer]))

        return sum(1 for three in threes if any(t.startswith("t") for t in three))

    def get_largest_group(self, group, trials):
        # Find the first element which is connected to the whole group
        trial = None
        for i, t in enumerate(trials):
            if all(c in self.connections[t] for c in group):
                trial = i
                break

        if trial is None:
            return group

        # Try with and without the new trial
        set1 = self.get_largest_group(group, trials[trial+1:])
        groupcpy = group.copy()
        groupcpy.add(trials[trial])
        set2 = self.get_largest_group(groupcpy, trials[trial+1:])

        return set1 if len(set1) > len(set2) else set2

    def part_2(self):
        # find the largest group: walk out from each
        maxlen = 0
        for computer, conn_set in self.connections.items():
            group = self.get_largest_group(
                group=set([computer]), trials=list(conn_set))
            if len(group) > maxlen:
                maxlen, maxgroup = len(group), group

        maxgroup = list(maxgroup)
        maxgroup.sort()
        return str(",".join(maxgroup))
