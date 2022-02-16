# https://www.codechef.com/SNCKEL21/problems/SORTSEGS
import numpy as np


def sort_at(nl, lis, k, a=0):
    """
    [-1,1,0,0,0,0,-1,1]
    """
    mind = 0
    mval = 0
    vlis = []
    for i in range(0, len(nl)-k + 1 - a):
        v = abs(sum(nl[i:i+k]))

        vlis.append(v)
        if(v > mval and v != 0):
            mval = v
            mind = i
    return mind, max(lis) != 0


def sort_seg(lis, k):
    # Calculating Sum.
    sorted_lis = sorted(lis)
    while(lis != sorted_lis):
        nl = []
        for i in range(0, len(lis)-k+1):
            nl.append(sum(lis[i:i+k]))

        # Checking where to sort This part is going wrong somewhere.
        wrong_ind = 0
        for i in range(1, len(nl)):
            if(nl[i-1] > nl[i]):
                if(sorted(lis[i-1:i+k-1]) != lis[i-1:i+k-1]):
                    wrong_ind = i-1
                    break
        print(wrong_ind)
        print(lis[wrong_ind:wrong_ind+k])
        # Sorting
        if(i != len(nl)-1):
            lis = lis[:wrong_ind] + \
                sorted(lis[wrong_ind:wrong_ind+k]) + lis[wrong_ind+k:]
    return lis

    # if its negative
    # add till 0 if abs less than k else add k.
    # if its positive
    # sub till k if abs less than k else add k.

    # print(sort_weights)
    return nl


print(sort_seg([2, 6, 4, 3, 1, 5], 4))
