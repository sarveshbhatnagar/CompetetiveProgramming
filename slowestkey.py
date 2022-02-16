from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:

        pt = [releaseTimes[0]]
        for i in range(1, len(releaseTimes)):
            pt.append(releaseTimes[i]-releaseTimes[i-1])

        max_val = pt[0]
        max_lex = keysPressed[0]

        for i in range(len(releaseTimes)):
            if(pt[i] > max_val):
                max_val = pt[i]
                max_lex = keysPressed[i]
            if(pt[i] == max_val and keysPressed[i] > max_lex):
                max_lex = keysPressed[i]

        return max_lex


keysPressed = "cbcd"
releaseTimes = [9, 29, 49, 50]
