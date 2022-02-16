class Solution:
    def breakPalindrome(self, s):
        # Check if its odd, if it is get mid.
        mid = None
        if len(s) % 2 != 0:
            mid = len(s)//2

        if len(s) <= 1:
            return ""

        for i in range(len(s)):
            if i == mid:
                continue
            if s[i] != 'a':
                s = s[:i] + 'a' + s[i+1:]
                return s

        return s[:-1] + 'b'
