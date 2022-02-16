from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        teams = 0
        lgt = 0
        llt = 0
        rgt = 0
        rlt = 0
        for i in range(1, len(rating)-1):
            for j in range(i+1, len(rating)):
                if(rating[j] > rating[i]):
                    rgt += 1
                elif(rating[j] < rating[i]):
                    rlt += 1
            for j in range(0, i):
                if(rating[j] > rating[i]):
                    lgt += 1
                elif(rating[j] < rating[i]):
                    llt += 1
            teams += lgt * rlt
            teams += rgt * llt

        return teams
