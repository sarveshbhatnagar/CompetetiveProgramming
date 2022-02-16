from cmath import inf
from typing import List


class Solution:
    def fillAmount(self, amount, coins, dp, default):
        """
        Given amount, find minimum number of coins to get that
        """
        # res = []
        minVal = inf
        for coin in coins:
            if(amount-coin >= 0):
                # res.append(1+dp[amount-coin])
                minVal = min(1+dp[amount-coin], minVal)

        # if(res == []):
        #     return default
        # return min(res)
        return minVal

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for i in range(1, len(dp)):
            # Fill dp...
            dp[i] = self.fillAmount(i, coins, dp, amount+1)

        # print(dp)
        return dp[-1]


coins = [1, 2, 5]
amount = 11

print(Solution().coinChange(coins, amount))
