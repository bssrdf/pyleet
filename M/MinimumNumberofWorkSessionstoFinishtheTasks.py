'''
-Medium-
*DP*
*Bitmask*
There are n tasks assigned to you. The task times are represented as an integer array tasks of length n, 
where the ith task takes tasks[i] hours to finish. A work session is when you work for at most sessionTime 
consecutive hours and then take a break.

You should finish the given tasks in a way that satisfies the following conditions:

If you start a task in a work session, you must complete it in the same work session.
You can start a new task immediately after finishing the previous one.
You may complete the tasks in any order.
Given tasks and sessionTime, return the minimum number of work sessions needed to finish all the tasks 
following the conditions above.

The tests are generated such that sessionTime is greater than or equal to the maximum element in tasks[i].

 

Example 1:

Input: tasks = [1,2,3], sessionTime = 3
Output: 2
Explanation: You can finish the tasks in two work sessions.
- First work session: finish the first and the second tasks in 1 + 2 = 3 hours.
- Second work session: finish the third task in 3 hours.
Example 2:

Input: tasks = [3,1,3,1,1], sessionTime = 8
Output: 2
Explanation: You can finish the tasks in two work sessions.
- First work session: finish all the tasks except the last one in 3 + 1 + 3 + 1 = 8 hours.
- Second work session: finish the last task in 1 hour.
Example 3:

Input: tasks = [1,2,3,4,5], sessionTime = 15
Output: 1
Explanation: You can finish all the tasks in one work session.
 

Constraints:

n == tasks.length
1 <= n <= 14
1 <= tasks[i] <= 10
max(tasks[i]) <= sessionTime <= 15


'''

from functools import lru_cache

class Solution(object):
    def minSessions(self, tasks, sessionTime):
        """
        :type tasks: List[int]
        :type sessionTime: int
        :rtype: int
        """
        tasks.sort()
        n = len(tasks)
        allOnes = (1 << n) - 1
        @lru_cache(None)
        def backtrack(mask, currTime):
            if currTime > sessionTime: return float('inf')
            if mask == allOnes: return 1
            #if(dp[mask][currTime] != -1) return dp[mask][currTime];
            ans = float('inf')
            for i in range(n):
                if (mask & (1<<i)) == 0:
                    includeInCurrentSession = backtrack(mask | (1<<i), currTime + tasks[i])
                    includeInNextSession = 1 + backtrack(mask | (1<<i), tasks[i])
                    ans = min(ans, includeInCurrentSession, includeInNextSession)
            return ans
        return backtrack(0, 0)

    def minSessionsDpBit(self, tasks, sessionTime):
        """
        :type tasks: List[int]
        :type sessionTime: int
        :rtype: int
        """
        n = len(tasks)
        T = sessionTime
        @lru_cache(None)
        def dp(mask):
            if mask == 0: return (1, 0) # base case, about to start the 1st session
            ans = (float("inf"), float("inf"))
            for j in range(n):
                if mask & (1<<j): 
                    pieces, last = dp(mask - (1 << j)) # find the total # of sessions and time over the 
                                                       # last accumulated without taking j-th task
                    full = (last + tasks[j] > T)   # now account for j-th task
                    # if tasks[j] > T, we got one more sessions
                    # otherwise, j-th task can stay in the last session
                    ans = min(ans, (pieces + full, tasks[j] + (1-full)*last))  
            return ans

        return dp((1<<n) - 1)[0]
        
                

if __name__ == "__main__":
    print(Solution().minSessions(tasks = [3,1,3,1,1], sessionTime = 8))
    print(Solution().minSessionsDpBit(tasks = [3,1,3,1,1], sessionTime = 8))