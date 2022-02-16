import heapq


class Solution:
    def longestVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        prev = 0
        my_heap = []
        for i in range(len(s)):
            if s[i] in vowels:
                prev += 1
                continue

            if prev != 0:
                if(len(my_heap) == 0):
                    heapq.heappush(my_heap, -prev)
                else:
                    heapq.heappush(my_heap, -prev)
                # my_heap.push(-prev)
                prev = 0

        fsum = 0
        for i in range(k):
            fsum += heapq.heappop(my_heap)

        return -fsum


print(Solution().longestVowels("letsgosomewhere", 2))
