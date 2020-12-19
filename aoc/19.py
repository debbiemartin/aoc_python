from . import utils 
from itertools import product

def parse(lines):
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

def main():
    sections = utils.get_sections(19)
    rules, expanded = parse(sections[0].split("\n"))
    
    while len(expanded) != len(rules):
        for i, rule in [(i, rule) for (i, rule) in rules.items() if i not in expanded]:
            if all(i in expanded for subrule in rule for i in subrule):
                rules[i] = [
                    "".join(i)
                    for subrule in rule
                    for i in product(*[rules[index] for index in subrule])
                ]
                expanded.add(i)
    
    print("PART 1:")
    print(len(set(rules[0]) & set(sections[1].split("\n"))))
            
