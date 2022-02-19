from typing import List
from cmath import inf


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        minDif = inf
        for i in range(len(nums)):
            if i >= k - 1:
                minDif = min(nums[i]-nums[i-k+1], minDif)

        return minDif


print(Solution().minimumDifference([90], 1))
