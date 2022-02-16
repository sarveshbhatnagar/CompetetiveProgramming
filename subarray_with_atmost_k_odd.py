from collections import deque


class Solution:
    def subarray_bruteforce(self, arr):
        subarrays = []

        for i in range(len(arr)):
            d = []
            d.append(arr[i])
            for j in range(i+1, len(arr)):
                d.append(arr[j])
                subarrays.append(d[:])

        for i in arr:
            subarrays.append([i])

        return subarrays

    def isValid(self, arr, k):
        """
        check if the logic holds for subarray.
        In this case, atmost k. (distinct in another pass)
        """
        count_odd = 0
        for i in arr:
            if i % 2 == 1:
                count_odd += 1
        if count_odd <= k:
            return True
        return False

    def subarray_with_atmost_k_odd(self, arr, k):
        subarrays = []
        # edge case: len == 1
        if len(arr) == 1:
            if(self.isValid(arr)):
                return [arr]

        i = 0
        j = 1
        count_odd = 0
        odd_positions = set()
        if(arr[i] % 2 == 1):
            count_odd += 1
            odd_positions.add(i)
        while True:
            if j > len(arr) and i == j:
                break

            if i >= j:
                break

            if(arr[j] % 2 == 1):
                count_odd += 1
                odd_positions.add(j)

            if(count_odd > k):
                while count_odd > k:
                    if(arr[i] % 2 == 1):
                        count_odd -= 1
                        odd_positions.remove(i)
                    i += 1

            subarrays.append(arr[i:j+1])

            if(j < len(arr)-1):
                j += 1
            else:
                i += 1

            # print(i, j)

        # edge case: single elements, after this.
        for i in arr:
            subarrays.append([i])

        # Removing duplicates
        subarrays = list(set(tuple(x) for x in subarrays))
        subarrays = [list(x) for x in subarrays]
        return len(subarrays)


# arr = [1, 3, 9, 5]
k = 1

arr = [3, 2, 3, 2]

# arr = [3, 2, 3, 4]

print(Solution().subarray_with_atmost_k_odd(arr, k))
# print(Solution().subarray_bruteforce([3, 2, 3, 4]))
