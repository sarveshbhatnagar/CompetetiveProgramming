from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, mx = 0, 0

        for r, n in enumerate(nums):
            k -= (1-n)
            if(k < 0):
                k += (1-nums[l])
                l += 1
            mx = max(mx, r-l+1)

        return mx


# nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
nums = [0, 0, 0, 0, 0, 0, 0, 0, 0]
k = 0

# nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
# nums = [0, 0, 1, 1, 1, 0, 0]
# k = 3
# k = 0
# k = 2
print(Solution().longestOnes(nums, k))
