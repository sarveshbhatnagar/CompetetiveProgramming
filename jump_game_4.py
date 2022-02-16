from typing import List

import heapq


class Solution:
    def get_max(self, ps, nums, k):
        if(not nums):
            return ps

        z = [self.get_max(ps+nums[i], nums[i+1:], k)
             for i in range(min(k, len(nums)))]

        return max(z)

    def maxResult(self, nums: List[int], k: int) -> int:
        # return self.get_max(nums[0], nums[1:], k)
        # What i need to do is start from end, keep track of max value for
        # every position.

        dp = [0 for i in range(len(nums))]
        dp[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            dp[i] = max([nums[i]+dp[j]
                         for j in range(i+1, min(i+k+1, len(nums)))])

        return dp[0]

    def maxResult2(self, nums: List[int], k: int) -> int:
        # return self.get_max(nums[0], nums[1:], k)
        # What i need to do is start from end, keep track of max value for
        # every position.
        q = [(-nums[-1], len(nums)-1)]
        for i in range(len(nums)-2, -1, -1):
            while(q and q[0][1] > i+k):
                heapq.heappop(q)
            v = nums[i] + (-q[0][0])
            heapq.heappush(q, (-v, i))
            if i == 0:
                return v
            # heapq.heappush(q, (-nums[i]-q[0][0], i))
        # return -q[0][0]


nums = [1, -1, -1, -1, 5]
# nums = [1, -1, -2, 4, -7, 3]
print(Solution().maxResult2(nums, 2))
