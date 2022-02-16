class Solution:
    def findMemoryPairs(self, foreground, background, k):
        foreground_dict = dict()
        background_dict = dict()
        for i in range(len(foreground)):
            foreground_dict[foreground[i]] = i
        for j in range(len(background)):
            background_dict[background[j]] = j

        # Edge case: maximum val in one only.
        pairs = []
        if k in foreground_dict:
            pairs.append((foreground_dict[k], -1))
        if k in background_dict:
            pairs.append((-1, background_dict[k]))
        while True:
            for key in background_dict:
                if abs(key-k) in foreground_dict:
                    pairs.append(
                        (foreground_dict[abs(key-k)], background_dict[key]))

            if(len(pairs) > 0 or k == 0):
                break
            k -= 1

        return pairs


# foregroundTasks = [1, 7, 2, 4, 5, 6]
foregroundTasks = [3, 5, 7, 10]
# backgroundTasks = [3, 1, 2]
backgroundTasks = [2, 3, 4, 5]

k = 10
# k = 6

print(Solution().findMemoryPairs(foregroundTasks, backgroundTasks, k))
