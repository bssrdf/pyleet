'''
-Medium-

Given a 2D grid, each cell is either an house 1 or empty 0 (It is represented by the numbers 0, 1 and 2.), 
find the place to build a post office, the distance that post office to all the house sum is smallest. Returns the sum of the minimum distances from all houses to the post office, Return -1 if it is not possible.

You can pass through house and empty.
You only build post office on an empty.
The distance between house and the post office is Manhattan distance
样例
Example 1:

Input：[[0,1,0,0],[1,0,1,1],[0,1,0,0]]
Output： 6
Explanation：
Placing a post office at (1,1), the distance that post office to all the house sum is smallest.
Example 2:

Input：[[0,1,0],[1,0,1],[0,1,0]]
Output： 4
Explanation：
Placing a post office at (1,1), the distance that post office to all the house sum is smallest.


'''

import sys
class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    def shortestDistance(self, grid):
        # write your code here
        
        INT_MAX = sys.maxsize-1
        m,n = len(grid),len(grid[0])
        empty = 0
        hor, ver = [0]*n, [0]*m
        ans = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    hor[j] += 1
                    ver[i] += 1
                else:
                    empty += 1
        if empty == 0: return -1
        disH = [INT_MAX/2]*n
        disV = [INT_MAX/2]*m
        for i in range(n):
            if (hor[i] < m):
                disH[i] = 0
                for j  in range(n):
                    disH[i] += hor[j] * abs(i-j)
        for i in range(m):
            if (ver[i] < n):
                disV[i] = 0
                for j in range(m):
                    disV[i] += ver[j] * abs(i-j)
        

        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    ans = min(ans, disV[i]+disH[j])

        return ans

if __name__ == "__main__":
    grid = [[0,1,0,0],[1,0,1,1],[0,1,0,0]]
    print(Solution().shortestDistance(grid))
