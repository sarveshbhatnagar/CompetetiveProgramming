from typing import List

from collections import deque


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums = deque(nums)
        result = []

        if len(nums) == 1:
            return [nums.copy()]

        for i in range(len(nums)):
            n = nums.popleft()
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)

            result.extend(perms)
            nums.append(n)

        return result


print(Solution().permute([1, 2]))
