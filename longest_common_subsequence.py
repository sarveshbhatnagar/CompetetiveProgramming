class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # make matrix
        dp = [[0 for i in range(len(text1)+1)] for j in range(len(text2)+1)]

        # we have len(text2)+1 rows and len(text1)+1 columns

        for row in range(len(text2)-1, -1, -1):
            for col in range(len(text1)-1, -1, -1):
                if(text2[row] == text1[col]):
                    dp[row][col] = 1 + dp[row+1][col+1]
                else:
                    dp[row][col] = max(dp[row][col+1], dp[row+1][col])

        return dp[0][0]
