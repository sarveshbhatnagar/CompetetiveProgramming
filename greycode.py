from typing import List


class Solution:

    def codes(self, prev, n):
        if(n == 0):
            return prev
        l = [i+"0" for i in prev]
        r = list(reversed([i+"1" for i in prev]))
        prev = l+r
        return self.codes(prev, n-1)

    def grayCode(self, n: int) -> List[int]:
        base = ["0", "1"]
        c = self.codes(base, n-1)
        c = [int(i, 2) for i in c]
        return c
