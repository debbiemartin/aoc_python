from . import utils
import re
from functools import reduce 


class FieldMap(object):
    def __init__(self, rulecount, fieldcount):
        # initialize array
        self.map = [[i for i in range(fieldcount)] for j in range(rulecount)]
        self.solved = [None for i in range(rulecount)]
    
    def _add_solved(self, rulenum, fieldnum):
        assert(not fieldnum in self.solved)
        self.solved[rulenum] = fieldnum
    
    def _check_rulenum(self, rulenum):
        if len(self.map[rulenum]) != 1 or self.solved[rulenum] != None:
            return
        
        fieldnum = self.map[rulenum][0]
        self._add_solved(rulenum, fieldnum)

        # Remove from rulemap
        for i in range(len(self.map)):
            if fieldnum in self.map[i]:
                self.remove(i, fieldnum)
    
    def _check_fieldnum(self, fieldnum):
        # Check whether only one rule has this number - if so, remove all the
        # others from it 
        if (sum((1 if fieldnum in rule else 0) for rule in self.map) != 1 or
            fieldnum in self.solved): 
            return
            
        for i, rule in enumerate(self.map):
            if fieldnum in rule:
                for f in (f for f in rule if f != fieldnum):
                    self.remove(i, f)
    
    def remove(self, rulenum, fieldnum):
        if not fieldnum in self.map[rulenum]:
            return

        self.map[rulenum].remove(fieldnum)
        
        # If there is only one left, remove it as a possibility for other fields
        self._check_rulenum(rulenum)
        self._check_fieldnum(fieldnum)
    
    def is_solved(self):
        return not any(f is None for f in self.solved)
        
    def get(self, rulenum):
        return self.solved[rulenum]

def validate_field(rule, field):
    valid = ((field >= rule[0] and field <= rule[1]) or 
             (field >= rule[2] and field <= rule[3]))

    return valid

def validate_ticket(rules, ticket):   
    return sum(f for f in ticket if not any(validate_field(r, f) for r in rules))

def main():
    sections = utils.get_sections(16)
    
    rules = []
    r = re.compile("^[a-z ]+: ([0-9]+)\-([0-9]+) or ([0-9]+)\-([0-9]+)$")
    for line in sections[0].split("\n"):
        m = r.match(line)
        rules.append(list(map(lambda x: int(x), m.groups())))
    
    ticketstrs = (str for str in sections[2].split("\n")[1:])
    tickets = [list(map(lambda x: int(x), ticket.split(","))) for ticket in ticketstrs]
    my_ticket = list(map(lambda x: int(x), sections[1].split("\n")[1].split(",")))
    
    print("PART 1:")
    print(sum(validate_ticket(rules, t) for t in tickets))
    
    print("PART 2:")
    
    valid_tickets = [t for t in tickets if validate_ticket(rules, t) == 0]

    field_map = FieldMap(len(rules), len(my_ticket))

    for ticket in valid_tickets:
        for i, f in enumerate(ticket):
            for j, r in enumerate(rules):
                if not validate_field(r, f):
                    field_map.remove(j, i) #@@@ nesting             
    dep_fields = (my_ticket[field_map.get(i)] for i, rule in enumerate(rules) if i < 6)
    print(reduce(lambda a, b: a * b, dep_fields))