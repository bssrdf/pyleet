# -*- coding: utf-8 -*-
"""
-Hard-
*Priority Queue*
*BFS*


Given an m x n matrix of positive integers representing the height of each unit 
cell in a 2D elevation map, compute the volume of water it is able to trap 
after raining.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.


The above image represents the elevation map [[1,4,3,1,3,2],
[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.



After the rain, water is trapped between the blocks. The total volume 
of water trapped is 4.

 
Constraints:

1 <= m, n <= 110
0 <= heightMap[i][j] <= 20000

"""

class Solution(object):
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0
        
        import heapq    
        m, n = len(heightMap), len(heightMap[0])
        heap = []
        visited = [[False]*n for _ in range(m)]

        # Push all the block on the border into heap
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m-1 or j == n-1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        result = 0
        while heap:
            height, i, j = heapq.heappop(heap)    
            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    result += max(0, height-heightMap[x][y])
                    heapq.heappush(heap, (max(heightMap[x][y], height), x, y))
                    visited[x][y] = True
        return result
        
        
if __name__ == "__main__":
  height = [
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
  ]
  print(Solution().trapRainWater(height))