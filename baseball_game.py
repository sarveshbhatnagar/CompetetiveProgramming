from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record = []
        for i in ops:
            if(i == "C"):
                record.pop()
            elif(i == "D"):
                record.append(record[-1]*2)
            elif(i == "+"):
                record.append(record[-1]+record[-2])
            else:
                record.append(int(i))
        return sum(record)


ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
print(Solution().calPoints(ops))
