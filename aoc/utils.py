#!/usr/bin/python3

import os
from collections import namedtuple

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


def add_coord(coord1, coord2):
    return tuple(x + y for x, y in zip(coord1, coord2))


def rotate(lines):
    return ["".join(line[i] for line in lines[::-1]) for i in range(len(lines))]


def flip(lines):
    return [line[::-1] for line in lines]