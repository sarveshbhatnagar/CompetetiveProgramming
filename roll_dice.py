from collections import defaultdict


class Solution:
    def rollDice(self, arr):
        map_val = {
            6: 1,
            1: 6,
            2: 4,
            4: 2,
            3: 5,
            5: 3
        }
        count_elem = defaultdict(int)

        showFace = None
        max_count = 0
        for elem in arr:
            count_elem[elem] += 1
            if count_elem[elem] > max_count:
                max_count = count_elem[elem]
                showFace = elem

        return len(arr) - count_elem[showFace] + count_elem[map_val[showFace]]


# def number_of_rotations(dice: List[int]) -> int:

#     return min(

#         sum(0 if d == v else 1 if d + v != 7 else 2 for d in dice)

#         for v in range(1, 7)

#     )

# N = [6, 6, 1]
N = [6, 1, 5, 4]
print(Solution().rollDice(N))
