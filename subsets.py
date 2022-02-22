from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        self.result = [[]]

        def helperFun(i, prevRes):
            if(i >= len(nums)):
                return

            for j in range(i, len(nums)):
                self.result.append(prevRes+[nums[j]])
                helperFun(j+1, prevRes+[nums[j]])

        helperFun(0, [])
        return self.result


print(Solution().subsets([1, 2, 3]))
