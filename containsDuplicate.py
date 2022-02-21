from typing import List
from collections import Counter


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        c = Counter(nums[:k+1])
        if(k == 0):
            return False
        if(c.most_common(1)[0][1] >= 2):
            return True
        for j in range(k+1, len(nums)):
            # sub k-kth index...
            c[nums[j-(k+1)]] -= 1
            c[nums[j]] += 1
            if(c[nums[j]] >= 2):
                return True
        return False


nums = [4, 1, 2, 3, 1, 5]

print(Solution().containsNearbyDuplicate(nums, 3))
