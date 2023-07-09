'''
-Medium-

You are given two integers m and n representing the dimensions of a 0-indexed m x n grid.

You are also given a 0-indexed 2D integer matrix coordinates, where coordinates[i] = [x, y] indicates that the cell with coordinates [x, y] is colored black. All cells in the grid that do not appear in coordinates are white.

A block is defined as a 2 x 2 submatrix of the grid. More formally, a block with cell [x, y] as its top-left corner where 0 <= x < m - 1 and 0 <= y < n - 1 contains the coordinates [x, y], [x + 1, y], [x, y + 1], and [x + 1, y + 1].

Return a 0-indexed integer array arr of size 5 such that arr[i] is the number of blocks that contains exactly i black cells.

 

Example 1:

Input: m = 3, n = 3, coordinates = [[0,0]]
Output: [3,1,0,0,0]
Explanation: The grid looks like this:

There is only 1 block with one black cell, and it is the block starting with cell [0,0].
The other 3 blocks start with cells [0,1], [1,0] and [1,1]. They all have zero black cells. 
Thus, we return [3,1,0,0,0]. 
Example 2:

Input: m = 3, n = 3, coordinates = [[0,0],[1,1],[0,2]]
Output: [0,2,2,0,0]
Explanation: The grid looks like this:

There are 2 blocks with two black cells (the ones starting with cell coordinates [0,0] and [0,1]).
The other 2 blocks have starting cell coordinates of [1,0] and [1,1]. They both have 1 black cell.
Therefore, we return [0,2,2,0,0].
 

Constraints:

2 <= m <= 105
2 <= n <= 105
0 <= coordinates.length <= 104
coordinates[i].length == 2
0 <= coordinates[i][0] < m
0 <= coordinates[i][1] < n
It is guaranteed that coordinates contains pairwise distinct coordinates.


'''

from typing import List

class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        ans = [0]*5
        pts = set((i,j) for i,j in coordinates)
        total = (m-1)*(n-1)
        def countBlack(xs, xe, ys, ye, a):
            cnt = 0
            for i in range(xs,xe+1):
                for j in range(ys,ye+1):
                    if (i,j) in pts:
                        cnt += 1
            a[cnt] += 1

        for x,y in coordinates:
            if x == 0:
                if y == 0:
                    countBlack(0, 1, 0, 1, ans)
                elif y == n-1:
                    countBlack(0, 1, n-2, n-1, ans)
                else:    
                    countBlack(0, 1, y-1, y, ans)
                    countBlack(0, 1, y, y+1, ans)
            elif x == m-1:
                if y == 0:
                    countBlack(m-2, m-1, 0, 1, ans)
                elif y == n-1:
                    countBlack(m-2, m-1, n-2, n-1, ans)
                else:    
                    countBlack(m-2, m-1, y-1, y, ans)
                    countBlack(m-2, m-1, y, y+1, ans)
            elif y == 0:
                if x == 0:
                    countBlack(0, 1, 0, 1, ans)
                elif x == m-1:
                    countBlack(m-2, m-1, 0, 1, ans)
                else:    
                    countBlack(x-1, x, 0, 1, ans)
                    countBlack(x, x+1, 0, 1, ans)
            elif y == n-1:
                if x == 0:
                    countBlack(0, 1, n-2, n-1, ans)
                elif x == m-1:
                    countBlack(m-2, m-1, n-2, n-1, ans)
                else:    
                    countBlack(x-1, x, n-2, n-1, ans)
                    countBlack(x, x+1, n-2, n-1, ans)
            else:
                xs = [x-1, x-1, x, x]
                ys = [y-1, y, y-1, y]
                xe = [x, x, x+1, x+1]
                ye = [y, y+1, y, y+1]            
                for k in range(4):                
                    countBlack(xs[k], xe[k], ys[k], ye[k], ans)
        for i in range(1,5):
            ans[i] //= i
        # print(ans)
        return [total - sum(ans[1:])] + ans[1:]

if __name__ == "__main__":
    print(Solution().countBlackBlocks(m = 3, n = 3, coordinates = [[0,0]]))
    print(Solution().countBlackBlocks(m = 3, n = 3, coordinates = [[0,0],[1,1],[0,2]]))