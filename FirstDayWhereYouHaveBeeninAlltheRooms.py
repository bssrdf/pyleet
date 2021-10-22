'''

-Medium-

There are n rooms you need to visit, labeled from 0 to n - 1. Each day is labeled, 
starting from 0. You will go in and visit one room a day.

Initially on day 0, you visit room 0. The order you visit the rooms for the coming days 
is determined by the following rules and a given 0-indexed array nextVisit of length n:

Assuming that on a day, you visit room i,

if you have been in room i an odd number of times (including the current visit), 
on the next day you will visit a room with a lower or equal room number specified 
by nextVisit[i] where 0 <= nextVisit[i] <= i;

if you have been in room i an even number of times (including the current visit), 
on the next day you will visit room (i + 1) mod n.

Return the label of the first day where you have been in all the rooms. It can be 
shown that such a day exists. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: nextVisit = [0,0]
Output: 2
Explanation:
- On day 0, you visit room 0. The total times you have been in room 0 is 1, which is odd.
  On the next day you will visit room nextVisit[0] = 0
- On day 1, you visit room 0, The total times you have been in room 0 is 2, which is even.
  On the next day you will visit room (0 + 1) mod 2 = 1
- On day 2, you visit room 1. This is the first day where you have been in all the rooms.
Example 2:

Input: nextVisit = [0,0,2]
Output: 6
Explanation:
Your room visiting order for each day is: [0,0,1,0,0,1,2,...].
Day 6 is the first day where you have been in all the rooms.
Example 3:

Input: nextVisit = [0,1,2,0]
Output: 6
Explanation:
Your room visiting order for each day is: [0,0,1,1,2,2,3,...].
Day 6 is the first day where you have been in all the rooms.
 

Constraints:

n == nextVisit.length
2 <= n <= 10^5
0 <= nextVisit[i] <= i

The only way to get to room i+1 is when you are visiting room i and room i has been 
visited an even number of times.

After visiting room i an odd number of times, you are required to visit room nextVisit[i] 
where nextVisit[i] <= i. It takes a fixed amount of days for you to come back from 
room nextVisit[i] to room i. Then, you have visited room i even number of times.nextVisit[i]

Can you use Dynamic Programming to avoid recomputing the number of days it takes to visit 
room i from room nextVisit[i]?


'''

from typing import List

class Solution:
    def firstDayBeenInAllRooms2(self, nextVisit: List[int]) -> int:
        n, MOD = len(nextVisit), 10**9+7
        dp = 2
        preSum = [0]*(n+1)
        preSum[1] = dp
        res = dp
        for i in range(1, n-1):            
            dp = preSum[i]-preSum[nextVisit[i]]+2
            preSum[i+1] = preSum[i] + dp
            res += dp
        return res % MOD

    def firstDayBeenInAllRooms3(self, A):
        #If I were to explain further in other words, to count steps to reach room i, steps[i], 
        # you need to sum:

        # Steps to reach room i-1 for the first time, which is steps[i-1]
        # 1 step to go to nextVisit[i-1]
        # Steps to reach room i-1 for the second time, which is 
        # steps[i-1] - steps[nextVisit[i-1]], since this time we start from 
        # room nextVisit[i-1] instead of room 0
        # 1 step to finally move to room i
        # Therefore, total being 2 * steps[i-1] - steps[nextVisit[i-1]] + 2
 
        n, M = len(A), 10**9 + 7
        dp = [0]*n # Defined as number of days to reach cell i
        for i in range(1, n):
            dp[i] = (2*dp[i-1] - dp[A[i-1]] + 2) % M
        return dp[-1]  
       

    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        n = len(nextVisit)
        dp = [0]*n
        dp[0] = 2
        preSum = [0]*(n+1)
        preSum[1] = dp[0]
        for i in range(1, n):            
            #print(i, nextVisit[i], preSum[i+1], preSum[nextVisit[i]])
            dp[i] = preSum[i]-preSum[nextVisit[i]]+2
            preSum[i+1] = preSum[i] + dp[i]

        #print(dp)
        return sum(dp[:-1])%(10**9+7)

if __name__ == "__main__":
    #print(Solution().firstDayBeenInAllRooms([0,1,1,1]))
    print(Solution().firstDayBeenInAllRooms([0,0]))
    print(Solution().firstDayBeenInAllRooms([0,0,2]))
    print(Solution().firstDayBeenInAllRooms([0,1,2,0]))
    #print(Solution().firstDayBeenInAllRooms([0,1,2,3,0]))
    #print(Solution().firstDayBeenInAllRooms([0,1,0,1]))
    print(Solution().firstDayBeenInAllRooms([0,0,0,0,0,0,0,0,0,9,1,8]))
    print(Solution().firstDayBeenInAllRooms2([0,0,0,0,0,0,0,0,0,9,1,8]))