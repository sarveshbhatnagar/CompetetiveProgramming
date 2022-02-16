from typing import List
from collections import defaultdict, Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_counter = Counter(p)
        res = []
        s_counter = Counter(s[:len(p)-1])
        i = 0
        j = i+len(p)-1

        while True:
            if(j >= len(s)):
                break
            s_counter[s[j]] += 1
            # print(s_counter)

            if(s_counter == p_counter):
                res.append(i)

            s_counter[s[i]] -= 1
            if(s_counter[s[i]] == 0):
                del s_counter[s[i]]
            i += 1
            j += 1
        return res
        # for i in range(len(s) - len(p) + 1):


# s = "cbaebabacd"
s = "abab"
p = "ab"

print(Solution().findAnagrams(s, p))
