

from typing import List

from matplotlib.pyplot import box


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        ans = 0
        for i in range(truckSize):
            ans += boxes[0][1]
            boxes[0][0] -= 1
            if(boxes[0][0] == 0):
                boxes.pop(0)

        return ans


boxTypes = [[1, 3], [2, 2], [3, 1]]
truckSize = 4

print(Solution().maximumUnits(boxTypes, truckSize))
