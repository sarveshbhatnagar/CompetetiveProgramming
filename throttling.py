
# I changed the first if statement to the following:
# if(i > 2 && requestTime.get(i) - requestTime.get(i-3) < 1)
class Solution:
    def droppedRequests(self, requestTime: list) -> int:

        dropped = 0

        for i, _ in enumerate(requestTime):
            if i > 2 and requestTime[i] == requestTime[i-3]:
                dropped += 1
                continue

            if i > 19 and requestTime[i] - requestTime[i-20] < 10:
                dropped += 1
                continue

            if i > 59 and requestTime[i] - requestTime[i-60] < 60:
                dropped += 1

        return dropped


requests = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4,
            5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 11, 11, 11, 11]
print(Solution().droppedRequests(requests))
