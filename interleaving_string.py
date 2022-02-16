class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # We have s1, s2, s3.
        # We need to find if s3 is interleaving of s1 and s2.
        # we can use double pointer to do that.
        i = 0
        j = 0
        k = 0

        res1 = False

        if(len(s1) + len(s2) != len(s3)):
            return False
        while True:
            if(s1 == s2 and s2 == s3 and s3 == ""):
                res1 = True
                break

            if(i >= len(s1) and j >= len(s2)):
                # We still need to handle base case.
                if(k >= len(s3)):
                    res1 = True
                    break
                res1 = False
                break

            if(i < len(s1) and s1[i] == s3[k]):
                while(i < len(s1) and s1[i] == s3[k]):
                    i += 1
                    k += 1
                # i += 1
                # k += 1

            elif(j < len(s2) and s2[j] == s3[k]):
                while(j < len(s2) and s2[j] == s3[k]):
                    j += 1
                    k += 1

            elif(k >= len(s3)):
                res1 = True
                break
            else:
                res1 = False
                break

        i = 0
        j = 0
        k = 0
        res2 = False
        while True:
            if(s1 == s2 and s2 == s3 and s3 == ""):
                res2 = True
                break

            if(i >= len(s1) and j >= len(s2)):
                # We still need to handle base case.
                if(k >= len(s3)):
                    res2 = True
                    break
                res2 = False
                break
            if(j < len(s2) and s2[j] == s3[k]):
                while(j < len(s2) and s2[j] == s3[k]):
                    j += 1
                    k += 1
            elif(i < len(s1) and s1[i] == s3[k]):
                while(i < len(s1) and s1[i] == s3[k]):
                    i += 1
                    k += 1

            elif(k >= len(s3)):
                res2 = True
                break
            else:
                res2 = False
                break

        return any([res1, res2])


# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbbaccc"

# s1 = ""
# s2 = ""
# s3 = ""

# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbcbcac"

s1 = "aa"
s2 = "ab"
s3 = "aaba"

print(Solution().isInterleave(s1, s2, s3))
