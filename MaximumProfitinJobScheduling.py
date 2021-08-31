'''
-Hard-

We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], 
obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there 
are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

 

Example 1:



Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
Example 2:



Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.
Example 3:



Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6
 

Constraints:

1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
1 <= startTime[i] < endTime[i] <= 10^9
1 <= profit[i] <= 10^4

Hints:

Think on DP.

Sort the elements by starting time, then define the dp[i] as the maximum profit taking elements 
from the suffix starting at i.

Use binarySearch (lower_bound/upper_bound on C++) to get the next index for the DP transition.

'''
import bisect

class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [[0, 0]]
        for s, e, p in jobs:
            i = bisect.bisect(dp, [s + 1]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]
    
    def jobSchedulingDP(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        n = len(jobs)
        dp = [0] * n
        dp[0] = jobs[0][2]
        def search(index):
            left, right = 0, index-1
            while left <= right:
                mid = left + (right-left)//2
                if jobs[mid][1] <= jobs[index][0]:
                    if jobs[mid + 1][1] <= jobs[index][0]:
                        left = mid + 1
                    else:
                        return mid
                else:
                    right = mid - 1
            return -1
        for i in range(1, n):
            #print(i, jobs[i])
            l = search(i)
            profit = jobs[i][2]
            if l != -1:
                profit += dp[l]
            dp[i] = max(dp[i-1], profit)
        return dp[n-1]
        
if __name__ == "__main__":
    print(Solution().jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]))
    print(Solution().jobSchedulingDP(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]))
    print(Solution().jobSchedulingDP([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60]))