# 22m 50s

class Solution:

    def getChar(self, next=False):
        if(next):
            z = self.important_rates[1]
        else:
            z = self.important_rates[0]

        self.counts[z] -= 1
        if(self.counts[z] == 0):
            self.important_rates.remove(z)

        return z

    def makeLabels(self, labelString, k):
        from collections import Counter
        self.counts = Counter(list(labelString))

        self.important_rates = sorted(list(set(labelString)), reverse=True)

        c = 0
        cur_str = []
        for i in range(len(labelString)):
            if(c == k and self.counts[cur_str[-1]] != 0):
                try:
                    a = self.getChar(next=True)
                except:
                    break
                cur_str.append(a)
                c = 0
                continue

            a = self.getChar()
            cur_str.append(a)
            c += 1

        return "".join(cur_str)


labelString = "baccc"
k = 2
print(Solution().makeLabels(labelString, k))
