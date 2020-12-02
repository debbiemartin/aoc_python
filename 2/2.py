#!/usr/bin/python3

from collections import namedtuple

def valid_part_1(p):
    count = p.password.count(p.char)
    return count >= p.first and count <= p.second

def valid_part_2(p):
    return (p.password[p.first - 1] == p.char) ^ (p.password[p.second - 1] == p.char)

with open("2/input.txt") as f:
    lines = f.readlines()

Password = namedtuple('Password', ['first', 'second', 'char', 'password'])
linetuples = [tuple(line.strip("\n").split(" ")) for line in lines]
passwords = [Password(int(range.split("-")[0]), int(range.split("-")[1]), char.strip(":"), password) for range, char, password in linetuples]
    
print("PART 1:")
numvalid = sum(1 for p in passwords if valid_part_1(p))
print(f"Number of valid passwords found: {numvalid}")

print("PART 2:")
numvalid = sum(1 for p in passwords if valid_part_2(p))
print(f"Number of valid passwords found: {numvalid}")

    
