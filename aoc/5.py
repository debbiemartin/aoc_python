#!/usr/bin/python3

from . import utils
import re

class BoardingStringSyntaxError(Exception):
    def __init__(self, str):
        self.str = str
    
    def __str__(self):
        return f"String {self.str} for col or row is not of the correct format"

def get_index(poschar, negchar, str):
    # Sanitise the string
    r = re.compile(f"^[{poschar}{negchar}]+$")
    m = r.match(str)
    if not m:
        raise BoardingStringSyntaxError(str)

    return sum(1 << (len(str) - i - 1) for i in range(len(str)) 
                if str[i] == poschar)

def get_id(pass_str):
    row = get_index("B", "F", pass_str[:7])
    col = get_index("R", "L", pass_str[7:])
    return row * 8 + col

def main():
    lines = utils.get_lines(5)
    
    ids = [get_id(line.strip("\n")) for line in lines]
    
    print("PART 1:")
    # Get max ID for input list
    max_id = max(ids)
    print(max_id)
    
    print("PART 2:")
    # Find the ID which is not present, but +-1 IDs are i.e. go between min + 1 and max
    for i in range(min(ids), max_id):
        if i not in list(ids):
            print(i)
            break