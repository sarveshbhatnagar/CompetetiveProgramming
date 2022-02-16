

class Solution():
    def minimumRemoval(self, beans):
        """
        :type beans: List[int]
        :rtype: int
        """
        a = sorted(beans)
        s = r = sum(a)
        n = len(beans)
        for i, v in enumerate(a):
            r = min(r, s-v*(n-i))
        return r


beans = [4, 1, 6, 5]
print(Solution().minimumRemoval(beans))
