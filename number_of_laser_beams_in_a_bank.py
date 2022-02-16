from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        devices = []
        for st in bank:
            cst = st.count('1')
            if(cst == 0):
                continue
            devices.append(cst)

        if(len(devices) < 2):
            return 0
        tsum = 0
        for i in range(1, len(devices)):
            if(devices[i] == 1 or devices[i-1] == 1):
                tsum += max(devices[i], devices[i-1])

            else:
                tsum += devices[i]*devices[i-1]

        return tsum


# bank = ["000", "111", "000"]
bank = ["011001", "000000", "010100", "001000"]
print(Solution().numberOfBeams(bank))
