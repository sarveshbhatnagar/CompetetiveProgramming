from functools import lru_cache
from typing import List


class Solution:

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        i = 1

        @lru_cache(None)
        def dfs(i, j, day):
            if([i, j] in cells[:day]):
                return row*col

            if(i > row or j > col or i < 1 or j < 1):
                return row*col

            if(i == col):
                return day

            a = dfs(i+1, j, day+1)
            b = dfs(i-1, j, day+1)
            c = dfs(i, j+1, day+1)
            d = dfs(i, j-1, day+1)

            return min(a, b, c, d)
        res = []
        for l in range(1, col+1):
            res.append(dfs(i, l, 0))

        return min(res)


arr = [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]
r = c = 3
print(Solution().latestDayToCross(r, c, arr))
