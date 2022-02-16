from collections import defaultdict


class Solution:
    user_dict = defaultdict(lambda: 0)

    def addUser(self, u1, u2):
        u1 = int(u1)
        u2 = int(u2)
        self.user_dict[u1] += 1
        if(u1 != u2):
            self.user_dict[u2] += 1
        return

    def transactions(self, logData, threshold):
        for data in logData:
            z = data[0].split(" ")
            self.addUser(z[0], z[1])
        users = set()
        for key in self.user_dict.keys():
            if(self.user_dict[key] >= threshold):
                users.add(key)

        # l = sorted(list(users))
        return sorted(list(users))


data = [["345366 89921 45"],
        ["029323 38239 23"],
        ["38239 345366 15"],
        ["029323 38239 77"],
        ["345366 38239 23"],
        ["029323 345366 13"],
        ["38239 38239 23"]]

threshold = 3

print(Solution().transactions(data, threshold))
