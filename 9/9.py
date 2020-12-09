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
# def find_invalid_index():
#    pairs = [[nums[pair[0]], nums[pair[1]]] for pair in itertools.permutations(range(0,PREAMBLE_LEN), 2)]
#    for i in range(PREAMBLE_LEN, len(nums)):
#        if nums[i] not in set(map(lambda x: sum(x), pairs)):
#            return i
#
#        # take the i - PREAMBLE_LEN one out of the pairs and add in i
#        # NOTE: this assumes no repeats in subarray
#        for pair in pairs:
#            if nums[i - PREAMBLE_LEN] in pair:
#                pair.remove(nums[i - PREAMBLE_LEN])
#                pair.append(nums[i])

def find_invalid_index():
    for i in range(PREAMBLE_LEN, len(nums)):
        sums_pairs = (
            sum(numvars) for numvars in 
            itertools.permutations(nums[i - PREAMBLE_LEN:i], 2)
        )
 
        if nums[i] not in sums_pairs:
            return i


with open("9/input.txt", "r") as f:
    nums = list(map(lambda x: int(x), f.read().split("\n")))

print("PART 1:")
invalid = find_invalid_index()
print(nums[invalid])

# find contiguous set which add to number
print("PART 2:") 
print(find_weakness(invalid))