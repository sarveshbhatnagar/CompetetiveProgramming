from collections import deque
import heapq


class HeapNode:
    def __init__(self, time, hid):
        self.time = time
        self.id = hid

    def update_time(self, newtime):
        self.time = newtime

    def __lt__(self, other):
        return self.time < other.time

    def __gt__(self, other):
        return self.time > other.time

    def __eq__(self, other):
        return self.time == other.time

    def __le__(self, other):
        return self.time <= other.time

    def __ge__(self, other):
        return self.time >= other.time

    def __ne__(self, other):
        return self.time != other.time


class Solution:
    def lrucache(self, jobs, cacheSize):

        cache_set = dict()
        cache_queue = []

        misses = 0

        for i in range(len(jobs)):
            if(jobs[i] in cache_set):
                # do something
                cache_set[jobs[i]].update_time(i)
            else:
                misses += 1
                if(len(cache_queue) < cacheSize):
                    cache_set[jobs[i]] = HeapNode(i, jobs[i])
                    heapq.heappush(cache_queue, cache_set[jobs[i]])
                else:
                    z = heapq.heappop(cache_queue)
                    cache_set.pop(z.id)
        return misses


arr = [1, 2, 1, 3, 1, 2]
cacheSize = 2
print(Solution().lrucache(arr, cacheSize))
