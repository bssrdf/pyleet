'''
-Hard-

*DP*
*Sorting*


There are some robots and factories on the X-axis. You are given an integer array robot where robot[i] is the position of the ith robot. You are also given a 2D integer array factory where factory[j] = [positionj, limitj] indicates that positionj is the position of the jth factory and that the jth factory can repair at most limitj robots.

The positions of each robot are unique. The positions of each factory are also unique. Note that a robot can be in the same position as a factory initially.

All the robots are initially broken; they keep moving in one direction. The direction could be the negative or the positive direction of the X-axis. When a robot reaches a factory that did not reach its limit, the factory repairs the robot, and it stops moving.

At any moment, you can set the initial direction of moving for some robot. Your target is to minimize the total distance traveled by all the robots.

Return the minimum total distance traveled by all the robots. The test cases are generated such that all the robots can be repaired.

Note that

All robots move at the same speed.
If two robots move in the same direction, they will never collide.
If two robots move in opposite directions and they meet at some point, they do not collide. They cross each other.
If a robot passes by a factory that reached its limits, it crosses it as if it does not exist.
If the robot moved from a position x to a position y, the distance it moved is |y - x|.
 

Example 1:


Input: robot = [0,4,6], factory = [[2,2],[6,2]]
Output: 4
Explanation: As shown in the figure:
- The first robot at position 0 moves in the positive direction. It will be repaired at the first factory.
- The second robot at position 4 moves in the negative direction. It will be repaired at the first factory.
- The third robot at position 6 will be repaired at the second factory. It does not need to move.
The limit of the first factory is 2, and it fixed 2 robots.
The limit of the second factory is 2, and it fixed 1 robot.
The total distance is |2 - 0| + |2 - 4| + |6 - 6| = 4. It can be shown that we cannot achieve a better total distance than 4.
Example 2:


Input: robot = [1,-1], factory = [[-2,1],[2,1]]
Output: 2
Explanation: As shown in the figure:
- The first robot at position 1 moves in the positive direction. It will be repaired at the second factory.
- The second robot at position -1 moves in the negative direction. It will be repaired at the first factory.
The limit of the first factory is 1, and it fixed 1 robot.
The limit of the second factory is 1, and it fixed 1 robot.
The total distance is |2 - 1| + |(-2) - (-1)| = 2. It can be shown that we cannot achieve a better total distance than 2.
 

Constraints:

1 <= robot.length, factory.length <= 100
factory[j].length == 2
-109 <= robot[i], positionj <= 109
0 <= limitj <= robot.length
The input will be generated such that it is always possible to repair every robot.




'''

from typing import List
import heapq
from collections import deque
from functools import lru_cache

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # Greedy not working
        pq = []
        R, F = robot, factory
        n, m = len(robot), len(factory)
        for i in range(n):
            for j in range(m):
                heapq.heappush(pq, (abs(R[i]-F[j][0]), i, j))
        ans, cnt, visited = 0, 0, [False]*n
        while pq and cnt < n:
            d, i, j = heapq.heappop(pq)            
            if not visited[i] and F[j][1] > 0:
                ans += d
                visited[i] = True
                cnt += 1
                F[j][1] -= 1
        return ans

    def minimumTotalDistance2(self, robot: List[int], factory: List[List[int]]) -> int:
        R, F = robot, factory
        inf = float('inf')
        R.sort()
        F.sort()
        @lru_cache(None)
        def dp(i, j, k):
            if i == len(R): return 0
            if j == len(F): return inf
            res1 = dp(i, j + 1, 0)
            res2 = dp(i + 1, j, k + 1) + abs(R[i] - F[j][0]) if F[j][1] > k else inf
            return min(res1, res2)
        return dp(0, 0, 0)
    
    def minimumTotalDistance3(self, robot: List[int], factory: List[List[int]]) -> int:
        R, F = robot, factory
        n, m = len(R), len(F)
        inf = float('inf')
        dp = [inf] * (n + 1)
        dp[n] = 0
        R.sort()
        F.sort()
        for j in range(m-1,-1,-1):
            for i in range(n):
                cur = 0
                for k in range(1, min(F[j][1], n - i) + 1):
                    cur += abs(R[i + k - 1] - F[j][0])
                    dp[i] = min(dp[i], dp[i + k] + cur)
        return dp[0]

    def minimumTotalDistance4(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        inf = float('inf')
        m, n = len(robot), len(factory)
        dp = [[0]*(n+1) for _ in range(m+1)] 
        for i in range(m): dp[i][-1] = inf 
        for j in range(n-1, -1, -1): 
            prefix = 0 
            qq = deque([(m, 0)])
            for i in range(m-1, -1, -1): 
                prefix += abs(robot[i] - factory[j][0])
                if qq[0][0] > i+factory[j][1]: qq.popleft()
                while qq and qq[-1][1] >= dp[i][j+1] - prefix: qq.pop()
                qq.append((i, dp[i][j+1] - prefix))
                dp[i][j] = qq[0][1] + prefix
        return dp[0][0]
    
    def minimumTotalDistance5(self, robot: List[int], factory: List[List[int]]) -> int:
        # typical DP solution
        # Time O(mnk)
        # space O(mn)

        robot.sort()
        factory.sort()
        inf = float('inf')
        m, n = len(robot), len(factory)
        dp = [[0]*(n+1) for _ in range(m+1)] 
        # define dp[i][j] as the minimum moves to fix robot[i:] with factory[j:]. 
        # Clearly, dp[0][0] is the desired answer. The recurrence relation is

        # dp[i][j] = min(dp[i][j+1], 
		# 	            |robot[i] - pos| + dp[i+1][j+1], 
		# 	            |robot[i] - pos| + |robot[i+1] - pos| + dp[i+2][j+1], 
		# 	            ...
		# 	            |robot[i] - pos| + ... + |robot[i+limit-1] - pos| + dp[i+limit][j+1])
        for i in range(m): dp[i][-1] = inf # base case: no factory to repair any robots
        for j in range(n-1, -1, -1): 
            pos, limit = factory[j]
            for i in range(m-1, -1, -1): 
                prefix = abs(robot[i] - pos)
                dp[i][j] = dp[i][j+1] # let i be repaird by factory j+1, ...
                for k in range(i+1, min(m, i+limit)): # factory j repairs i, i+1, ... k-1                    
                    dp[i][j] = min(dp[i][j], prefix + dp[k][j+1])
                    # if k == i+limit or k == m:
                    #     break
                    prefix += abs(robot[k] - pos)
                dp[i][j] = min(dp[i][j], prefix + dp[min(m,i+limit)][j+1])
        return dp[0][0]
        

        

if __name__ == "__main__":   
    # print(Solution().minimumTotalDistance(robot = [0,4,6], factory = [[2,2],[6,2]]))
    # print(Solution().minimumTotalDistance(robot = [1,-1], factory = [[-2,1],[2,1]]))
    robot = [670355988,403625544,886437985,224430896,126139936,-477101480,-868159607,-293937930]
    factory = [[333473422,7],[912209329,7],[468372740,7],[-765827269,4],[155827122,4],[635462096,2],[-300275936,2],[-115627659,0]]
    print(Solution().minimumTotalDistance4(robot = robot, factory = factory))
    print(Solution().minimumTotalDistance5(robot = robot, factory = factory))
    robot = [9,11,99,101]
    factory = [[10,1],[7,1],[14,1],[100,1],[96,1],[103,1]]
    print(Solution().minimumTotalDistance4(robot = robot, factory = factory))
    print(Solution().minimumTotalDistance5(robot = robot, factory = factory))