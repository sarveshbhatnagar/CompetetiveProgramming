from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        z = set(nums)
        if(len(z) == len(nums)):
            return "false"
        else:
            return "true"


nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(Solution().containsDuplicate(nums))
