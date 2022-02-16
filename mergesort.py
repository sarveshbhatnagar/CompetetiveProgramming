class Solution:

    def merge(self, left, right):
        """
        Merge two sorted arrays
        """
        res = []
        i = 0
        j = 0

        while i < len(left) or j < len(right):
            if(i >= len(left)):
                return res + right[j:]

            if(j >= len(right)):
                return res + left[i:]

            if(left[i] < right[j]):
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1

        return res

    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr

        # Recursive Step
        left_arr = self.mergeSort(arr[:len(arr)//2])
        right_arr = self.mergeSort(arr[len(arr)//2:])

        # Merge Step
        return self.merge(left_arr, right_arr)


arr = [2, 3, 4, 6, 5, 1]

print(Solution().mergeSort(arr))
