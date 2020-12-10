#!/usr/bin/python3
from collections import defaultdict

def count_hops():
    counts = defaultdict(lambda: 0)
    
    # add diff between 0 for charging outlet
    counts[adapters[0]] = 1
    # add counts for each of the adapters:
    for i in range(len(adapters) - 1):
        counts[adapters[i + 1] - adapters[i]] += 1
    # add count for device (3 higher than highest adapter)
    counts[3] += 1
    
    return counts[1] * counts[3]
    
def count_paths(start):
    if start == adapters[-1]:
        # 1 possible hop to device
        return 1

    if start not in cache:
        cache[start] = sum(
            count_paths(start + hop) 
            for hop in range(1, 4) 
            if start + hop in adapters
        )
    
    return cache[start]
    
with open("10/input.txt", "r") as f:
    adapters = sorted(map(lambda x: int(x), f.read().split("\n")))

print("PART 1:")
print(count_hops())

print("PART 2:")
cache = {}
print(count_paths(0))

