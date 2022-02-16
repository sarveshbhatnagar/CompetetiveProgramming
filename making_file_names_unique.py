from typing import List
from collections import defaultdict


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        prev = defaultdict(int)
        arr = []
        for name in names:
            if name not in prev:
                prev[name] = 0
                arr.append(name)
            else:
                prev[name] += 1
                counter = prev[name]
                while True:
                    new_name = name + '(' + str(counter) + ')'

                    print(new_name)
                    if(new_name not in prev):
                        prev[new_name] = 0
                        arr.append(new_name)
                        break
                    else:
                        counter += 1

        return arr


names = ["kaido", "kaido(1)", "kaido", "kaido(1)", "kaido(2)"]
print(Solution().getFolderNames(names))


# Incorrect test case:
# "kaido", "kaido(1)", "kaido", "kaido(1)", "kaido(2)"
# Result should be
# 'kaido', 'kaido(1)', 'kaido(3)', 'kaido(1)(1)', 'kaido(2)'
# and not:
# ["kaido","kaido(1)","kaido(2)","kaido(1)(1)","kaido(2)(1)"]
