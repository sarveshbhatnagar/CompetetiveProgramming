class Solution:
    def minimumTime(self, s: str) -> int:
        total_ones = s.count("1")
        atfront = 0
        atback = 0
        
        if(len(s) == total_ones):
            # if string is all one.
            return total_ones
        
        if(total_ones == 0):
            # the train is clean
            return 0
        
        # Count number of 1's at front.
        for i in range(len(s)):
            if(s[i] == "1"):
                atfront +=1
            else:
                break
                
        for i in range(len(s)-1,-1,-1):
            if(s[i] == "1"):
                atback += 1
            else:
                break

        t = atfront+atback
        
        return t + (2*(total_ones-t))