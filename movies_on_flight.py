# https://leetcode.com/discuss/interview-question/313719/Amazon-or-Online-Assessment-2019-or-Movies-on-Flight

class Solution:
    def moviesOnFlight(self, movieDuration, d):
        # we need d-30 maximum.
        d = d-30
        # keep all indexes in hashmap
        # key: movie duration, value: index
        hm = dict()
        for i in range(len(movieDuration)):
            hm[movieDuration[i]] = i

        movieDuration = sorted(movieDuration, reverse=True)

        i = 0
        j = len(movieDuration)-1
        iidx = 0
        jidx = len(movieDuration)-1
        max_d = 0
        while i < j:
            if movieDuration[i] + movieDuration[j] <= d:
                prev_max = max_d
                max_d = max(max_d, movieDuration[i] + movieDuration[j])
                if(prev_max != max_d):
                    iidx = i
                    jidx = j
                j -= 1
            else:
                i += 1

        z = hm[movieDuration[iidx]], hm[movieDuration[jidx]]

        return max_d, min(z), max(z)


print(Solution().moviesOnFlight([90, 85, 75, 60, 120, 150, 125], 250))
