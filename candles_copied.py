from typing import List

from bisect import bisect_left
from bisect import bisect_right


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        ans = []
        A = [i for i, c in enumerate(s) if c == '|']  # indices of '|'

        for left, right in queries:
            print(s)
            print("Candle Pos: ", A)
            l = bisect_left(A, left)
            print("Left: ", l, left)
            r = bisect_right(A, right) - 1
            print("Right: ", r, right)

            if l < r:
                print(A[r])
                print(A[l])
                lengthBetweenCandles = A[r] - A[l] + 1
                numCandles = r - l + 1
                ans.append(lengthBetweenCandles - numCandles)
            else:
                ans.append(0)

        return ans


# Test cases
s = "***|**|*****|**||**|*"

queries = [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]
# queries = [[5, 16]]

print(Solution().platesBetweenCandles(s, queries))
