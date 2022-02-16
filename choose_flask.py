import bisect
from cmath import inf


class Solution:
    def chooseFlask(self, jobs, flask):
        new_flasks = []
        for i in flask:
            new_flasks.append(list(map(int, i.split(" "))))

        print(new_flasks)

        arr = [0 for i in range(len(new_flasks))]
        for job in jobs:
            for j in range(len(new_flasks)):
                i = bisect.bisect_left(new_flasks[j], job)
                if(i > len(new_flasks[j])-1):
                    arr[j] = inf
                    continue
                arr[j] += new_flasks[j][i] - job

        print(arr)
        mi = inf
        ind = -1
        for i in range(len(arr)):
            if(arr[i] < mi):
                mi = arr[i]
                ind = i

        return ind


jobs = [4, 6, 6, 7]
flask = ["3 5 7", "6 8 9", "3 5 6"]
print(Solution().chooseFlask(jobs, flask))
