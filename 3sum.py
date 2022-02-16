from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        res = []
        while i < len(nums):
            a = nums[i]
            j = i+1
            k = len(nums)-1
            while j < k:
                b = nums[j]
                c = nums[k]
                if(a+b+c == 0):
                    res.append([a, b, c])
                    j += 1
                    while(nums[j-1] == nums[j] and j < k):
                        j += 1
                    continue

                if(a+b+c > 0):
                    k -= 1
                    continue
                else:
                    j += 1
                    continue

            i += 1
            while(i < len(nums) and nums[i-1] == nums[i]):
                i += 1
        return res


nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))
