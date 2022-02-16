# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        max_price = prices[0]
        max_profit = 0
        while j < len(prices):
            max_profit = max(max_profit, prices[j] - prices[i])
            if prices[j] < prices[i]:
                i = j
                max_price = prices[j]

            if prices[j] > max_price:
                max_price = prices[j]

            j += 1
        return max_profit


prices = [7, 1, 5, 3, 6, 4]

print(Solution().maxProfit(prices))
