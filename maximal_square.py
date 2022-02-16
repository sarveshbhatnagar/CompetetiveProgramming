from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        if(not matrix):
            return 0

        ROWS = len(matrix)
        COLS = len(matrix[0])
        dp = [[0]*(COLS+1) for j in range(ROWS+1)]

        ans = 0

        for i in range(1, ROWS+1):
            for j in range(1, COLS+1):
                if(matrix[i-1][j-1] == "1"):
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    ans = max(ans, dp[i][j]**2)
        return ans


matrix = [["1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "0"], ["1", "1", "1",
                                                                                               "1", "1", "1", "1", "0"], ["1", "1", "1", "1", "1", "0", "0", "0"], ["0", "1", "1", "1", "1", "0", "0", "0"]]
print(Solution().maximalSquare(matrix))
