from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curSum = sum(arr[:k])
        tsum = threshold * k
        curCount = 0
        if(curSum >= tsum):
            curCount += 1
        for i in range(k, len(arr)):
            curSum -= arr[i-k]
            curSum += arr[i]
            if(curSum >= tsum):
                curCount += 1

        return curCount
