# Question is something like this:
# [[1,5],[2,4],[3,4],[4,5],[7,3]]
# Sort by 2nd pos in descending and 1st pos in ascending...

# Basic of cmp_to_key is if x<y then negative, x>y then positive and for x==y 0

from functools import cmp_to_key


class Solution:
    def __init__(self) -> None:
        pass

    def compare(self, x, y):
        if(x[1] > y[1]):
            # Coz in reverse...
            return -1
        elif(x[1] < y[1]):
            return 1

        else:
            # Equal case
            if(x[0] < y[0]):
                return -1
            elif(x[0] > y[0]):
                return 1
            else:
                return 0

    def customSort(self, arr):
        arr = sorted(arr, key=cmp_to_key(self.compare))
        return arr


arr = [[1, 5], [2, 4], [3, 4], [4, 5], [7, 3]]
print(Solution().customSort(arr))
