from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]

        while(l <= r):
            if(nums[l] <= nums[r]):
                res = min(res, nums[l])
                break

            m = (l+r)//2
            # Check which part does middle belong...
            # Also consume its value...
            res = min(res, nums[m])
            # Consumed.
            if(nums[l] <= nums[m]):
                # Search on right part.
                l = m+1
            else:
                r = m-1

        return res


# nums = [6, 1, 2, 3, 4, 5]
nums = [2, 1]
# nums = [4, 5, 6, 7, 0, 1, 2]
print(Solution().findMin(nums))
