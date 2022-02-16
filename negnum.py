class Solution:
    def smallestNumber(self, num: int) -> int:
        minus = False
        if(num < 0):
            minus = True
            num *= -1
        num = sorted(str(num), reverse=True)
        if(minus):
            return -1*int("".join(num))
        zeros = []
        while(True):
            if(len(num) <= 0):
                break
            if(num[-1] == "0"):
                zeros.append(num.pop())

            else:
                break

        # check len
        if(len(num) == 0):
            return int("".join(zeros))

        n = [num.pop()]
        n.extend(zeros)
        while(num):
            n.append(num.pop())

        return int("".join(n))


print(Solution().smallestNumber(0))
