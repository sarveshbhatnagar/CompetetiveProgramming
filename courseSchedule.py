from typing import List


class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False

            if prereq[crs] == []:
                return True

            visitSet.add(crs)

            for pr in prereq[crs]:
                if not dfs(pr):
                    return False

            visitSet.remove(crs)
            prereq[crs] = []

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True


numCourses = 2
prerequisites = [[1, 0], [0, 1]]
print(Solution().canFinish(numCourses, prerequisites))
