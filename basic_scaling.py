# 11mins 40 seconds

import math

instances = 2
averageUtil = [25, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 76, 80]


def final_instances(instances, averageUtil):
    i = 0
    while i < len(averageUtil):
        if(averageUtil[i] < 25):
            if(instances > 1):
                instances = math.ceil(instances/2)
                i += 10
                continue
        if(averageUtil[i] > 60):
            j = 2*instances
            if(not j > 200000000):
                instances = j
                i += 10
                continue

        i = i + 1
    return instances


print(final_instances(instances, averageUtil))
