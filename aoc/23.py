import copy 

start="643719258"
mod = 1

def move(current, cups): 
    # work out which 3 cups we are moving 
    global mod
    picked = [cups[(current + 1 + i)%mod] for i in range(3)]
            
    # get the destination - current - 1 until we get to one in the remaining 
    # pack, remembering to wrap back around to 9.
    dest = cups[current]
    while True:
        dest = (dest-2)%mod + 1
        if dest not in picked:
            break
    
    # shuffle the array to be able to fit the cups in at dest
    dest_index = cups.index(dest)
    if dest_index > current:
        for i in range(dest_index - current - 3):
            cups[(current + 1 + i)%mod] = cups[(current + 4 + i)%mod]
        for i in range(3):
            cups[(dest_index - 2 + i)%mod] = picked[i]
        current = (current+1)%mod
    else:
        # dest_index < current
        for i in range(current - dest_index - 1, -1, -1):
            cups[(dest_index + 4 + i)%mod] = cups[(dest_index + 1 + i)%mod]
        for i in range(3):
            cups[(dest_index + 1 + i)%mod] = picked[i]
        current = (current+4)%mod
   
    return current, cups

def do_n_moves(cups, n):
    current = 0
    global mod
    mod = len(cups)
    
    for i in range(n):
        print(f"doing move {i}")
        current, cups = move(current, cups)
    
    return cups

def hundred_moves(cups):
    cups = copy.deepcopy(cups)
    
    cups = do_n_moves(cups, 100)
 
    index1 = cups.index(1)
    return "".join(str(cups[(index1 + i) % len(cups)]) for i in range(1, len(cups)))

def million_moves(cups):
    cups = copy.deepcopy(cups) + [10 + i for i in range(999990)]
    
    cups = do_n_moves(cups, 10000000)
    
    return  cups[(cups.index(1) + 1) % len(cups)] * cups[(cups.index(1) + 2) % len(cups)]

def main():
    cups = list(map(lambda x: int(x), start))   
        
    print("PART 1:")
    print(hundred_moves(cups))
    
    print("PART 2:")
    #print(million_moves(cups))
    
