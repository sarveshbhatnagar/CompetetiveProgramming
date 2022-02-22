from collections import Counter
from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = Counter()
        l = 0
        maxRes = 0
        for r, val in enumerate(s):
            c[val] += 1
            # print(c, l, r)
            if(c[val] == 1):
                maxRes = max(maxRes, r-l+1)
            while(c[val] > 1):
                c[s[l]] -= 1
                l += 1

        return maxRes
