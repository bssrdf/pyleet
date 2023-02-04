'''
-Hard-


You want to build a house on an empty land which reaches all buildings in the shortest 
amount of distance. 
You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, 
where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7 

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total 
             travel distance of 3+3+1=7 is minimal. So return 7.
Note:
There will be at least one building. If it is not possible to build such house according 
to the above rules, return -1.

'''
import sys
from collections import deque

class Solution(object):

    def shortestDistance(self, grid):
        m, n = len(grid), len(grid[0])
       # res = sys.maxsize-1
        val = 0
        sumDist = [[0 for _ in range(n)] for _ in range(m)]
        dirs = ((-1, 0),(1, 0), (0, -1), (0, 1))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = sys.maxsize-1
                    q = deque()
                    dist = [[x for x in row] for row in grid]
                    q.append((i,j))
                    while q:
                        (a,b) = q.popleft()
                        for d in dirs:
                            ik, jk = a+d[0], b+d[1]
                            if ik >= 0  and ik < m and jk >=0 and jk < n and grid[ik][jk] == val:
                                grid[ik][jk] -= 1
                                dist[ik][jk] = dist[a][b] + 1
                                sumDist[ik][jk] += dist[ik][jk]-1
                                q.append((ik,jk))
                                res = min(res, sumDist[ik][jk])
                    val -= 1
        return -1 if res == sys.maxsize-1 else res


s = Solution()
grid = [[1,0,2,0,1],
        [0,0,0,0,0],
        [0,0,1,0,0]]
print(s.shortestDistance(grid))








