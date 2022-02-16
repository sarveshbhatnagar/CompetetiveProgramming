from cmath import inf


def getMaximumGreyness(pixels):
    """
    Logic is simple, simply maintain count for 1's
    count for 0 would be count_onesrow-m and count_onescol-n

    Based on that, for each pixel calculate the greyness.

    O(n*m)
    """
    l = list(zip(*pixels))
    row_counts = [0 for i in range(len(l))]
    col_counts = [0 for i in range(len(l[0]))]

    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] == '1':
                row_counts[i] += 1
                col_counts[j] += 1

    -inf

    print(row_counts)
    print(col_counts)



    # print(list(zip(*pixels)))

    # for col in zip(*pixels):
    #     count_onescol.append(col.count('1'))

    # print(count_onesrow, count_onescol)


pixels = ['101', '001', '101']

getMaximumGreyness(pixels)
