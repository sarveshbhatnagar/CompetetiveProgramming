from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        res = nums[0]
        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break

            mid = (l+r) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                # minimum towards left side.
                l = mid+1
            else:
                # minimum towards right side.
                r = mid-1

        return res
