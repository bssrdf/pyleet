'''

-Hard-

You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the i-th job, 
you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum of 
difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of 
a job done in that day.

Given an array of integers jobDifficulty and an integer d. The difficulty of the i-th job 
is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.

 

Example 1:


Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7 
Example 2:

Input: jobDifficulty = [9,9,9], d = 4
Output: -1
Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.
Example 3:

Input: jobDifficulty = [1,1,1], d = 3
Output: 3
Explanation: The schedule is one job per day. total difficulty will be 3.
Example 4:

Input: jobDifficulty = [7,1,7,1,7,1], d = 3
Output: 15
Example 5:

Input: jobDifficulty = [11,111,22,222,33,333,44,444], d = 6
Output: 843
 

Constraints:

1 <= jobDifficulty.length <= 300
0 <= jobDifficulty[i] <= 1000
1 <= d <= 10


'''

from  functools import lru_cache

class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        inf = float('inf')
        n = len(jobDifficulty)
        @lru_cache(None)
        def dp(start, days, diff):
            if start == n:
                if days == 0:
                    return diff
                else:
                    return inf 
            if days == 0 :
                return inf
            ans = inf
            mi = 0
            for i in range(start, n-days+1):
                mi = max(mi, jobDifficulty[i])
                newd = diff + mi 
                if newd < ans:
                    ans = min(ans, dp(i+1, days-1, newd))
            return ans
        res = dp(0, d, 0)
        return -1 if res == inf else res

    def minDifficulty2(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        inf = float('inf')
        n = len(jobDifficulty)
        res = [inf]
        #@lru_cache(None)
        def dp(start, days, diff):
            if start == n:
                if days == 0:
                    res[0] = min(res[0], diff)
                return 
            if days == 0: return 
            if diff >= res[0]: return  
            mi = 0
            for i in range(start, n-days+1):
                mi = max(mi, jobDifficulty[i])
                newd = diff + mi 
                if newd > res[0]:
                    break
                dp(i+1, days-1, newd)
            return 
        dp(0, d, 0)
        return -1 if res[0] == inf else res[0]

    def minDifficultyLee215(self, A, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        n = len(A)
        if n < d: return -1

        @lru_cache(None)
        def dfs(i, d):
            if d == 1:
                return max(A[i:])
            res, maxd = float('inf'), 0
            for j in range(i, n - d + 1):
                maxd = max(maxd, A[j])
                res = min(res, maxd + dfs(j + 1, d - 1))
            return res
        return dfs(0, d)

    def minDifficultyLee215BU(self, A, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        n, inf = len(A), float('inf')
        if n < d: return -1
        dp = [inf] * n + [0]
        for d in range(1, d + 1):
            for i in range(n - d + 1):
                maxd, dp[i] = 0, inf
                for j in range(i, n - d + 1):
                    maxd = max(maxd, A[j])
                    dp[i] = min(dp[i], maxd + dp[j + 1])
            print(dp)
        return dp[0]
       

if __name__ == "__main__":
    print(Solution().minDifficulty([6,5,4,3,2,1], 2))
    print(Solution().minDifficulty([9,9,9], 4))
    print(Solution().minDifficulty([1,1,1], 3))
    print(Solution().minDifficulty([7,1,7,1,7,1], 3))
    print(Solution().minDifficulty([11,111,22,222,33,333,44,444], 6))
    print(Solution().minDifficulty2([6,5,4,3,2,1], 2))
    print(Solution().minDifficulty2([9,9,9], 4))
    print(Solution().minDifficulty2([1,1,1], 3))
    print(Solution().minDifficulty2([7,1,7,1,7,1], 3))
    print(Solution().minDifficulty2([11,111,22,222,33,333,44,444], 6))
    jobs = [976,662,877,135,175,628,856,855,807,769,200,223,527,36,399,409,468,884,229,311,41,350,734,472,480,77,299,821,534,776,965,926,867,45,108,504,468,910,594,355,193,905,211,719,191,961,940,176,737,591,831,22,550,822,840,295,643,1,591,227,345,298,918,561,962,977,871,610,39,247,453,405,306,994,782,395,92,81,956,691,692,395,249,351,342,752,709,521,936,997,651,559,760,796,286,531,187,515,550,470,879,747,3,966,933,696,164,547,278,272,343,552,355,303,15,384,870,85,515,959,168,160,77]
    #print(Solution().minDifficulty(jobs, 7))
    print(Solution().minDifficulty2(jobs, 7))
    jobs = [270,340,359,593,689,75,923,738,564,582,553,776,324,871,734,259,915,195,538,247,174,82,642,44,50,786,448,762,46,526,458,443,274,859,701,466,417,917,543,87,414,69,196,372,150,106,154,611,686,15,478,260,961,248,980,387,629,233,410,637,588,786,924,137,164,501,338,205,303,28,957,851,370,17,484,187,791,340,789,866,300,499,831,300,133,811,204,536,875,87,850,451,749,905,620,990,291,713,623,741,25,133,14,7,631,249,507,136,298,47,315,841,667,88,808,173,618,715,937,877,737,313,203,579,817,596,700,787,414,41,852,152,212,246,925,304,375,307,717,734,215,464,390,192,496,796,530,666,590,0,688,141,230,20,504,24,150,952,608,878,805,709,519,798,17,439,540,516,723,898,249,606,468,75,96,390,731,43,411,7,799,816,639,405,101,567,67,881,721,16,175,248,876,461,864,48,51,474,90,508,266,72,294,545,447,343,216,909,424,432,799,533,52,377,368,961,231,56,217,638,425,9,946,206,915,428,980,686]
    print(Solution().minDifficulty2(jobs, 8))
    print(Solution().minDifficultyLee215(jobs, 8))
    #print(Solution().minDifficultyLee215BU(jobs, 8))
    print(Solution().minDifficultyLee215BU([6,5,4,3,2,1], 2))
