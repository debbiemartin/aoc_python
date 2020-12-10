#!/usr/bin/python3

import os

def get_lines(day):
    with open(os.path.join("inputs", f"{day}.txt"), "r") as f:
        return f.read().split("\n")

def get_sections(day):
    with open(os.path.join("inputs", f"{day}.txt"), "r") as f:
        return f.read().split("\n\n")
        
def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func

def visited(func):
    visited = set()

    def visited_func(*args):
        if args in visited:
            return 0
        visited.add(args)
        result = func(*args)
        return result

    return visited_func
    