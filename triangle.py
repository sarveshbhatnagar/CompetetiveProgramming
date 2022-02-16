from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        rows = len(triangle)

        if(rows == 0):
            return 0
        if(rows == 1):
            return triangle[0][0]

        dp = [0] * len(triangle[-1])
        for i in range(rows-2, -1, -1):
            for j in range(len(triangle[i])+1):
                dp[j] = min(dp[j]+triangle[i+1][j], dp[j]+triangle[i+1][j+1])
        # print(dp)
        return dp[0] + triangle[0][0]


t = [[-1], [2, 3], [1, -1, -3]]

print(Solution().minimumTotal(t))
