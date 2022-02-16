from collections import deque
import heapq


class Solution:
    def maxDisk(self, arr, k):
        z = deque(arr[:k])
        hp = arr[:k]
        heapq.heapify(hp)
        minimas = []
        for i in range(k, len(arr)):
            minimas.append(hp[0])
            a = z.popleft()
            hp.remove(a)
            heapq.heappush(hp, arr[i])
            z.append(arr[i])

        return max(minimas)


hdd = [62, 64, 77, 75, 71, 60, 79, 75]
k = 4


print(Solution().maxDisk(hdd, k))
