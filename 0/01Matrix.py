'''
-Medium-

*BFS*
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 10^4
1 <= m * n <= 10^4
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.

'''

from collections import deque

class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        Q = deque()
        res = [[0 for _ in range(n)] for _ in range(m)]
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    Q.append((i, j, 0))
                    visited[i][j] = True
        while Q:
            i,j,d = Q.popleft()
            res[i][j] = d 
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                x, y = i+dx, j+dy
                if x < 0 or x > m-1 or y < 0 or y > n-1 or visited[x][y]:
                    continue
                visited[x][y] = True
                Q.append((x,y,d+1))
        return res



if __name__ == "__main__":
    mat = [[0,0,0],[0,1,0],[0,0,0]]
    dist = Solution().updateMatrix(mat)
    for d in dist:
        print(d)