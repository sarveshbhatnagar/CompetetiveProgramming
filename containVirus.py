from typing import List


class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        rcount = len(isInfected)
        ccount = len(isInfected[0])
        maptransition = {(0, 0): 0, (0, 1): 1, (1, 0): 1, (1, 1): 0}
        walls = 0
        for row in range(rcount):
            for col in range(1, ccount):
                walls += maptransition[(isInfected[row]
                                        [col-1], isInfected[row][col])]

        for col in range(ccount):
            for row in range(1, rcount):
                walls += maptransition[(isInfected[row-1]
                                        [col], isInfected[row][col])]

        return walls


isInfected = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

print(Solution().containVirus(isInfected))
