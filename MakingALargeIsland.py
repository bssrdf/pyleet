'''
In a 2D grid of 0s and 1s, we change at most one 0 to a 1.

After, what is the size of the largest island? (An island is a 4-directionally 
connected group of 1s).

Example 1:

Input: [[1, 0], [0, 1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: [[1, 1], [1, 0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: [[1, 1], [1, 1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
 

Notes:

1 <= grid.length = grid[0].length <= 50.
0 <= grid[i][j] <= 1.

'''


class Solution(object):

    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])                
        sizes = [0, 0]
        def get(i,j):
            if i > m-1 or i < 0 or j > n-1 or j < 0:
                return 0
            else:
                return grid[i][j]
        def helper(i,j,c):
            if i > m-1 or i < 0 or j > n-1 or j < 0 or grid[i][j] != 1:
                return 0
            grid[i][j] = c
            return 1+helper(i+1,j,c)+helper(i-1,j,c)+helper(i,j+1,c)+helper(i,j-1,c)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    sizes.append(helper(i,j,len(sizes)))
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    s = set([get(i+1,j), get(i-1,j), get(i,j+1), get(i,j-1)])
                    res = max(res, 1+sum([sizes[t] for t in s]))
        return m*n if res == 0 else res
    
    def largestIslandUF(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])    
        roots = [i for i in range(m*n)]
        ranks = [1]*(m*n)
        def find(i):
            while roots[i] != i:
                roots[i] = roots[roots[i]]
                i = roots[i]
            return i 
        def union(i,j):
            x, y = find(i), find(j)
            if x != y:
                if ranks[x] < ranks[y]:
                    roots[x] = y
                    ranks[y] += ranks[x]
                else:
                    roots[y] = x
                    ranks[x] += ranks[y]
        def isValid(i,j):
            if i >= 0 and i < m and j >= 0 and j < n: return True
            return False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    idx = i*n+j
                    for dx,dy in [(-1,0), (1,0), (0,1), (0,-1)]:
                        x,y = i+dx, j+dy
                        if isValid(x,y) and grid[x][y] == 1:
                            nidx = x*n+y 
                            union(idx, nidx)
        res = 1
        for i in ranks:
            res = max(res, i)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    prev = set()
                    combineSize = 1
                    for dx,dy in [(-1,0), (1,0), (0,1), (0,-1)]:
                        x,y = i+dx, j+dy
                        if isValid(x,y) and grid[x][y] == 1:
                            root = find(x*n+y)
                            if not prev or root not in prev:
                                combineSize += ranks[root]
                                prev.add(root) 
                    res = max(res, combineSize)
        return res
                    
        

            

                    



    def largestIslandTLE(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        hasZero = False
        res = 0
        def helper(i,j):
            if i > m-1 or i < 0 or j > n-1 or j < 0 or visited[i][j] or grid[i][j] == 0:
                return 0
            visited[i][j] = True
            return 1+helper(i+1,j)+helper(i-1,j)+helper(i,j+1)+helper(i,j-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    continue
                grid[i][j] = 1
                visited = [[False for _ in range(n)] for _ in range(m)]   
                res = max(res, helper(i,j))
                if res == m*n: return res
                grid[i][j] = 0
                hasZero = True
        return res if hasZero else m*n

        
if __name__ == "__main__":
    print(Solution().largestIsland([[1, 0], [0, 1]]))
    print(Solution().largestIslandUF([[1, 0], [0, 1]]))
    print(Solution().largestIsland([[1, 1], [1, 1]]))
    print(Solution().largestIslandUF([[1, 1], [1, 1]]))