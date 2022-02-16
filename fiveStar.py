# Beautiful Solution
# Took a lot time to get this one.

import heapq


class HeapNode:
    def __init__(self, studentPassed, studentTotal):
        self.studentPassed = studentPassed
        self.studentTotal = studentTotal
        self.ratio = self.calcRatio(self.studentPassed, self.studentTotal)
        self.delta = self.calcDelta(1, 1)

    def calcDelta(self, a, b):
        sp1 = self.studentPassed + a
        st1 = self.studentTotal + b
        return -1 * (self.calcRatio(sp1, st1) - self.ratio)

    def calcRatio(self, a, b):
        return a / b

    def __lt__(self, other):
        return self.delta < other.delta

    def __gt__(self, other):
        return self.delta > other.delta

    def __eq__(self, other):
        return self.delta == other.delta

    def __le__(self, other):
        return self.delta <= other.delta

    def __ge__(self, other):
        return self.delta >= other.delta

    def __ne__(self, other):
        return self.delta != other.delta


class Solution:
    def maxAverageRatio(self, classes, extraStudents):
        classes = [HeapNode(c[0], c[1]) for c in classes]

        heapq.heapify(classes)

        while extraStudents > 0:
            minNode = heapq.heappop(classes)
            print(minNode.studentPassed, minNode.studentTotal, minNode.ratio)
            minNode.studentPassed += 1
            minNode.studentTotal += 1
            minNode.ratio = minNode.calcRatio(
                minNode.studentPassed, minNode.studentTotal)
            minNode.delta = minNode.calcDelta(1, 1)
            print(minNode.studentPassed, minNode.studentTotal, minNode.ratio)
            heapq.heappush(classes, minNode)
            extraStudents -= 1

        vals = [i.ratio for i in classes]
        return sum(vals)/len(vals)


classes = [[1, 2], [3, 5], [2, 2]]
extraStudents = 2


print(Solution().maxAverageRatio(classes, extraStudents).ratio)
