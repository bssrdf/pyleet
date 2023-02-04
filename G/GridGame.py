'''

-Medium-

You are given a 0-indexed 2D array grid of size 2 x n, where grid[r][c] represents the number of points at 
position (r, c) on the matrix. Two robots are playing a game on this matrix.

Both robots initially start at (0, 0) and want to reach (1, n-1). Each robot may only move to the right 
((r, c) to (r, c + 1)) or down ((r, c) to (r + 1, c)).

At the start of the game, the first robot moves from (0, 0) to (1, n-1), collecting all the points from 
the cells on its path. For all cells (r, c) traversed on the path, grid[r][c] is set to 0. Then, the 
second robot moves from (0, 0) to (1, n-1), collecting the points on its path. Note that their paths 
may intersect with one another.

The first robot wants to minimize the number of points collected by the second robot. In contrast, the 
second robot wants to maximize the number of points it collects. If both robots play optimally, 
return the number of points collected by the second robot.

 

Example 1:


Input: grid = [[2,5,4],[1,5,1]]
Output: 4
Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
The cells visited by the first robot are set to 0.
The second robot will collect 0 + 0 + 4 + 0 = 4 points.
Example 2:


Input: grid = [[3,3,1],[8,5,2]]
Output: 4
Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
The cells visited by the first robot are set to 0.
The second robot will collect 0 + 3 + 1 + 0 = 4 points.
Example 3:


Input: grid = [[1,3,1,15],[1,3,3,1]]
Output: 7
Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
The cells visited by the first robot are set to 0.
The second robot will collect 0 + 1 + 3 + 3 + 0 = 7 points.
 

Constraints:

grid.length == 2
n == grid[r].length
1 <= n <= 5 * 10^4
1 <= grid[r][c] <= 10^5


'''

from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        preSum = [[0]*(n+1) for _ in range(2)]
        for i in range(2):
            for j in range(1,n+1):
                preSum[i][j] = preSum[i][j-1]+grid[i][j-1]
        r2 = (10**5+1)*n
        for j in range(n):
            tmp = max(preSum[0][n]-preSum[0][j+1], preSum[1][j])
            if r2 > tmp:                
                r2 = tmp
        return r2


    def gridGame2(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        upper = sum(grid[0])
        r2 = (10**5+1)*n
        r1Sum, r2Sum = 0, 0 
        for j in range(n):
            r1Sum += grid[0][j]
            tmp = max(upper - r1Sum, r2Sum)
            r2Sum += grid[1][j]
            if r2 > tmp:                
                r2 = tmp
        return r2

            



        
if __name__ == '__main__':
    #'''
    grid = [[2,5,4],[1,5,1]]
    print(Solution().gridGame(grid))
    grid = [[3,3,1],[8,5,2]]
    print(Solution().gridGame(grid))
    grid = [[1,3,1,15],[1,3,3,1]]
    print(Solution().gridGame(grid))
    #'''
    grid = [[20,3,20,17,2,12,15,17,4,15],
            [20,10,13,14,15,5,2,3,14,3]]
    print(Solution().gridGame(grid))
    print(Solution().gridGame2(grid))