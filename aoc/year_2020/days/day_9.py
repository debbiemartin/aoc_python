#!/usr/bin/python3

import itertools

class Day(object):
    PREAMBLE_LEN=25
    def __init__(self, parser):
        self.parser = parser

    def find_weakness(self, invalid):
        for i in range(invalid):
            curr_sum = self.nums[i]

            # try all subarrays starting at i
            for j in range(i + 1, invalid):
                if curr_sum == self.nums[invalid]:
                    numsub = self.nums[i:j]
                    return min(numsub) + max(numsub)

                if curr_sum > self.nums[invalid] or j == invalid:
                    break

                curr_sum = curr_sum + self.nums[j]

    def find_invalid_index(self):
        subarr = self.nums[:self.PREAMBLE_LEN]
        sums_pairs = [
            sum(numvars) for numvars in
            itertools.permutations(subarr, 2)
        ]

        for i in range(self.PREAMBLE_LEN, len(self.nums)):
            if self.nums[i] not in sums_pairs:
                return i

            # take the first PREAMBLE_LEN one of the pairs and add in i * each elem
            # of the new subarray. This avoids counting the
            # (PREAMBLE_LEN * PREAMBLE_LEN - 1) perms each time.
            sums_pairs = sums_pairs[self.PREAMBLE_LEN:]
            subarr = subarr[1:]
            subarr.append(self.nums[i])
            for s in subarr:
                sums_pairs.append(s + self.nums[i])


    def calculate(self):
        self.nums = list(map(lambda x: int(x), self.parser.get_lines()))
        self.invalid = self.find_invalid_index()

    def part_1(self):
        return self.nums[self.invalid]

    def part_2(self):
        # find contiguous set which add to number
        return self.find_weakness(self.invalid)
