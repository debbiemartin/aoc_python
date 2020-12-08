#!/usr/bin/python3

import re
from collections import namedtuple

G = {}
Edge = namedtuple("Edge", ["to", "weight", "parent"])

def parse_input():
    """
    Parse the bag info into the global bag graph. This is a weighted 
    undirected graph, however we do store the parent of each edge as an 
    attribute. This pseudo-directed graph implementation allows us to be 
    able to find neighbours in both directions. 
    """
    with open("7/input.txt", "r") as f:
        lines = f.read().split("\n")
    
    r = re.compile(r"^(?P<bagcol>[A-Za-z ]+) bags contain (?P<baglist>[0-9A-Za-z, ]+).$")
    rbag = re.compile(r"^(?P<num>[0-9]+) (?P<col>[A-Za-z ]+) bag[s]?$")
    for l in lines:
        m = r.match(l)
        assert(m is not None)
        if m.group("bagcol") not in G:
            G[m.group("bagcol")] = set()
        if m.group("baglist") == "no other bags":
            continue
        for bag in m.group("baglist").split(", "):
            mbag = rbag.match(bag)
            assert(mbag is not None)
            if mbag.group("col") not in G:
                G[mbag.group("col")] = set()
            G[mbag.group("col")].add(Edge(m.group("bagcol"), int(mbag.group("num")), False))
            G[m.group("bagcol")].add(Edge(mbag.group("col"), int(mbag.group("num")), True))

def count_parents(name, current_parents=None):
    """
    Recursively count the number of bags which are parents to the specified 
    bag. Add to the current_parents list to ensure each bag counted maximum of
    once. 
    """
    if not current_parents:
        current_parents = set()
    if name not in current_parents:
        current_parents.add(name)
        parents = (edge.to for edge in G[name] if not edge.parent)
        for p in parents: 
            count_parents(p, current_parents)
    return len(current_parents) - 1

def count_children_weighted(name, cache=None):
    """
    Recursively count total number of bags contained within the specified bag
    i.e. total number of children, taking into account weight. Can be counted
    more than once so don't track which we've already processed. 
    
    Uses children count cache for optimisation.
    """
    if not cache:
        cache = {}
    if name not in cache: 
        children = ((edge.to, edge.weight) for edge in G[name] if edge.parent)
        cache[name] = sum(weight * (1 + count_children_weighted(c)) for c, weight in children)

    return cache[name]

parse_input()

print("PART 1:")
print(count_parents("shiny gold"))

print("PART 2:")
print(count_children_weighted("shiny gold"))