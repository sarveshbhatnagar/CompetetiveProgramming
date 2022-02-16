# 17m 0s

from typing import List


class Solution:
    def cutOffRank(self, scores: List[int], cutOffRank: int, num: int) -> int:
        scores_sorted = sorted(scores, reverse=True)

        # Give ranking
        rank = 0
        ranks = []
        prev = -1
        count = 1
        for i in range(len(scores_sorted)):
            if(scores_sorted[i] != prev):
                prev = scores_sorted[i]
                rank += count
                ranks.append(rank)
                count = 1
                continue
            if(scores_sorted[i] == prev):
                count += 1
                ranks.append(rank)
                continue

        count = 0
        for i in ranks:
            if(i <= cutOffRank):
                count += 1
            else:
                break
        print(ranks)
        return count


scores = [10, 10, 5, 3]
cutOffRank = 2
num = 4

print(Solution().cutOffRank(scores, cutOffRank, num))
