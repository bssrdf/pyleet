'''

-Medium-
*DP*

There is a 3 lane road of length n that consists of n + 1 points labeled from 0 to n. A frog starts at point 0 in the second lane and wants to jump to point n. However, there could be obstacles along the way.

You are given an array obstacles of length n + 1 where each obstacles[i] (ranging from 0 to 3) describes an obstacle on the lane obstacles[i] at point i. If obstacles[i] == 0, there are no obstacles at point i. There will be at most one obstacle in the 3 lanes at each point.

For example, if obstacles[2] == 1, then there is an obstacle on lane 1 at point 2.
The frog can only travel from point i to point i + 1 on the same lane if there is not an obstacle on the lane at point i + 1. To avoid obstacles, the frog can also perform a side jump to jump to another lane (even if they are not adjacent) at the same point if there is no obstacle on the new lane.

For example, the frog can jump from lane 3 at point 3 to lane 1 at point 3.
Return the minimum number of side jumps the frog needs to reach any lane at point n starting from lane 2 at point 0.

Note: There will be no obstacles on points 0 and n.

 

Example 1:


Input: obstacles = [0,1,2,3,0]
Output: 2 
Explanation: The optimal solution is shown by the arrows above. There are 2 side jumps (red arrows).
Note that the frog can jump over obstacles only when making side jumps (as shown at point 2).
Example 2:


Input: obstacles = [0,1,1,3,3,0]
Output: 0
Explanation: There are no obstacles on lane 2. No side jumps are required.
Example 3:


Input: obstacles = [0,2,1,0,3,0]
Output: 2
Explanation: The optimal solution is shown by the arrows above. There are 2 side jumps.
 

Constraints:

obstacles.length == n + 1
1 <= n <= 5 * 105
0 <= obstacles[i] <= 3
obstacles[0] == obstacles[n] == 0



'''

from typing import List
from random import randint

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        O, n = obstacles, len(obstacles)-1
        dp = [[float('inf')]*3 for _ in range(n+1)]
        dp[n][0] = dp[n][1] = dp[n][2] = 0
        for i in range(n-1, -1, -1):
            o = O[i] - 1
            if o != 0: 
               dp[i][0] = min(dp[i+1][0], 1+dp[i+1][1] if o != 1 else float('inf'), 1+dp[i+1][2] if o != 2 else float('inf')) 
            if o != 1:
               dp[i][1] = min(dp[i+1][1], 1+dp[i+1][0] if o != 0 else float('inf'), 1+dp[i+1][2] if o != 2 else float('inf'))
            if o != 2:
               dp[i][2] = min(dp[i+1][2], 1+dp[i+1][1] if o != 1 else float('inf'), 1+dp[i+1][0] if o != 0 else float('inf'))
        # for i in range(3):
        #     for j in range(n+1):            
        #         print(dp[j][i],end=' ')
        #     print("\n")
        return dp[0][1]
    
    def minSideJumps2(self, obstacles: List[int]) -> int:
        O, n = obstacles, len(obstacles)-1
        dp = [[float('inf')]*3 for _ in range(n+1)]
        dp[n][0] = dp[n][1] = dp[n][2] = 0
        for i in range(n-1, -1, -1):
            o = O[i] - 1
            if o == -1:
                dp[i][0] = min(dp[i+1][0], 1+dp[i+1][1], 1+dp[i+1][2]) 
                dp[i][1] = min(dp[i+1][1], 1+dp[i+1][0], 1+dp[i+1][2])
                dp[i][2] = min(dp[i+1][2], 1+dp[i+1][1], 1+dp[i+1][0])
            elif o == 0:
                dp[i][1] = min(dp[i+1][1], 1+dp[i+1][2])
                dp[i][2] = min(dp[i+1][2], 1+dp[i+1][1])
            elif o == 1:
                dp[i][0] = min(dp[i+1][0], 1+dp[i+1][2]) 
                dp[i][2] = min(dp[i+1][2], 1+dp[i+1][0])
            else:
                dp[i][0] = min(dp[i+1][0], 1+dp[i+1][1]) 
                dp[i][1] = min(dp[i+1][1], 1+dp[i+1][0])
        return dp[0][1]
    
    def minSideJumps3(self, obstacles: List[int]) -> int:
        O, n = obstacles, len(obstacles)-1
        dp_0 = [0]*3
        dp_1 = [0]*3
        for i in range(n-1, -1, -1):
            o = O[i] - 1
            if o == -1:
                dp_1[0] = min(dp_0[0], 1+dp_0[1], 1+dp_0[2]) 
                dp_1[1] = min(dp_0[1], 1+dp_0[0], 1+dp_0[2])
                dp_1[2] = min(dp_0[2], 1+dp_0[1], 1+dp_0[0])
            elif o == 0:
                dp_1[0] = float('inf')
                dp_1[1] = min(dp_0[1], 1+dp_0[2])
                dp_1[2] = min(dp_0[2], 1+dp_0[1])
            elif o == 1:
                dp_1[1] = float('inf')
                dp_1[0] = min(dp_0[0], 1+dp_0[2])
                dp_1[2] = min(dp_0[2], 1+dp_0[0])
            else:
                dp_1[2] = float('inf')
                dp_1[0] = min(dp_0[0], 1+dp_0[1])
                dp_1[1] = min(dp_0[1], 1+dp_0[0])
            dp_0, dp_1 = dp_1, dp_0
            # print(i, dp_0)
        return dp_0[1]
    
    def minSideJumps4(self, obstacles: List[int]) -> int:
        O, n = obstacles, len(obstacles)-1
        dp = [0, 0, 0]
        for i in range(n-1, -1, -1):            
            if O[i]:
                dp[O[i]-1] = float('inf')
            for k in range(3):
                if O[i] != k+1:
                    dp[k] = min(dp[k], 1+dp[(k+1)%3], 1+dp[(k+2)%3]) 
        return dp[1]
    

if __name__ == "__main__":
    print(Solution().minSideJumps(obstacles = [0,1,2,3,0]))
    print(Solution().minSideJumps3(obstacles = [0,1,2,3,0]))
    print(Solution().minSideJumps4(obstacles = [0,1,2,3,0]))
    print(Solution().minSideJumps(obstacles = [0,1,1,3,3,0]))
    print(Solution().minSideJumps4(obstacles = [0,1,1,3,3,0]))
    print(Solution().minSideJumps(obstacles = [0,2,1,0,3,0]))
    print(Solution().minSideJumps4(obstacles = [0,2,1,0,3,0]))
    N = 5*10**5
    obstacles = []
    for i in range(N):
        obstacles.append(randint(0, 3))
    obstacles[0] = 0
    obstacles[N-1] = 0
    # print(Solution().minSideJumps(obstacles = obstacles))
    # print(Solution().minSideJumps2(obstacles = obstacles))
    print(Solution().minSideJumps3(obstacles = obstacles))
    print(Solution().minSideJumps4(obstacles = obstacles))



        