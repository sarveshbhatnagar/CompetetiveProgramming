from typing import List

from bisect import bisect_left
from bisect import bisect_right


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        ans = []
        # TODO get candles positions...
        # print(s)

        A = [i[0] for i in enumerate(s) if i[1] == "|"]  # O(n)
        ans = []
        for left, right in queries:
            # print("Query: ", left, right)
            l = bisect_left(A, left)
            r = bisect_right(A, right)-1
            # print(l, r)
            if l < r:
                len_bw = A[r] - A[l] - 1
                candles_bw = r-l - 1
                ans.append(len_bw - candles_bw)
            else:
                ans.append(0)
        return ans


s = "***|**|*****|**||**|*"

queries = [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]
print(Solution().platesBetweenCandles(s, queries))
