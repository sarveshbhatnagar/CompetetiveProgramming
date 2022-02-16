from typing import List


class Solution:
    combinations = list()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.search(res, candidates, target)

        return self.combinations

    def search(self, res, candidates, target):
        if not candidates:
            return

        if sum(res) == target:
            self.combinations.append(res.copy())
            return

        if sum(res) > target:
            return

        # one side with including all, other side with excluding.
        if len(candidates) > 0:
            z = res + [candidates[0]]
        else:
            z = res
        self.search(z, candidates, target)
        self.search(res, candidates[1:], target)


print(Solution().combinationSum([2, 3, 5], 8))
