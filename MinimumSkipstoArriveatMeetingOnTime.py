'''
-Hard-
*DP*

You are given an integer hoursBefore, the number of hours you have to travel to your 
meeting. To arrive at your meeting, you have to travel through n roads. The road 
lengths are given as an integer array dist of length n, where dist[i] describes 
the length of the ith road in kilometers. In addition, you are given an integer 
speed, which is the speed (in km/h) you will travel at.

After you travel road i, you must rest and wait for the next integer hour 
before you can begin traveling on the next road. Note that you do not have to 
rest after traveling the last road because you are already at the meeting.

For example, if traveling a road takes 1.4 hours, you must wait until the 2 hour 
mark before traveling the next road. If traveling a road takes exactly 2 hours, you 
do not need to wait.
However, you are allowed to skip some rests to be able to arrive on time, meaning 
you do not need to wait for the next integer hour. Note that this means you 
may finish traveling future roads at different hour marks.

For example, suppose traveling the first road takes 1.4 hours and traveling 
the second road takes 0.6 hours. Skipping the rest after the first road will 
mean you finish traveling the second road right at the 2 hour mark, letting you 
start traveling the third road immediately.
Return the minimum number of skips required to arrive at the meeting on time, 
or -1 if it is impossible.

 

Example 1:

Input: dist = [1,3,2], speed = 4, hoursBefore = 2
Output: 1
Explanation:
Without skipping any rests, you will arrive in (1/4 + 3/4) + (3/4 + 1/4) + (2/4) = 2.5 hours.
You can skip the first rest to arrive in ((1/4 + 0) + (3/4 + 0)) + (2/4) = 1.5 hours.
Note that the second rest is shortened because you finish traveling the second road at an integer hour due to skipping the first rest.
Example 2:

Input: dist = [7,3,5,5], speed = 2, hoursBefore = 10
Output: 2
Explanation:
Without skipping any rests, you will arrive in (7/2 + 1/2) + (3/2 + 1/2) + (5/2 + 1/2) + (5/2) = 11.5 hours.
You can skip the first and third rest to arrive in ((7/2 + 0) + (3/2 + 0)) + ((5/2 + 0) + (5/2)) = 10 hours.
Example 3:

Input: dist = [7,3,5,5], speed = 1, hoursBefore = 10
Output: -1
Explanation: It is impossible to arrive at the meeting on time even if you skip all the rests.
 

Constraints:

n == dist.length
1 <= n <= 1000
1 <= dist[i] <= 105
1 <= speed <= 106
1 <= hoursBefore <= 107

'''

from typing import List
import math

class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        n, eps = len(dist), 1e-9
        dp = [[10**10]*(n+1) for _ in range(n+1)]
        dp[0][0] = 0
        for i in range(1, n+1):
            d = dist[i-1]/speed
            # dp[i][0] = math.ceil(time)+dist[i-1]/speed 
            dp[i][0] = math.ceil(dp[i-1][0]+d-eps) 
            # time = dp[i][0]
            # ctime = math.ceil(time) - time
            for j in range(1, i+1):
            #    dp[i][j] = min(dp[i-1][j]+(ctime if i < n else 0), dp[i-1][j-1]) + dist[i-1]/speed
               dp[i][j] = min(math.ceil(dp[i-1][j]+d-eps), dp[i-1][j-1]+d)
        for i in range(n+1):
            if dp[n][i] <= hoursBefore:
                return i 
        return -1 
    

if __name__ == "__main__":
    # print(Solution().minSkips(dist = [1,3,2], speed = 4, hoursBefore = 2))
    # print(Solution().minSkips(dist = [7,3,5,5], speed = 2, hoursBefore = 10))
    # print(Solution().minSkips(dist = [7,3,5,5], speed = 1, hoursBefore = 10))
    print(Solution().minSkips(dist = [1,2,3,4,5], speed = 1000000, hoursBefore = 1))
