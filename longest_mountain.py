
from typing import List


# class Solution:
#     def longestMountain(self, arr: List[int]) -> int:
#         # Learn Double Counter Technique
#         # Learn Double Pointer Technique

#         # Triple Counter
#         max_mountain = 0

#         i = 1
#         j = 1
#         k = 1

#         while(i < len(arr) and j < len(arr) and k < len(arr)):
#             # We have 3 cases.
#             # 1. We are at the beginning of a mountain. (i)
#             # 2. We care climbing the mountain. (j)
#             # 3. We are descending the mountain. (k)
#             #
#             if(i == j):
#                 if(arr[i] > arr[i-1]):
#                     # Ascend ready from i-1.
#                     j = i
#                     i = i-1
#                 else:
#                     i += 1
#                     j = i
#                     k = i
#             if(j > i and j == k):
#                 # Keep ascending.
#                 if(arr[j] > arr[j-1]):
#                     j += 1
#                     k = j
#                 elif (arr[j] == arr[j-1]):
#                     # max_mountain = max(max_mountain, j-1-i)
#                     i = j
#                     k = j
#                 else:
#                     # We are descending.
#                     k = j
#                     j = j-1
#             if(k > j):
#                 # Keep descending.

#                 if(arr[k] == arr[k-1]):
#                     # Its not descending so stop.
#                     if(k-i >= 3):
#                         max_mountain = max(max_mountain, k-i)
#                     i = k
#                     j = k
#                     continue
#                 if(arr[k] < arr[k-1]):
#                     k += 1
#                 else:
#                     # Mountain is over, restart.
#                     # Length of mountain:
#                     max_mountain = max(max_mountain, k-i)
#                     k = k-1
#                     i = k
#                     j = k

#         if(k > j):
#             max_mountain = max(max_mountain, k-i)

#         if(max_mountain > 2):
#             return max_mountain

#         return 0
#         # pass


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        icount = 1
        jcount = 1
        i = 1
        j = 1

        max_mountain = 0

        while i < len(arr) and j < len(arr):
            if(arr[i-1] < arr[i] and j == i):
                # If curr value > prev value, then we are increasing icount.
                # We are also shifting i and j together.
                icount += 1
                i += 1
                j += 1
                continue
            elif(arr[i-1] == arr[i] and j == i):
                # If curr value == prev value, then we are shifting i and j together.
                i += 1
                j += 1
                icount = 1
                continue
            elif(arr[i-1] > arr[i] and j == i):
                # It means that previous element is the top of the mountain.
                # We will increase jcount and j.
                if(icount >= 2):
                    jcount += 1
                    j += 1
                    continue
                else:
                    i += 1
                    j += 1
                    icount = 1
                    jcount = 1
                    continue
            elif(arr[j] < arr[j-1] and j > i):
                # We are increasing jcount.
                jcount += 1
                j += 1
                continue
            elif(arr[j] > arr[j-1] and j > i):

                max_mountain = max(max_mountain, jcount+icount)
                icount = 2
                jcount = 1
                j += 1
                i = j
                continue
            elif(arr[j] == arr[j-1] and j > i):
                # Update max mountain, reset everything.
                max_mountain = max(max_mountain, jcount+icount)
                icount = 1
                jcount = 1
                j += 1
                i = j
        # We also have to check if last mountain was valid.
        if(jcount+icount >= 3 and jcount > 1):
            # print(jcount+icount)
            max_mountain = max(max_mountain, jcount+icount)

        if(max_mountain > 3):
            return max_mountain-1
        return 0


# arr = [0, 0, 1, 0, 0, 1, 1, 1, 1, 1]
# arr = [2, 1, 4, 7, 3, 2, 5]
# arr = [0, 2, 0, 2, 1, 2, 3, 4, 4, 1]
# arr = [0, 2, 2]
# arr = [1, 2, 3, 4, 5, 6, 6, 6]
arr = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
print(Solution().longestMountain(arr))
