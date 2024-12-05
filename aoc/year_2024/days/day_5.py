from collections import defaultdict


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
        correct = []
        for u in update:
            for i, c in enumerate(correct):
                if c in self.rules[u]:
                    correct.insert(i, u)
                    break
            else:
                correct.append(u)

        return correct

    def part_1(self):
        return sum(int(u[int((len(u)-1)/2)]) for u in self.correct)

    def part_2(self):
        score = 0
        for u in self.incorrect:
            correct = self.find_correct(u)
            score += int(correct[int((len(correct)-1)/2)])

        return score
