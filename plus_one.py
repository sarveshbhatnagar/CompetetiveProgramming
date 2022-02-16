class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tg = dict()
        for i in range(len(nums)):
            if nums[i] in tg:
                return [tg[nums[i]], i]
            else:
                tg[target - nums[i]] = i


q = [3, 3]
t = 6
print(Solution().twoSum(q, t))
