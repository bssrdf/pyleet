'''

-Medium-

You are given a 0-indexed 2D integer matrix grid of size 3 * 3, representing the number of stones in each cell. The grid contains exactly 9 stones, and there can be multiple stones in a single cell.

In one move, you can move a single stone from its current cell to any other cell if the two cells share a side.

Return the minimum number of moves required to place one stone in each cell.

 

Example 1:


Input: grid = [[1,1,0],[1,1,1],[1,2,1]]
Output: 3
Explanation: One possible sequence of moves to place one stone in each cell is: 
1- Move one stone from cell (2,1) to cell (2,2).
2- Move one stone from cell (2,2) to cell (1,2).
3- Move one stone from cell (1,2) to cell (0,2).
In total, it takes 3 moves to place one stone in each cell of the grid.
It can be shown that 3 is the minimum number of moves required to place one stone in each cell.
Example 2:


Input: grid = [[1,3,0],[1,0,0],[1,0,3]]
Output: 4
Explanation: One possible sequence of moves to place one stone in each cell is:
1- Move one stone from cell (0,1) to cell (0,2).
2- Move one stone from cell (0,1) to cell (1,1).
3- Move one stone from cell (2,2) to cell (1,2).
4- Move one stone from cell (2,2) to cell (2,1).
In total, it takes 4 moves to place one stone in each cell of the grid.
It can be shown that 4 is the minimum number of moves required to place one stone in each cell.
 

Constraints:

grid.length == grid[i].length == 3
0 <= grid[i][j] <= 9
Sum of grid is equal to 9.


'''
from typing import List
from collections import deque

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        ans = float('inf')
        def solve(i, a, b, vis, c, s):
            nonlocal ans
            if c == len(b):
                ans = min(ans, s)
                return
            for j in range(len(b)):
                if vis[j] == 1:
                    continue
                vis[j] = 1
                x = abs(a[i][0] - b[j][0]) + abs(a[i][1] - b[j][1])
                solve(i + 1, a, b, vis, c + 1, s + x)
                vis[j] = 0
        a = []
        b = []
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    b.append([i, j])
                else:
                    x = grid[i][j] - 1
                    t = [i, j]
                    while x > 0:
                        a.append(t.copy())
                        x -= 1
        x = len(b)
        vis = [0] * x
        
        solve(0, a, b, vis, 0, 0)
        return ans

    def minimumMoves2(self, grid: List[List[int]]) -> int:
        start = tuple((grid[i][j] for i in range(3) for j in range(3)))
        target = (1, 1, 1, 1, 1, 1, 1, 1, 1)
        que = deque([start])
        vis = set(start)
        moves = 0
        def getAdjacent(index):
            adjacent = []
            if index % 3 != 0: adjacent.append(index - 1)
            if index % 3 != 2: adjacent.append(index + 1)
            if index // 3 != 0: adjacent.append(index - 3)
            if index // 3 != 2: adjacent.append(index + 3)
            return adjacent
        
        while que:
            for i in range(len(que)):
                cur = que.popleft()
                if cur == target:
                    return moves
                for j in range(9):
                    if cur[j] > 1:
                        for nxt in getAdjacent(j):
                            nstate = list(cur)
                            nstate[j] -= 1
                            nstate[nxt] += 1
                            nstate = tuple(nstate)
                            if nstate not in vis:
                                vis.add(nstate)
                                que.append(nstate)
            moves += 1
        return -1                         










        

if __name__ == "__main__":
    print(Solution().minimumMoves(grid = [[1,1,0],[1,1,1],[1,2,1]]))
    # print(Solution().minimumMoves(grid = [[1,1,0],[1,1,1],[1,2,1]]))
        