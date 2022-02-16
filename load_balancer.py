
# TODO Remaining...
from collections import deque


class Solution:
    def balance_load(self, arr):
        i = 0
        j = len(arr) - 1

        if(len(arr) < 5):
            return False

        isum = arr[i]
        jsum = arr[j]
        indeqi = None
        indeqj = None
        while i < j:
            if(isum == jsum):
                indeqi = i
                indeqj = j

                i += 1
                if(i < len(arr)):
                    isum += arr[i]
                else:
                    break

            if(isum > jsum):
                j -= 1
                jsum += arr[j]
            else:
                i += 1
                isum += arr[i]

        if(indeqi and indeqj):

            return arr[indeqi+1], arr[indeqj-1]
        else:
            return False


array = [2, 4, 5, 3, 3, 9, 2, 2, 2]
print(Solution().balance_load(array))
