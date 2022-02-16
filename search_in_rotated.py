from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l+r)//2
            if(nums[m] == target):
                return m

            if(nums[l] <= nums[m]):
                # LEFT SORTED PORTION.
                if(target > nums[m]):
                    # SEARCH RIGHT
                    l = m + 1
                    continue
                if(target <= nums[m] and target < nums[l]):
                    # SEARCH RIGHT
                    l = m + 1
                else:
                    # SEARCH LEFT
                    r = m - 1
            else:
                # RIGHT SORTED PORTION.
                if(target < nums[m]):
                    # SEARCH LEFT
                    r = m - 1
                    continue
                if(target > nums[m] and target > nums[r]):
                    # SEARCH LEFT
                    r = m - 1
                    pass
                else:
                    # SEARCH RIGHT
                    l = m + 1
        return -1


nums = [2, 1]

print(Solution().search(nums, 1))
