from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = sum(nums[:k])
        curSum = maxSum
        for i in range(k, len(nums)):
            print(nums[i])
            curSum -= nums[i-k]
            curSum += nums[i]
            maxSum = max(maxSum, curSum)

        return maxSum/k
