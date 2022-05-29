'''
-Hard-
*BFS*
*Dijkstra's Algorithm*
You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:

0 represents an empty cell,
1 represents an obstacle that may be removed.
You can move up, down, left, or right from and to an empty cell.

Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).

 

Example 1:


Input: grid = [[0,1,1],[1,1,0],[1,1,0]]
Output: 2
Explanation: We can remove the obstacles at (0, 1) and (0, 2) to create a path from (0, 0) to (2, 2).
It can be shown that we need to remove at least 2 obstacles, so we return 2.
Note that there may be other ways to remove 2 obstacles to create a path.
Example 2:


Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
Output: 0
Explanation: We can move from (0, 0) to (2, 4) without removing any obstacles, so we return 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 105
2 <= m * n <= 105
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 0


'''

from typing import List
from collections import deque
import heapq
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # 0-1 BFS
        m, n = map(len, (grid, grid[0]))
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = grid[0][0]
        hp = deque([(dist[0][0], 0, 0)])
        while hp:
            d, r, c = hp.popleft()
            if (r, c) == (m - 1, n - 1):
                return d
            for i, j in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if m > i >= 0 <= j < n and grid[i][j] + d < dist[i][j]:
                    dist[i][j] = grid[i][j] + d
                    if grid[i][j] == 1:
                        hp.append((dist[i][j], i, j))
                    else:
                        hp.appendleft((dist[i][j], i, j))
        return dist[-1][-1]
    
    def minimumObstacles2(self, grid: List[List[int]]) -> int:
        # Dijkstra
        m, n = map(len, (grid, grid[0]))
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = grid[0][0]
        hp = [(dist[0][0], 0, 0)]
        while hp:
            o, r, c = heapq.heappop(hp)
            if (r, c) == (m - 1, n - 1):
                return o
            for i, j in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if m > i >= 0 <= j < n and grid[i][j] + o < dist[i][j]:
                    dist[i][j] = grid[i][j] + o
                    heapq.heappush(hp, (dist[i][j], i, j))