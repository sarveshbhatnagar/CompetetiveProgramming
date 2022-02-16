from typing import List
from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = defaultdict(bool)

        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if len(s[i:]) >= len(word)-1 and s[i:i+len(word)] == word:
                    dp[i] = dp[i+len(word)]

                if(dp[i]):
                    break

        return dp[0]
