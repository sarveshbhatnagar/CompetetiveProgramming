from collections import defaultdict


class Solution:

    def criticalConnections(self, connections):
        dis = [0] * len(connections)
        low = [0] * len(connections)
        self.time = 0
        res = []
        visited = set()
        g = defaultdict(list)

        for s, t in connections:
            g[s].append(t)
            g[t].append(s)

        def dfs(node, parent):
            nonlocal self, res, visited, low, dis
            visited.add(node)
            low[node] = dis[node] = self.time
            self.time += 1
            for n in g[node]:
                if n == parent:
                    continue
                if n not in visited:
                    dfs(n, node)
                    low[node] = min(low[node], low[n])
                    if low[n] > dis[node]:
                        res.append([node, n])
                else:
                    low[node] = min(low[node], dis[n])

        dfs(0, -1)
        return res
