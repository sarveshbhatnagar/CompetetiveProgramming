from cmath import inf
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        min_dict = dict()
        max_dict = dict()
        for i in range(len(s)):
            if(s[i] not in min_dict):
                min_dict[s[i]] = i
                max_dict[s[i]] = i
            else:
                max_dict[s[i]] = i

        i = 0
        cur_min = min_dict[s[0]]
        cur_max = max_dict[s[0]]
        # TODO handle edge case of length 1
        groups = []
        g = 0
        while i < len(s):
            if(i == cur_max):
                # group.
                g += 1
                groups.append(g)
                cur_min = i+1
                if(i < len(s)-1):
                    cur_max = max_dict[s[i+1]]
                g = 0
                i += 1
                continue

            # for each in between element update maximum
            if(cur_max < max_dict[s[i]]):
                cur_max = max_dict[s[i]]
            g += 1
            i += 1

        return groups

        # print(min_dict)
        # print(max_dict)


s = "ababcbacadefegdehijhklij"
# s = "baddacx"
print(Solution().partitionLabels(s))
