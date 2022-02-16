# 12m 22s

def package_automation(arr):
    narr = sorted(arr)
    narr[0] = 1
    for i in range(1, len(arr)):
        if(narr[i]-narr[i-1] > 1):
            narr[i] = narr[i-1] + 1

    return narr[-1]


arr = [3, 1, 3, 4]
print(package_automation(arr))
