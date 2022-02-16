class Solution:
    def match(self, group, basket):
        for i in range(len(group)):
            if(group[i] == "anything"):
                continue
            if(group[i] != basket[i]):
                return False

        return True

    def secretFruit(self, groups, basket):
        g1 = groups[0]
        g2 = groups[1]

        g1i = None
        g2i = None
        for i in range(0, len(basket)-len(g1)+1):
            # print(basket[i:i+len(g1)])
            if(self.match(g1, basket[i:i+len(g1)])):
                g1i = i
                break

        if g1i == None:
            return 0

        if len(g2) > len(basket) - g1i + len(g1):
            return 0

        for i in range(g1i+len(g1), len(basket)-len(g2)+1):
            if(self.match(g2, basket[i:i+len(g2)])):
                g2i = i
                return 1

        return 0


groups = [["apple", "apple"], ["banana", "anything", "banana"]]
basket = ["banana", "apple", "banana", "banana", "banana", "banana"]
print(Solution().secretFruit(groups, basket))
