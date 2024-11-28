import re
from collections import defaultdict

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def parse(self, lines):
        r = re.compile("^(?P<ingreds>.*) \(contains (?P<allergens>.*)\)$")
        self.allergens = {}
        self.ingredients = defaultdict(lambda: 0)
        for line in lines:
            m = r.match(line)
            assert(m)
            ingred_list = set(m.group("ingreds").split(" "))
            for a in m.group("allergens").split(", "):
                if a not in self.allergens:
                    self.allergens[a] = ingred_list
                else:
                    # take any out of the list that aren't in this food's allergens
                    self.allergens[a] = self.allergens[a] & ingred_list

            for i in ingred_list:
                self.ingredients[i] += 1

    def process_single_ingred(self, allergen):
        ingredient = self.allergens[allergen] # this is a len-1 set
        for a, ingreds in ((a, ingreds) for (a, ingreds) in self.allergens.items() if a != allergen and len(ingreds) > 1):
            ingreds -= ingredient
            if len(ingreds) == 1:
                self.process_single_ingred(a)

    def get_alphabetical(self):
        # Any ingredient which could only be one allergen take it out of the others
        for a in (a for (a, ingreds) in self.allergens.items() for i in self.ingredients.keys() if len(ingreds) == 1):
            self.process_single_ingred(a)

        return ",".join(self.allergens[a].pop() for a in sorted(self.allergens.keys()))


    def calculate(self):
        lines = self.parser.get_lines()

        self.parse(lines)

    def part_1(self):
        # Allergens dict does not have 1-1 mapping, however has the same number of
        # ingredients as allergens, so can use it to find any non-allergenic
        # ingredients
        return sum(self.ingredients[i] for i in self.ingredients.keys() if not any(i in a for a in self.allergens.values()))

    def part_2(self):
        # Now solve for 1-1 mapping
        return self.get_alphabetical()


