# 10m 30s

from bisect import bisect_left
from math import floor


def multiProcessorSolution(processors, processes):
    arr = sorted(processors)
    count = 0
    while True:
        count += 1
        p = arr.pop()
        processes -= p
        p = floor(p/2)
        i = bisect_left(arr, p)
        arr.insert(i, p)
        if(processes <= 0):
            break
    return count


print(multiProcessorSolution([3, 1, 7, 2, 4], 15))
