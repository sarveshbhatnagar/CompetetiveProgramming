from typing import List

from collections import defaultdict


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = defaultdict(int)
        n = len(nums)-1

        # base case
        lis[n] = 1

        for i in range(len(nums)-2, -1, -1):
            cur_val = nums[i]
            possible_set = [1]
            # print(cur_val)
            for j in range(i+1, len(nums)):
                if(nums[j] > cur_val):
                    # print(cur_val, nums[j])
                    possible_set.append(1+lis[j])

            # print("MAX: ",nums[i],max(possible_set))
            lis[i] = max(possible_set)

        return max(lis.values())
