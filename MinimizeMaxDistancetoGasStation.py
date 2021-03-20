'''

-Medium-

On a horizontal number line, we have gas stations at positions stations[0], 
stations[1], ..., stations[N-1], where N = stations.length.

Now, we add K more gas stations so that D, the maximum distance between 
adjacent gas stations, is minimized.

Return the smallest possible value of D.

Example:

Input: stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9
Output: 0.500000
Note:

stations.length will be an integer in range [10, 2000].
stations[i] will be an integer in range [0, 10^8].
K will be an integer in range [1, 10^6].
Answers within 10^-6 of the true value will be accepted as correct.

'''


class Solution(object):

    def minmaxGasDist(self, stations, K):
        n = len(stations)
        dist = [ i-j for i,j in zip(stations[1:], stations[:-1])]
        def condition(mid):
            cnt = 0
            for i in range(1, n):                
                cnt += int((stations[i]-stations[i-1])/mid)
            return cnt <= K

        l, r = 0, max(dist)
        while r-l > 1.e-6:
            mid = l + (r-l)/2
            if condition(mid):
            #if feasible(mid):
                r = mid
            else:
                l = mid
        return l


if __name__ == "__main__":
    print(Solution().minmaxGasDist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9))
    print(Solution().minmaxGasDist([3,6,12,19,33,44,67,72,89,95], 2))
