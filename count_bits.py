def countBits(n):
    """
    :type num: int
    :rtype: List[int]
    """
    # Approach 1:
    # res = [0]
    # for i in range(1, n+1):
    #     res.append(res[i>>1] + (i&1))
    # return res

    # Approach 2:
    # res = [0]
    # for i in range(1, n+1):
    #     res.append(res[i&(i-1)] + 1)
    # return res

    # Approach 3:
    # res = [0]
    # for i in range(1, n+1):
    #     res.append(res[i&(i-1)] + 1)
    # return res

    # Approach 4:
    # res = [0]
    # for i in range(1, n+1):
    #     res.append(res[i&(i-1)] + 1)
    # return res

    # Approach 5:
    # res = [0]
    # for i in range(1, n+1):
    #     res.append(res[i&(i-1)] + 1)
    # return res

    # Approach 6:
    # res = [0]
    # for i in range(1, n+1):
    #     res.append(res[i&(i-1)] + 1)
    # return res

    # Approach 7:
    # res = [0]
    # for i in range(1, n+1):
    #     res.append(res[i&(i-1)] + 1)
    # return res

    # Approach 8:
    # res = [0]
    # for i in range(1, n+1):
    #     res.append(res[i&(i-1)] + 1)
    # return res

    # Approach 9:
    res = [0]
    for i in range(1, n+1):
        res.append(res[i & (i-1)] + 1)
    return res


print(countBits(2))
