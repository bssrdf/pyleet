'''

-Hard-
*BFS*

You are given a 0-indexed 2D integer array grid of size m x n which represents a field. Each cell has one of three values:

0 represents grass,
1 represents fire,
2 represents a wall that you and fire cannot pass through.
You are situated in the top-left cell, (0, 0), and you want to travel to the safehouse at the bottom-right cell, (m - 1, n - 1). Every minute, you may move to an adjacent grass cell. After your move, every fire cell will spread to all adjacent cells that are not walls.

Return the maximum number of minutes that you can stay in your initial position before moving while still safely reaching the safehouse. If this is impossible, return -1. If you can always reach the safehouse regardless of the minutes stayed, return 109.

Note that even if the fire spreads to the safehouse immediately after you have reached it, it will be counted as safely reaching the safehouse.

A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).

 

Example 1:


Input: grid = [[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]]
Output: 3
Explanation: The figure above shows the scenario where you stay in the initial position for 3 minutes.
You will still be able to safely reach the safehouse.
Staying for more than 3 minutes will not allow you to safely reach the safehouse.
Example 2:


Input: grid = [[0,0,0,0],[0,1,2,0],[0,2,0,0]]
Output: -1
Explanation: The figure above shows the scenario where you immediately move towards the safehouse.
Fire will spread to any cell you move towards and it is impossible to safely reach the safehouse.
Thus, -1 is returned.
Example 3:


Input: grid = [[0,0,0],[2,2,0],[1,2,0]]
Output: 1000000000
Explanation: The figure above shows the initial grid.
Notice that the fire is contained by walls and you will always be able to safely reach the safehouse.
Thus, 109 is returned.
 

Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 300
4 <= m * n <= 2 * 104
grid[i][j] is either 0, 1, or 2.
grid[0][0] == grid[m - 1][n - 1] == 0

'''


from typing import List
from collections import deque

class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(-1,0), (0,-1), (1,0), (0,1)]
        MAX = float('inf')        
        def bfs(typ):
            dist = [[MAX]*n for _ in range(m)]            
            if typ == 0:                
                que = deque([(0,0)]) 
                dist[0][0] = 0
            else:
                que = deque()
                for i in range(m):
                    for j in range(n):
                        if grid[i][j] == 1:
                            que.append((i,j))
                            dist[i][j] = 0
            steps = 0
            while que:
                newque = deque()
                while que:
                    x, y = que.popleft()                    
                    for dx, dy in dirs:
                        i, j = x+dx, y+dy
                        if i < 0 or i >= m or j < 0 or j >= n: continue
                        if grid[i][j] == 2: continue
                        if dist[i][j] != MAX: continue
                        dist[i][j] = steps + 1
                        if i != m-1 or j != n-1:
                            newque.append((i,j))
                que = newque 
                steps += 1
            return dist
        def checkOk(fire, D):
            visited = [[False]*n for _ in range(m)]                        
            steps = D
            que = deque([(0,0)])
            while que:
                newque = deque()
                while que:
                    x, y = que.popleft()                    
                    for dx, dy in dirs:
                        i, j = x+dx, y+dy
                        if i < 0 or i >= m or j < 0 or j >= n: continue
                        if grid[i][j] == 2: continue
                        if visited[i][j]: continue
                        if (i != m-1 or j != n-1) and steps+1 >= fire[i][j]: continue
                        newque.append((i,j))
                        visited[i][j] = True
                        if i == m-1 and j == n-1 and steps+1 <= fire[i][j]:
                            return True
                que = newque 
                steps += 1
            return False
        person = bfs(0)
        fire = bfs(1)
        # for r in fire:
        #     print(r)
        if person[m-1][n-1] == MAX: return -1
        if person[m-1][n-1] > fire[m-1][n-1]: return -1
        if fire[m-1][n-1] == MAX: return 10**9
        D = fire[m-1][n-1] - person[m-1][n-1]
        # print(D)
        if checkOk(fire, D):
            return D
        return D-1


    
if __name__ == "__main__":
    grid = [[0,2,0,0,0,0,0],
            [0,0,0,2,2,1,0],
            [0,2,0,0,1,2,0],
            [0,0,2,2,2,0,2],
            [0,0,0,0,0,0,0]]
    print(Solution().maximumMinutes(grid))
        