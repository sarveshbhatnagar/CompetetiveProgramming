from cmath import inf
from collections import defaultdict
from dis import dis
import heapq


class HeapNode:
    def __init__(self, x, y, pid):
        self.x = x
        self.y = y
        self.pid = pid

    def __lt__(self, other):
        return self.x + self.y < other.x + other.y

    def __gt__(self, other):
        return self.x + self.y > other.x + other.y

    def __eq__(self, other):
        return self.x + self.y == other.x + other.y

    def __le__(self, other):
        return self.x + self.y <= other.x + other.y

    def __ge__(self, other):
        return self.x + self.y >= other.x + other.y

    def __ne__(self, other):
        return self.x + self.y != other.x + other.y


class Solution:

    def dist(self, p1, p2):
        return abs(sum(p1) - sum(p2))

    def nearestCity(self, points, x_coordinates, y_coordinates, query):
        p_dict = defaultdict(list)
        p_d = dict()
        x_nodes = defaultdict(list)
        y_nodes = defaultdict(list)

        for i in range(len(points)):
            x_nodes[x_coordinates[i]].append(points[i])
            y_nodes[y_coordinates[i]].append(points[i])
            p_dict[points[i]] = x_coordinates[i], y_coordinates[i]

        res = []
        for q in query:
            x, y = p_dict[q]
            a = x_nodes[x]
            b = y_nodes[y]
            z = a+b
            sp = None
            min_dist = inf
            for p in z:
                if p == q:
                    continue
                dist = self.dist(p_dict[p], p_dict[q])
                if(dist < min_dist):
                    min_dist = dist
                    sp = p

            res.append(sp)
        return res

        # heapq.heappush(p_dict[point], HeapNode(x, y, points[i]))


points = ["p1", "p2", "p3", "p4", "p5"]

xCoordinates = [10, 20, 30, 40, 50]

yCoordinates = [10, 20, 30, 40, 50]

queriedPoints = ["p1", "p2", "p3", "p4", "p5"]

print(Solution().nearestCity(points, xCoordinates, yCoordinates, queriedPoints))
