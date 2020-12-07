#!/usr/bin/python3

import re
import networkx as nx

G = nx.Graph()

def parse_input():
    """
    Parse the bag info into the "bags" global var. The key is the bag name, 
    and entry is a list of BagChild tuples. 
    
    IMPORTANT: this dict is in the opposite direction to that of the input i.e.
    it is information for each bag of the number of its own bag the PARENT BAG
    is able to contain.
    """
    with open("7/input.txt", "r") as f:
        lines = f.read().split("\n")
    
    r = re.compile(r"^(?P<bagcol>[A-Za-z ]+) bags contain (?P<baglist>[0-9A-Za-z, ]+).$")
    rbag = re.compile(r"^(?P<num>[0-9]+) (?P<col>[A-Za-z ]+) bag[s]?$")
    for l in lines:
        m = r.match(l)
        assert(m is not None)
        G.add_node(m.group("bagcol"))
        if m.group("baglist") == "no other bags":
            continue
        for bag in m.group("baglist").split(", "):
            mbag = rbag.match(bag)
            assert(mbag is not None)
            G.add_node(mbag.group("col"))
            # parent attribute is bit of a hack to make a pseudo-digraph but be 
            # able to use neighbours fn both ways to count both parents and 
            # children            
            G.add_edge(m.group("bagcol"), mbag.group("col"), 
                       weight=int(mbag.group("num")), parent=m.group("bagcol"))

def count_parents(name, current_parents=list()):
    """
    Recursively count the number of bags which are parents to the specified 
    bag. Add to the current_parents list to ensure each bag counted maximum of
    once. 
    """
    if name not in current_parents:
        current_parents.append(name)
        parents = [n for n in G.neighbors(name) if G.edges[name, n]["parent"] == n]
        for p in parents: 
            count_parents(p, current_parents)
    return len(current_parents) - 1 # the minus one is for the child in question

def count_children_weighted(name, cache=dict()):
    """
    Recursively count total number of bags contained within the specified bag
    i.e. total number of children, taking into account weight. Can be counted
    more than once so don't track which we've already processed. 
    
    Uses children count cache for optimisation.
    """
    if name not in cache: 
        children = [(n, G.edges[name, n]["weight"]) for n in G.neighbors(name) if G.edges[name, n]["parent"] == name]
        cache[name] = sum(weight * (1 + count_children_weighted(c)) for c, weight in children)

    return cache[name]

parse_input()

print("PART 1:")
print(count_parents("shiny gold"))

print("PART 2:")
print(count_children_weighted("shiny gold"))
    