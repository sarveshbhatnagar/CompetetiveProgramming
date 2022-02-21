from typing import List
from collections import Counter


class Solution:
    def checkValid(self, counts):
        for i in counts:
            if(counts[i] == 0 or len(counts) != 3):
                return False

        return True

    def numberOfSubstrings(self, s: str) -> int:
        c = Counter()
        l = 0
        counts = 0
        for r in range(len(s)):
            # Shift right as much as we can
            c[s[r]] += 1
            while(self.checkValid(c)):
                # Shift left as much as we can
                counts += len(s)-r
                c[s[l]] -= 1
                l += 1

        return counts
