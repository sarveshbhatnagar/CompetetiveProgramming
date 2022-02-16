from typing import List

from collections import defaultdict


def bioHazard(n, allergic, poisonous):
    """
    Returns number of possible sequences.
    """
    nums = [i for i in range(1, n+1)]
    res = []
    for i in range(0, n):
        for j in range(0, n-i):
            res.append(set(nums[j:j+i+1]))

    apl = list(zip(allergic, poisonous))

    toremove = []
    # print(res)
    for possible_seq in res:
        for j in apl:
            if(j[0] in possible_seq and j[1] in possible_seq):
                toremove.append(possible_seq)
                break
    # print(toremove)

    # print(apl)
    return len(res) - len(toremove)


alergic = [2, 1, 3]
poisonous = [3, 3, 1]

print(bioHazard(3, alergic, poisonous))
