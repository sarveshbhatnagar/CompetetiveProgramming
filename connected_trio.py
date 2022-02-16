from cmath import inf
from typing import List


from collections import defaultdict

from sympy import deg


class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        nodes = defaultdict(set)

        for u, v in edges:
            nodes[u].add(v)
            nodes[v].add(u)

        ans = inf
        for u in nodes:
            for n2 in nodes[u]:
                for n3 in nodes[n2]:
                    if u in nodes[n3] and n2 in nodes[n3]:
                        ans = min(ans, len(nodes[u]) +
                                  len(nodes[n2]) + len(nodes[n3])-6)

        return ans if ans != inf else -1

    def minToDegreeTwo(self, n: int, edges: List[List[int]]) -> int:
        nodes = defaultdict(set)
        degrees = defaultdict(int)

        for u, v in edges:
            if(u < v):
                nodes[u].add(v)
            else:
                nodes[v].add(u)
            degrees[u] += 1
            degrees[v] += 1

        ans = inf
        for u in nodes:
            for v in nodes[u]:
                if(v not in nodes):
                    continue
                for x in nodes[v]:
                    if x in nodes[u]:
                        ans = min(ans, degrees[u] +
                                  degrees[v] + degrees[x] - 6)

        return ans if ans != inf else -1

        # return 0


n = 0
edges = [[1, 2], [1, 3], [3, 2], [4, 1], [5, 2], [3, 6]]
# print(Solution().minTrioDegree(n, edges))
print(Solution().minToDegreeTwo(n, edges))
