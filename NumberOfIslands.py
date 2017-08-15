'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands
 horizontally or vertically. You may assume all four edges of the grid are all
 surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
'''
from collections import deque

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        n,m = len(grid), len(grid[0])
        processed = [[False for _ in range(m)] for _ in range(n)]
        dirs = [(-1,0), (0,-1), (1,0), (0,1)]
        nums = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (not processed[i][j]):
                    nums += 1
                    q = deque()
                    q.append((i,j))
                    processed[i][j] = True
                    while q:
                        (x,y) = q.popleft()
                        for r,c in dirs:
                            x1 = x+r
                            y1 = y+c
                            if 0 <= x1 < n and 0 <= y1 < m and grid[x1][y1] == '1' and (not processed[x1][y1]):
                                q.append((x1,y1))
                                processed[x1][y1] = True
        return nums
        
    def numIslandsUF(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        n,m = len(grid), len(grid[0])
        roots = [-1]*(m*n)
        cnt = 0
        dirs = [(-1,0), (0,-1), (1,0), (0,1)]
        for i in range(n):
            for j in range(m):
                roots[i*n+j] = i*n+j
                if grid[i][j] == '1':
                    cnt += 1
        for i in range(n):
            for j in range(m):                
                if grid[i][j] == '1':
                    idx = i*n+j
                    for r,c in dirs:
                        i1,j1=i+r,j+c
                        if i1<0 or i1>=n or j1<0 or j1>=m:
                            continue
                        if grid[i1][j1] == '1':
                            idx1 = n*i1+j1
                            x,y =self.find(roots, idx),self.find(roots, idx1) 
                            if x != y:
                                roots[x] = y
                                cnt -= 1
        return cnt
        
    def find(self, roots, i):
        # this while loop is called "qiuck union";
        # it "recursively" decends to the root node represented by the
        # node whose roots value is untouched 'i'
        while roots[i] != i:
            # path compression; set every other node in path point to its grandparent
            roots[i] = roots[roots[i]] 
            i = roots[i]
        return i

if __name__ == "__main__":
    assert Solution().numIslands([['1', '1', '0', '0', '0'],
                                  ['1', '1', '0', '0', '0'],
                                  ['0', '0', '1', '0', '0'],
                                  ['0', '0', '0', '1', '1']]) == 3
    assert Solution().numIslandsUF([['1', '1', '0', '0', '0'],
                                    ['1', '1', '0', '0', '0'],
                                    ['0', '0', '1', '0', '0'],
                                    ['0', '0', '0', '1', '1']]) == 3