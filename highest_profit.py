import heapq


class Solution:
    def getHighestProfit(self, inventories, order):
        modified_inv = [-i for i in inventories]
        heapq.heapify(modified_inv)
        profit = 0
        for i in range(order):
            res = heapq.heappop(modified_inv)
            profit += -res
            res = res+1
            heapq.heappush(modified_inv, res)

        return profit


inventories = [10, 10]
order = 5

print(Solution().getHighestProfit(inventories, order))
