from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        if(len(nums) == 0):
            return 0, []
        count = 1
        while(j < len(nums)):
            if(nums[i] == nums[j]):
                j += 1
            else:
                i += 1
                count += 1
                print(nums[j])
                print(i, j)
                nums[i] = nums[j]

        print(count)
        print(nums[:count])


nums = [1, 1, 2]
print(Solution().removeDuplicates(nums))
