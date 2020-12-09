#!/usr/bin/python3

import itertools

def find_weakness(invalid):
    for i in range(invalid): 
        curr_sum = nums[i] 
      
        # try all subarrays starting at i
        j = i + 1
        while j <= invalid: 
            if curr_sum == nums[invalid]: 
                numsub = nums[i:j]
                return min(numsub) + max(numsub)
                  
            if curr_sum > nums[invalid] or j == invalid: 
                break
              
            curr_sum = curr_sum + nums[j] 
            j += 1

PREAMBLE_LEN=25

with open("9/input.txt", "r") as f:
    nums = list(map(lambda x: int(x), f.read().split("\n")))

print("PART 1:")
for i in range(PREAMBLE_LEN, len(nums)):
    sums_pairs = [sum(numvars) for numvars in itertools.permutations(nums[i-PREAMBLE_LEN:i], 2)] #@@@ better way to do this
    if nums[i] not in sums_pairs:
        invalid = i
        break
print(nums[invalid])

# find contiguous set which add to number
print("PART 2:") 
print(find_weakness(invalid))