from . import utils
import re
from collections import defaultdict

def parse(lines):
    global allergens, ingredients

    r = re.compile("^(?P<ingreds>.*) \(contains (?P<allergens>.*)\)$")
    allergens = {}
    ingredients = defaultdict(lambda: 0)
    for line in lines:
        m = r.match(line)
        assert(m)
        ingred_list = set(m.group("ingreds").split(" "))
        for a in m.group("allergens").split(", "):
            if a not in allergens:
                allergens[a] = ingred_list
            else:
                # take any out of the list that aren't in this food's allergens
                allergens[a] = allergens[a] & ingred_list
        
        for i in ingred_list:
            ingredients[i] += 1

def process_single_ingred(allergen):
    global allergens, ingredients

    ingredient = allergens[allergen] # this is a len-1 set
    for a, ingreds in ((a, ingreds) for (a, ingreds) in allergens.items() if a != allergen and len(ingreds) > 1):
        ingreds -= ingredient
        if len(ingreds) == 1:
            process_single_ingred(a)

def get_alphabetical():
    global allergens, ingredients

    # Any ingredient which could only be one allergen take it out of the others
    for a in (a for (a, ingreds) in allergens.items() for i in ingredients.keys() if len(ingreds) == 1):
        process_single_ingred(a)
    
    return ",".join(allergens[a].pop() for a in sorted(allergens.keys()))
    

def main():
    lines = utils.get_lines(21)
    
    global allergens, ingredients
    parse(lines)
        
    # Allergens dict does not have 1-1 mapping, however has the same number of 
    # ingredients as allergens, so can use it to find any non-allergenic 
    # ingredients
    print("PART 1:")
    print(sum(ingredients[i] for i in ingredients.keys() if not any(i in a for a in allergens.values())))
    
    # Now solve for 1-1 mapping 
    print("PART 2:")
    print(get_alphabetical())
    
    