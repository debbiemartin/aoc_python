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


def matches_rules(test, index, rules):
    if (index == len(test)):
        return 0, index
    
    for rule in (rule for rule in rules if test[index:].startswith(rule)):
        count, newindex = matches_rules(test, index + len(rule), rules)
        return count + 1, newindex
    
    return 0, index
   
def matches_rulelists(test, rules1, rules2):
    """
    Used in part 2 to match minimum 2 of 42 rules, then minimum 1 31 rule. 
    """
    n, index = matches_rules(test, 0, rules1)
    m, index = matches_rules(test, index, rules2)
    if index != len(test) or m < 1 or n < (m + 1):
        return False
    
    return True

def main():
    sections = utils.get_sections(19)
    rules, expanded = parse(sections[0].split("\n"))
    
    while len(expanded) != len(rules):
        for i, rule in [(i, rule) for (i, rule) in rules.items() if i not in expanded]:
            if all(x in expanded for subrule in rule for x in subrule if x != i):
                rules[i] = [
                    "".join(i)
                    for subrule in rule
                    for i in product(*[rules[index] for index in subrule])
                ]
                expanded.add(i)
    
    print("PART 1:")
    print(len(set(rules[0]) & set(sections[1].split("\n"))))
    
    print("PART 2:")
    # New rules effectively match 42 n times and 31 m times - just cheat and
    # check for this rather than evaluating loops intelligently
    #import pdb; pdb.set_trace()
    print(sum(1 for test in sections[1].split("\n") if matches_rulelists(test, rules[42], rules[31])))
                                
            