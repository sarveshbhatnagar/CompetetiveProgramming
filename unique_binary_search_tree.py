

class Solution:

    def getValueForRoot(self, i, ln, dp):
        """
        Returns the dp calculation given a root.
        """
        right = ln - (i+1)
        left = ln - (right+1)
        return dp[left] * dp[right]

    def numTrees(self, n: int) -> int:

        dp = [1] * (n+1)

        for i in range(2, n+1):
            tot = 0
            for j in range(1, i+1):
                tot += self.getValueForRoot(j-1, i, dp)
            dp[i] = tot

        # print(dp)
        return dp[-1]


print(Solution().numTrees(3))
