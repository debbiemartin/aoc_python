import numpy

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def get_next_workflow(self, part, rules):
        for rule in rules:
            if not rule[0]:
                return rule[1]
            val = part[rule[0][0]]
            comp = rule[0][1]
            comp_val = int(rule[0][2:])
            if comp == "<":
                if val < comp_val:
                    return rule[1]
            elif comp == ">":
                if val > comp_val:
                    return rule[1]
            else:
                print(comp)
                assert(False)

    def parse_maps(self, lines):
        maps = {}
        def parse_rule(rule):
            if not ":" in rule:
                return (None, rule)
            else:
                return (rule.split(":")[0], rule.split(":")[1])

        for l in lines:
            workflow =  l.split("{")[0]
            rules = l.split("{")[1].strip("}").split(",")
            rules = list(map(parse_rule, rules))
            maps[workflow] = rules
        return maps

    def calculate(self):
        sections = self.parser.get_sections_list()
        self.maps = self.parse_maps(sections[0])
        self.parts = [{x.split("=")[0]: int(x.split("=")[1]) for x in l.strip("{}").split(",")} for l in sections[1]]

    def part_1(self):
        accepted = 0
        for p in self.parts:
            workflow = "in"
            while workflow not in ("A", "R"):
                workflow = self.get_next_workflow(p, self.maps[workflow])
            if workflow == "A":
                accepted += sum(p.values())

        return accepted

    def split_workflow(self, workflow, ranges):
        if workflow == "A":
            self.accepted += numpy.prod([sum((a[1]-a[0]+1) for a in r) for r in ranges.values()])
            return
        if workflow == "R":
            return

        rules = self.maps[workflow]

        # process rules and get new workflows to process
        for rule in rules:
            if not rule[0]:
                self.split_workflow(rule[1], ranges)
                return

            part = rule[0][0]
            comp = rule[0][1]
            comp_val = int(rule[0][2:])
            comp_workflow = rule[1]
            if comp == "<":
                r_below = ranges.copy()
                r_below[part] = [(r[0], min(r[1], comp_val-1)) for r in ranges[part] if r[0] < comp_val]
                self.split_workflow(comp_workflow, r_below)
                ranges[part] = [(max(comp_val, r[0]), r[1]) for r in ranges[part] if r[1] >= comp_val]

            elif comp == ">":
                r_above = ranges.copy()
                r_above[part] = [(max(comp_val+1, r[0]), r[1]) for r in ranges[part] if r[1] > comp_val]
                self.split_workflow(comp_workflow, r_above)
                ranges[part] = [(r[0], min(comp_val, r[1])) for r in ranges[part] if r[0] <= comp_val]
            else:
                print(comp)
                assert(False)


    def part_2(self):
        self.accepted = 0

        self.split_workflow("in", ranges={char:[(1,4000)] for char in "xmas"})

        return self.accepted
