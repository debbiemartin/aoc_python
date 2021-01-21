from collections import defaultdict
import numpy as np

start="643719258"
mod = 1

def move(current, nexts):
    # want to move the three cups after current
    next = current
    picked = []
    for _ in range(3):
        next = nexts[next]
        picked.append(next)
    
    # move current to point to the last picked's next
    nexts[current] = nexts[picked[2]]

    # work out dest
    dest = current
    global mod
    while True:
        dest = (dest-2)%mod + 1
        if dest not in picked:
            break
     
    # move dest to point to picked[0] and 
    nexts[picked[2]] = nexts[dest]
    nexts[dest] = picked[0]
    
    current = nexts[current]
    
    return current, nexts

def do_n_moves(nexts, current, n):   
    for i in range(n):
        current, nexts = move(current, nexts)
    
    return nexts

def hundred_moves(cups):
    global mod
    mod = 9
    nexts = {cups[i]: cups[(i + 1)%9] for i in range(9)}
       
    nexts = do_n_moves(nexts, cups[0], 100)
    
    # Make the string of the nexts circularly from 1 non-inclusive
    ret = ""
    curr = 1
    while True:
        curr = nexts[curr]
        if curr == 1:
            break
        ret += str(curr)   
    
    return ret

def tenmillion_moves(cups):
    global mod
    mod = 1000000
    
    # Make the nexts array by padding up to a million
    nexts = [None] * (mod + 1)
    for i in range(len(cups)-1):
        nexts[cups[i]] = cups[i+1]
    nexts[cups[-1]] = len(cups) + 1    

    for i in range(len(cups) + 1, mod):
        nexts[i] = i+1
    nexts[mod] = cups[0]
        
    nexts = do_n_moves(np.array(nexts), cups[0], 10000000)
        
    return nexts[1] * nexts[nexts[1]]

def main():
    cups = list(map(lambda x: int(x), start))   
        
    print("PART 1:")
    print(hundred_moves(cups))
    
    print("PART 2:")
    print(tenmillion_moves(cups))