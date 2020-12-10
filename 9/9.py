#!/usr/bin/python3

import itertools

PREAMBLE_LEN=25

def find_weakness(invalid):
    for i in range(invalid): 
        curr_sum = nums[i] 
      
        # try all subarrays starting at i
        for j in range(i + 1, invalid): 
            if curr_sum == nums[invalid]: 
                numsub = nums[i:j]
                return min(numsub) + max(numsub)
                  
            if curr_sum > nums[invalid] or j == invalid: 
                break
              
            curr_sum = curr_sum + nums[j]

# Tried doing this to avoid computing permutations of all PREAMBLE_LEN each 
# time but was actually slower... 
#
def find_invalid_index():
    subarr = nums[:PREAMBLE_LEN]
    sums_pairs = [
        sum(numvars) for numvars in 
        itertools.permutations(subarr, 2)
    ]
    
    for i in range(PREAMBLE_LEN, len(nums)):
        if nums[i] not in sums_pairs:
            return i

        # take the first PREAMBLE_LEN one of the pairs and add in i * each
        sums_pairs = sums_pairs[PREAMBLE_LEN:]
        subarr = subarr[1:]
        subarr.append(nums[i])
        for s in subarr:
            sums_pairs.append(s + nums[i])

with open("9/input.txt", "r") as f:
    nums = list(map(lambda x: int(x), f.read().split("\n")))

print("PART 1:")
invalid = find_invalid_index()
print(nums[invalid])

# find contiguous set which add to number
print("PART 2:") 
print(find_weakness(invalid))