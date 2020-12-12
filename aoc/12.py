#!/usr/bin/python3

from . import utils
import math


angle_dir = {
    0:   "N",
    90:  "E",
    180: "S",
    270: "W",   
}

instructions1 = {
    "N": lambda dir, pos, wp, val: (dir, utils.add_coord(pos, (0, val)), wp),
    "S": lambda dir, pos, wp, val: (dir, utils.add_coord(pos, (0, -val)), wp),
    "E": lambda dir, pos, wp, val: (dir, utils.add_coord(pos, (val, 0)), wp),
    "W": lambda dir, pos, wp, val: (dir, utils.add_coord(pos, (-val, 0)), wp),
    "F": lambda dir, pos, wp, val: instructions1[angle_dir[dir]](dir, pos, wp, val),
    "R": lambda dir, pos, wp, val: ((dir + val)%360, pos, wp),
    "L": lambda dir, pos, wp, val: ((dir - val)%360, pos, wp),
}

angle_pos_factor = {
    0:   lambda coord: (coord[0],   coord[1]),
    90:  lambda coord: (coord[1],  -coord[0]),
    180: lambda coord: (-coord[0], -coord[1]),
    270: lambda coord: (-coord[1],  coord[0])
} 

instructions2 = {
    "N": lambda dir, pos, wp, val: (dir, pos, utils.add_coord(wp, (0, val))),
    "S": lambda dir, pos, wp, val: (dir, pos, utils.add_coord(wp, (0, -val))),
    "E": lambda dir, pos, wp, val: (dir, pos, utils.add_coord(wp, (val, 0))),
    "W": lambda dir, pos, wp, val: (dir, pos, utils.add_coord(wp, (-val, 0))),
    "F": lambda dir, pos, wp, val: (dir, utils.add_coord(pos, (val * wp[0], val * wp[1])), wp),
    "R": lambda dir, pos, wp, val: (dir, pos, angle_pos_factor[val%360](wp)),
    "L": lambda dir, pos, wp, val: (dir, pos, angle_pos_factor[-val%360](wp)),
}

def do_instructions(lines, instructions):
    dir, pos, wp = 90, (0,0), (10,1)
    
    for line in lines:
        dir, pos, wp = instructions[line[0]](dir, pos, wp, int(line[1:]))
        #print(f"new dir {dir} pos {pos} wp {wp}") #debug
    
    return abs(pos[0]) + abs(pos[1])

def main():    
    lines = utils.get_lines(12)

    print("PART 1:")
    print(do_instructions(lines, instructions1)) 
    
    print("PART 2:")
    print(do_instructions(lines, instructions2))   
    
        