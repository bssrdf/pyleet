'''
-Hard-
*BFS*

You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You 
can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right 
corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to 
find such walk return -1.

 

Example 1:

Input: 
grid = 
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 
k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10. 
The shortest path with one obstacle elimination at position (3,2) is 6. 
Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
Example 2:

Input: 
grid = 
[[0,1,1],
 [1,1,1],
 [1,0,0]], 
k = 1
Output: -1
Explanation: 
We need to eliminate at least two obstacles to find such a walk.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 40
1 <= k <= m * n
grid[i][j] == 0 or 1
grid[0][0] == grid[m - 1][n - 1] == 0

'''

from collections import deque
import heapq

class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        queue = deque([((0,0), k, 0)])
        visited = {(0,0,k)}
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]        
        while queue:
            (i,j), obs, steps = queue.popleft()
            if (i,j) == (m-1,n-1): return steps
            for di, dj in dirs:
                x, y = i+di, j+dj
                if x < 0 or x >= m or y < 0 or y >= n: continue
                if grid[x][y] == 0 and (x,y,obs) not in visited: 
                    visited.add((x,y,obs))
                    queue.append(((x,y), obs, steps+1))
                elif obs > 0 and (x,y,obs-1) not in visited: 
                    visited.add((x,y,obs-1))
                    queue.append(((x,y), obs-1, steps+1))
        return -1

    def shortestPath2(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        queue = deque([((0,0), k, 0)])
        visited = [[[False]*(k+1) for _ in range(n) ] for _ in range(m)]
        visited[0][0][k] = True
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]        
        while queue:
            (i,j), obs, steps = queue.popleft()
            # print(i, j, obs, steps)
            if (i,j) == (m-1,n-1): return steps
            for di, dj in dirs:
                x, y = i+di, j+dj
                if x < 0 or x >= m or y < 0 or y >= n: continue
                if grid[x][y] == 0 and not visited[x][y][obs]: 
                    visited[x][y][obs] = True
                    queue.append(((x,y), obs, steps+1))
                elif obs > 0 and not visited[x][y][obs-1]: 
                    visited[x][y][obs-1] = True
                    queue.append(((x,y), obs-1, steps+1))
        return -1      
    


if __name__ == "__main__":
    grid = [[0,0,0],
            [1,1,0],
            [0,0,0],
            [0,1,1],
            [0,0,0]]
    #print(Solution().shortestPath(grid, 1))
    grid = [[0,1,1],
            [1,1,1],
            [1,0,0]] 
    #print(Solution().shortestPath(grid, 1))
    grid = [[0,0],
            [1,0],
            [1,0],
            [1,0],
            [1,0],
            [1,0],
            [0,0],
            [0,1],
            [0,1],
            [0,1],
            [0,0],
            [1,0],
            [1,0],
            [0,0]]
    print(Solution().shortestPath(grid, 4))
    print(Solution().shortestPath2(grid, 4))
