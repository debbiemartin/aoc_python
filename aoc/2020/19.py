from itertools import product

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def parse(self, lines):
        rules = {}
        expanded = set()

        for num, rule in [(int(line.split(":")[0]), line.split(":")[1]) for line in lines]:
            if "\"" in rule:
                rules[num] = [rule.strip(" ").strip("\"")]
                expanded.add(num)
            else:
                rules[num] = [tuple(map(lambda x: int(x), option.strip(" ").split(" ")))
                              for option in rule.split ("|")]

        return rules, expanded


    def matches_rules(self, test, index, rules):
        if (index == len(test)):
            return 0, index

        for rule in (rule for rule in rules if test[index:].startswith(rule)):
            count, newindex = self.matches_rules(test, index + len(rule), rules)
            return count + 1, newindex

        return 0, index

    def matches_rulelists(self, test, rules1, rules2):
        """
        Used in part 2 to match minimum 2 of 42 rules, then minimum 1 31 rule.
        """
        n, index = self.matches_rules(test, 0, rules1)
        m, index = self.matches_rules(test, index, rules2)
        if index != len(test) or m < 1 or n < (m + 1):
            return False

        return True

    def calculate(self):
        self.sections = self.parser.get_sections()
        self.rules, expanded = self.parse(self.sections[0].split("\n"))

        while len(expanded) != len(self.rules):
            for i, rule in [(i, rule) for (i, rule) in self.rules.items() if i not in expanded]:
                if all(x in expanded for subrule in rule for x in subrule if x != i):
                    self.rules[i] = [
                        "".join(i)
                        for subrule in rule
                        for i in product(*[self.rules[index] for index in subrule])
                    ]
                    expanded.add(i)

    def part_1(self):
        return len(set(self.rules[0]) & set(self.sections[1].split("\n")))

    def part_2(self):
        # New rules effectively match 42 n times and 31 m times - just cheat and
        # check for this rather than evaluating loops intelligently
        #import pdb; pdb.set_trace()
        return sum(1 for test in self.sections[1].split("\n") if self.matches_rulelists(test, self.rules[42], self.rules[31]))
