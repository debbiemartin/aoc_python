#!/usr/bin/python3

from . import utils
from collections import namedtuple

def valid_part_1(p):
    count = p.password.count(p.char)
    return count >= p.first and count <= p.second

def valid_part_2(p):
    return (p.password[p.first - 1] == p.char) ^ (p.password[p.second - 1] == p.char)

def main():
    lines = utils.get_lines(2)
    
    Password = namedtuple('Password', ['first', 'second', 'char', 'password'])
    linetuples = [tuple(line.split(" ")) for line in lines]
    passwords = [
        Password(int(range.split("-")[0]), int(range.split("-")[1]), char.strip(":"), password) 
        for range, char, password in linetuples
    ]
        
    print("PART 1:")
    numvalid = sum(1 for p in passwords if valid_part_1(p))
    print(numvalid)
    
    print("PART 2:")
    numvalid = sum(1 for p in passwords if valid_part_2(p))
    print(numvalid)