from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])

        rows = [set() for i in range(rowLen)]
        cols = [set() for i in range(colLen)]

        for i in range(rowLen):
            for j in range(colLen):
                if(grid[i][j] == 1):
                    rows[i].add((i, j))
                    cols[j].add((i, j))

        # always check len(rows[i] > 2)...
        talking = 0
        for i in range(rowLen):
            for j in range(colLen):
                if((len(rows[i]) > 1 or len(cols[j]) > 1) and ((i, j) in rows[i] or (i, j) in cols[j])):
                    talking += 1

        return talking


# grid = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
grid = [[1, 0], [1, 1]]
print(Solution().countServers(grid))
