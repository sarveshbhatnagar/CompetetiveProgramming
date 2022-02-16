from typing import List
from collections import deque


class Solution:

    def isOverlapping(self, interval1, interval2):
        """
        Returns if intervals are overlapping.
        NOTE: interval2 is greater than interval1
        """

        if(interval2[0] <= interval1[1]):
            return True
        return False

    def mergeOverlapping(self, interval1, interval2):
        """
        Return's merged intervals
        """
        return [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 1

        intervals = sorted(intervals, key=lambda x: x[0])

        intervals = deque(intervals)
        print(intervals)

        if(len(intervals) <= 1):
            # BASE CASE.
            return intervals

        res = []
        while j < len(intervals):
            if(self.isOverlapping(intervals[i], intervals[j])):
                interval1 = intervals.popleft()
                interval2 = intervals.popleft()
                intervals.appendleft(
                    self.mergeOverlapping(interval1, interval2))
                continue

            res.append(intervals.popleft())

            # i += 1
            # j += 1
        while(intervals):
            res.append(intervals.popleft())
        return res


intervals = [[2, 3], [2, 2], [3, 3], [1, 3], [5, 7], [2, 2], [4, 6]]


print(Solution().merge(intervals))
