''''
-Medium-

Given an N x N grid containing only values 0 and 1, where 0 represents water 
and 1 represents land, find a water cell such that its distance to the nearest 
land cell is maximized and return the distance.

The distance used in this problem is the Manhattan distance: the distance between 
two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

If no land or water exists in the grid, return -1.

 

Example 1:



Input: [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: 
The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2:



Input: [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: 
The cell (2, 2) is as far as possible from all the land with distance 4.
 

Note:

1 <= grid.length == grid[0].length <= 100
grid[i][j] is 0 or 1

'''
from collections import deque

class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        wc, lc = 0, 0 
        q = deque()
        visited = set()
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        res = -1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    lc += 1
                    q.append(((i,j),0))
                    visited.add((i,j))
                if grid[i][j] == 0:
                    wc += 1
        if lc == n*n or wc == n*n: return res
        while q:
            (ic, jc), dist = q.popleft()
            res = max(res, dist)
            for d in dirs:
                i, j = ic+d[0], jc+d[1]
                if 0<=i<n and 0<=j<n and grid[i][j]==0:
                    if (i,j) not in visited:
                        visited.add((i,j))
                        q.append(((i,j),dist+1))
                        
        return res
            
if __name__ == "__main__":
    print(Solution().maxDistance([[1,0,1],[0,0,0],[1,0,1]]))
    print(Solution().maxDistance([[1,0,0],[0,0,0],[0,0,0]]))