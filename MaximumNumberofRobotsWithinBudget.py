'''

You have n robots. You are given two 0-indexed integer arrays, chargeTimes and runningCosts, both of length n. The ith robot costs chargeTimes[i] units to charge and costs runningCosts[i] units to run. You are also given an integer budget.

The total cost of running k chosen robots is equal to max(chargeTimes) + k * sum(runningCosts), where max(chargeTimes) is the largest charge cost among the k robots and sum(runningCosts) is the sum of running costs among the k robots.

Return the maximum number of consecutive robots you can run such that the total cost does not exceed budget.

 

Example 1:

Input: chargeTimes = [3,6,1,3,4], runningCosts = [2,1,3,4,5], budget = 25
Output: 3
Explanation: 
It is possible to run all individual and consecutive pairs of robots within budget.
To obtain answer 3, consider the first 3 robots. The total cost will be max(3,6,1) + 3 * sum(2,1,3) = 6 + 3 * 6 = 24 which is less than 25.
It can be shown that it is not possible to run more than 3 consecutive robots within budget, so we return 3.
Example 2:

Input: chargeTimes = [11,12,19], runningCosts = [10,8,7], budget = 19
Output: 0
Explanation: No robot can be run that does not exceed the budget, so we return 0.
 

Constraints:

chargeTimes.length == runningCosts.length == n
1 <= n <= 5 * 104
1 <= chargeTimes[i], runningCosts[i] <= 105
1 <= budget <= 1015


'''
from typing import List
from collections import deque

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        #O(NlogN)
        C, R, n = chargeTimes, runningCosts, len(runningCosts)
        l, r = 0, n+1
        preSum = [0]*(n+1)
        for i in range(n):
            preSum[i+1] = preSum[i] + R[i]  
        def canRun(k):
            if k == 0: return True
            dq = deque()
            for i in range(n):
                j = i - k + 1
                while dq and C[dq[-1]] < C[i]:
                    dq.pop()            
                dq.append(i)
                if i >= k and dq[0] < j:
                    dq.popleft()
                if j >= 0 and C[dq[0]] + k*(preSum[i+1]-preSum[j]) <= budget:
                    return True 
            return False 

        while l < r:
            mid = l + (r-l)//2
            if canRun(mid):
                l = mid + 1
            else:
                r = mid
        return l-1

    def maximumRobots2(self, times: List[int], costs: List[int], budget: int) -> int:
        # O(N)
        cur = i = 0
        n = len(times)
        d = deque()
        for j in range(n):
            cur += costs[j]
            while d and times[d[-1]] <= times[j]:
                d.pop()
            d.append(j)
            if times[d[0]] + (j - i + 1) * cur > budget:
                if d[0] == i:
                    d.popleft()
                cur -= costs[i]
                i += 1
        return n - i
    
    def maximumRobots3(self, times: List[int], costs: List[int], budget: int) -> int:
        # O(N)
        cur = i = 0
        n = len(times)
        d = deque()
        ans = 0
        for j in range(n):
            cur += costs[j]
            while d and times[d[-1]] <= times[j]:
                d.pop()
            d.append(j)
            while d and times[d[0]] + (j - i + 1) * cur > budget:
                if d[0] == i:
                    d.popleft()
                cur -= costs[i]
                i += 1
            ans = max(ans, j-i+1)
        return ans
        




if __name__ == "__main__":
    print(Solution().maximumRobots(chargeTimes = [3,6,1,3,4], runningCosts = [2,1,3,4,5], budget = 25))
    print(Solution().maximumRobots(chargeTimes = [11,12,19], runningCosts = [10,8,7], budget = 19))
    C = [32,83,96,70,98,80,30,42,63,67,49,10,80,13,69,91,73,10]
    R = [49,67,92,26,18,22,38,34,36,26,32,84,39,42,88,51,8,2]
    print(Solution().maximumRobots(chargeTimes = C, runningCosts= R, budget=599))
    print(Solution().maximumRobots3(C, R, 599))