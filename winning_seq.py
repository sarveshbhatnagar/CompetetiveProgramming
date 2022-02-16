def winning_seq(num, lowerEnd, upperEnd):
    arr = [0 for i in range(num)]
    if(upperEnd-1 == lowerEnd):
        return -1
    arr[0] = upperEnd-1
    arr[1] = upperEnd
    p = upperEnd
    for i in range(2, num):
        p = p-1
        if(p < lowerEnd):
            return -1
        arr[i] = p
    return arr


print(winning_seq(5, 3, 10))
