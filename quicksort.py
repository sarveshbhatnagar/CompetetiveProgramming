class Solution:

    def partition(self, arr):
        pivot = arr[-1]
        i = 0  # Looks for elem greater to swap with j.
        j = len(arr)-2  # Looks for elem smaller to swap with i.
        # if(len(arr) == 0):
        #     return [], [], []
        if(len(arr) == 1):
            return [], arr, []
        if(len(arr) == 2):
            return [min(arr)], max(arr), []
        while True:
            if(arr[i] < pivot):
                i += 1
                continue
            if(arr[j] > pivot):
                j -= 1
                continue
            if(j < i):
                # Swap pivot with i element.
                arr[i], arr[-1] = pivot, arr[i]
                break
            # Swap i and j
            arr[i], arr[j] = arr[j], arr[i]
        return arr[:i], arr[i], arr[i+1:]

    def quickSort(self, arr):
        left, pivot, right = self.partition(arr)
        if(not left and not right):
            return pivot
        if(not right):
            return self.quickSort(left) + [pivot]

        return self.quickSort(left) + [pivot] + self.quickSort(right)


arr = [1, 4, 3, 2, 5, 6]
print(Solution().quickSort(arr))
