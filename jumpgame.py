from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        visited = set()
        if(len(nums) == 1):
            return 0
        pos = {0}
        level = 0
        while True:
            level += 1
            newPos = set()
            for i in pos:
                visited.add(i)
                j = nums[i]
                if(i+j >= len(nums)-1):
                    return level
                for k in range(i, i+j+1):
                    if(k not in visited and k not in pos):
                        newPos.add(k)
            pos = newPos

        # return level


nums = [1, 2, 3]
print(Solution().jump(nums))
