from typing import List
import heapq
from collections import deque


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)-1
        a1 = []
        a2 = []
        while(i <= j):
            if(i == j):
                c = nums[i]
                if(max(a1) > c):
                    a1.append(c)
                else:
                    a2.append(c)
                break

            if(i < j):
                a1.append(nums[i])
                i += 1
                a2.append(nums[j])
                j -= 1

        # a1 = [-i for i in a1]
        # heapq.heapify(a1)
        a1 = deque(sorted(a1))
        # heapq.heapify(a2)
        a2 = deque(sorted(a2, reverse=True))
        print(a1)
        print(a2)
        an = int(len(nums)/3)
        for i in range(an):
            if(a1[-1] > a2[0] and len(a1) > an):
                a1.pop()
            elif(a2[-1] < a1[0] and len(a2) > an):
                a2.pop()
            elif(a1[-1] >= a2[0]):
                a1.pop()
                if(len(a1) < an):
                    z = a2.popleft()
                    a1.append(z)

            elif(a2[-1] <= a1[0]):
                a2.pop()
                if(len(a2) < an):
                    z = a1.popleft()
                    a2.append(z)

        print(a1)  # 215
        print(a2)
        return sum(a1) - sum(a2)


nums = [16, 46, 43, 41, 42, 14, 36, 49, 50, 28,
        38, 25, 17, 5, 18, 11, 14, 21, 23, 39, 23]
print(Solution().minimumDifference(nums))
