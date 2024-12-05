from collections import defaultdict
from functools import cmp_to_key


class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def rule_adhered(self, before, after, update):
        if not before in update or not after in update:
            return True
        return (update.index(before) < update.index(after))

    def calculate(self):
        self.rules = defaultdict(list)
        for r in self.parser.get_sections_list()[0]:
            before, after = tuple(r.split("|"))
            self.rules[before].append(after)

        # Read the pages into a hashmap of page: position.
        updates = (u.split(",") for u in self.parser.get_sections_list()[1])

        self.correct = []
        self.incorrect = []
        for u in updates:
            if all(self.rule_adhered(before, after, u) for before, rules in self.rules.items() for after in rules):
                self.correct.append(u)
            else:
                self.incorrect.append(u)

    def find_correct(self, update):
        def sorted_by(a, b):
            if b in self.rules[a]:
                return 1
            if a in self.rules[b]:
                return -1

        return sorted(update, key=cmp_to_key(sorted_by))

    def part_1(self):
        return sum(int(u[int((len(u)-1)/2)]) for u in self.correct)

    def part_2(self):
        score = 0
        for u in self.incorrect:
            correct = self.find_correct(u)
            score += int(correct[int((len(correct)-1)/2)])

        return score
