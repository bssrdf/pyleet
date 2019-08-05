'''

You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to 
represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to 
reach a gate, it should be filled with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

'''
import sys
from collections import deque
INF = sys.maxsize-1

class Solution():
        def wallsAndGates(self, rooms):
            if not rooms:
               return
            m, n = len(rooms), len(rooms[0])
            visited = [[False for _ in range(n)] for _ in range(m)]
            q = deque()
            dirs =((-1, 0), (1, 0), (0, 1), (0, -1)) 
            for i in range(m):
                for j in range(n):
                    if rooms[i][j] == 0:
                        q.append((i,j,0))
                        visited[i][j] = True
            while q:
                (i,j,k) = q.popleft()
                for d in dirs:
                    ik,jk=i+d[0],j+d[1]
                    if ik >= 0 and ik < m and jk >= 0 and jk < n and not visited[ik][jk] and rooms[ik][jk] == INF:
                        rooms[ik][jk] = k+1
                        q.append((ik,jk,k+1))
                        visited[ik][jk] = True
            return

        def wallsAndGatesDFS(self, rooms):
            if not rooms:
               return
            m, n = len(rooms), len(rooms[0])            
            
            for i in range(m):
                for j in range(n):
                    if rooms[i][j] == 0:
                        self.dfs(rooms, i, j, 0)
            return
            
        def dfs(self, rooms, i, j, k):
            if i < 0 or i >= len(rooms) or j < 0 or j >= len(rooms[0]) or rooms[i][j] < k:
                return            
            rooms[i][j] = k            
            self.dfs(rooms, i+1, j, k+1)
            self.dfs(rooms, i-1, j, k+1)
            self.dfs(rooms, i, j+1, k+1)
            self.dfs(rooms, i, j-1, k+1)            
            return



rooms = [[INF,  -1,  0,  INF],
         [INF, INF, INF,  -1],
         [INF,  -1, INF,  -1],
         [0,  -1, INF, INF] ]
for r in rooms:
    print(r)
Solution().wallsAndGatesDFS(rooms)
for r in rooms:
    print(r)