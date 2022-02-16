from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        t = customers[0][0]
        waitTime = 0
        for i in range(len(customers)):
            d = 0
            if(t > customers[i][0]):
                d = abs(t - customers[i][0])
            else:
                t = customers[i][0]
            # print(d)
            waitTime += (d+customers[i][1])
            t += customers[i][1]
            # print(waitTime)

        # print(waitTime/len(customers))
        return waitTime/len(customers)


customers = [[2, 3], [6, 3], [7, 5], [11, 3], [15, 2], [18, 1]]
Solution().averageWaitingTime(customers)
