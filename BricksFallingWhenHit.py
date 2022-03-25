'''
-Hard-

*Union Find*

You are given an m x n binary grid, where each 1 represents a brick and 0 
represents an empty space. A brick is stable if:

It is directly connected to the top of the grid, or
At least one other brick in its four adjacent cells is stable.
You are also given an array hits, which is a sequence of erasures we want to 
apply. Each time we want to erase the brick at the location hits[i] = (rowi, coli). 
The brick on that location (if it exists) will disappear. Some other bricks 
may no longer be stable because of that erasure and will fall. Once a brick 
falls, it is immediately erased from the grid (i.e., it does not land on other 
stable bricks).

Return an array result, where each result[i] is the number of bricks that will 
fall after the ith erasure is applied.

Note that an erasure may refer to a location with no brick, and if it does, 
no bricks drop.

 

Example 1:

Input: grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
Output: [2]
Explanation: Starting with the grid:
[[1,0,0,0],
 [1,1,1,0]]
We erase the underlined brick at (1,0), resulting in the grid:
[[1,0,0,0],
 [0,1,1,0]]
The two underlined bricks are no longer stable as they are no longer connected to the top nor adjacent to another stable brick, so they will fall. The resulting grid is:
[[1,0,0,0],
 [0,0,0,0]]
Hence the result is [2].
Example 2:

Input: grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]
Output: [0,0]
Explanation: Starting with the grid:
[[1,0,0,0],
 [1,1,0,0]]
We erase the underlined brick at (1,1), resulting in the grid:
[[1,0,0,0],
 [1,0,0,0]]
All remaining bricks are still stable, so no bricks fall. The grid remains the same:
[[1,0,0,0],
 [1,0,0,0]]
Next, we erase the underlined brick at (1,0), resulting in the grid:
[[1,0,0,0],
 [0,0,0,0]]
Once again, all remaining bricks are still stable, so no bricks fall.
Hence the result is [0,0].
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
grid[i][j] is 0 or 1.
1 <= hits.length <= 4 * 104
hits[i].length == 2
0 <= xi <= m - 1
0 <= yi <= n - 1
All (xi, yi) are unique.


'''

from typing import List
from collections import defaultdict
import copy
class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        gcopy = copy.deepcopy(grid)
        m, n = len(grid), len(grid[0])
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        #marks = []
        for x,y in hits:
            if grid[x][y] == 1: 
               grid[x][y] = 0
         #      marks.append((x,y))
        #hits = marks
        parents = defaultdict(tuple)
        ranks  = defaultdict(int)
        def find(x):
            while x != parents[x]:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x
        def union(x, y):
            fx, fy = find(x), find(y)
            if fx != fy:
                if fx[0] < fy[0]:
                    parents[fy] = fx
                    ranks[fx] += ranks[fy] 
                else:
                    parents[fx] = fy
                    ranks[fy] += ranks[fx] 

        # print('modified grid')
        # for x in grid:
        #     print(x)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    parents[(i,j)] = (i,j)
                    ranks[(i,j)] = 1
        #visited = [[False]*n for _ in range(m)]            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    #visited[i][j] = True
                    for dx,dy in dirs:
                        x, y = i+dx, j+dy
                        if 0<=x<m and 0<=y<n and grid[x][y] == 1:
                            # visited[x][y] = True
                            union((i,j),(x,y))
        # print(parents)
        ans = []
        for i,j in hits[::-1]:
            if gcopy[i][j] == 1: 
                unstable0, seen = 0, set()
                for dx, dy in dirs:
                    x, y = i+dx, j+dy
                    if 0<=x<m and 0<=y<n and grid[x][y] == 1:
                        head = find((x,y)) 
                        # print((i,j), (x,y), head, ranks[head])
                        if head[0] != 0 and head not in seen:
                            seen.add(head)
                            unstable0 += ranks[head]
                parents[(i,j)] = (i,j)
                ranks[(i,j)] = 1
                grid[i][j] = 1
                for dx, dy in dirs:
                    x, y = i+dx, j+dy
                    if 0<=x<m and 0<=y<n and grid[x][y] == 1:
                        union((i,j),(x,y))
                unstable1, seen = 0, set()
                for dx, dy in dirs:
                    x, y = i+dx, j+dy
                    if 0<=x<m and 0<=y<n and grid[x][y] == 1:
                        head = find((x,y)) 
                        if head[0] != 0 and head not in seen:
                            seen.add(head)
                            unstable1 += ranks[head]
                ans.append(max(0,unstable0-unstable1))
                # print((i,j), unstable0, unstable1)
            else:
                ans.append(0) 
        return ans[::-1]     
    
    def hitBricks2(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        #gcopy = copy.deepcopy(grid)
        m, n = len(grid), len(grid[0])
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        for i,(x,y) in enumerate(hits):
            if grid[x][y] == 1: 
               hits[i].append(1) 
               grid[x][y] = 0
            else:
               hits[i].append(0)
        parents = [x*n+y for x in range(m) for y in range(n)]
        ranks  =  [1]*(n*m)
        def row(idx):
            return idx//n
        def find(x):
            while x != parents[x]:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x
        def union(x, y):
            fx, fy = find(x), find(y)
            if fx != fy:
                if row(fx) < row(fy):
                    parents[fy] = fx
                    ranks[fx] += ranks[fy] 
                else:
                    parents[fx] = fy
                    ranks[fy] += ranks[fx] 
        def union_neighbors(i,j):
            idx1 = i*n+j
            for dx,dy in dirs:
                x, y = i+dx, j+dy
                if 0<=x<m and 0<=y<n and grid[x][y] == 1:
                    idx2 = x*n+y
                    union(idx1, idx2)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    union_neighbors(i, j)
        ans = []
        for i,j,v in hits[::-1]:
            def unstable():
                unstable0, seen = 0, set()
                for dx, dy in dirs:
                    x, y = i+dx, j+dy
                    if 0<=x<m and 0<=y<n and grid[x][y] == 1:
                        idx = x*n+y
                        head = find(idx) 
                        if row(head) != 0 and head not in seen:
                            seen.add(head)
                            unstable0 += ranks[head]
                return unstable0
            if v == 1: 
                unstable0 = unstable()                
                grid[i][j] = 1
                union_neighbors(i,j)
                unstable1 = unstable()                
                ans.append(max(0,unstable0-unstable1))
            else:
                ans.append(0) 
        return ans[::-1]     
            
                     



if __name__ == "__main__":
    print(Solution().hitBricks(grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]))
    print(Solution().hitBricks(grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]))
    grid = [[0,1,1,1,0],
            [0,1,1,1,0],
            [0,0,1,1,1],
            [0,0,1,1,1],
            [0,0,1,1,1]]
    hits = [[2,2],[2,3]] 
    print(Solution().hitBricks(grid, hits))
    grid = [[1],[1],[1],[1],[1]]
    hits = [[3,0],[4,0],[1,0],[2,0],[0,0]]
    print(Solution().hitBricks(grid, hits))
    grid = [[1,0,1],[1,1,1]]
    hits = [[0,0],[0,2],[1,1]]
    print(Solution().hitBricks(grid, hits))

    print(Solution().hitBricks2(grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]))
    print(Solution().hitBricks2(grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]))
    grid = [[0,1,1,1,0],
            [0,1,1,1,0],
            [0,0,1,1,1],
            [0,0,1,1,1],
            [0,0,1,1,1]]
    hits = [[2,2],[2,3]] 
    print(Solution().hitBricks2(grid, hits))
    grid = [[1],[1],[1],[1],[1]]
    hits = [[3,0],[4,0],[1,0],[2,0],[0,0]]
    print(Solution().hitBricks2(grid, hits))
    grid = [[1,0,1],[1,1,1]]
    hits = [[0,0],[0,2],[1,1]]
    print(Solution().hitBricks2(grid, hits))