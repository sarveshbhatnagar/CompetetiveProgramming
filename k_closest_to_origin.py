from typing import List


class Solution:

    def distance(self, p1, p2=(0, 0)):
        return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Approach:
        # Calculate distance for every point.
        # Return sorted based on distance.

        # Time Complexity: O(NlogN)

        points = [(p, self.distance(p)) for p in points]
        points.sort(key=lambda x: x[1])
        return [p[0] for p in points[:k]]


points = [[3, 3], [5, -1], [-2, 4]]
k = 2

print(Solution().kClosest(points, k))
