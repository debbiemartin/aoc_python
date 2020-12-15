from . import utils

def main():
    last_occ = {}
    
    starts = utils.get_lines(15)[0].split(",")
    
    for index, start in enumerate(starts[:-1]):
        last_occ[int(start)] = index + 1
       
    # Don't put the last spoken num in the last occurrences array so we can 
    # compute the next number
    lastnum, lastindex = int(starts[-1]), len(starts)
    
    while True:
        newnum = (0 if lastnum not in last_occ 
                    else (lastindex - last_occ[lastnum]))
        
        last_occ[lastnum] = lastindex
        
        lastnum = newnum
        lastindex += 1
       
        if lastindex == 2020:
            print("PART 1:")
            print(lastnum)
        elif lastindex == 30000000:
            print("PART 2:")
            print(lastnum)
            break