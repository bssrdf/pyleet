'''
-Medium-

You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls 
(represented as '+'). You are also given the entrance of the maze, where 
entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, 
and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit 
is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no 
such path exists.

 

Example 1:


Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.
Example 2:


Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.
Example 3:


Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
Explanation: There are no exits in this maze.
 

Constraints:

maze.length == m
maze[i].length == n
1 <= m, n <= 100
maze[i][j] is either '.' or '+'.
entrance.length == 2
0 <= entrancerow < m
0 <= entrancecol < n
entrance will always be an empty cell.

'''
from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        m, n = len(maze), len(maze[0])
        A = maze
        qs, qt = deque(), deque()
        vs, vt = set(), set()
        dirs = [ (-1,0), (1,0), (0,-1), (0,1)]
        for i in range(m):
            for j in range(n):
                if A[i][j] == '.' and (i == 0 or i == m-1 or 
                   j == 0 or j == n-1) and [i,j] != entrance:
                    qt.append((i,j))
                    vt.add((i,j))
        qs.append(tuple(entrance))
        vs.add(tuple(entrance))
        sk, tk = 0, 0 
        #print(qs, qt)
        while qs and qt:
            nxt = deque()
            for _ in range(len(qs)):
                si,sj = qs.popleft()
                if (si, sj) in vt:
                    return sk+tk
                for dx,dy in dirs:
                    x, y = si+dx, sj+dy
                    if x >= 0 and x < m and y >= 0 and y < n and (x,y) not in vs and A[x][y]=='.':
                        vs.add((x,y))
                        nxt.append((x,y))                        
            sk += 1
            qs = nxt
            nxt = deque()
            for _ in range(len(qt)):
                si,sj = qt.popleft()
                if (si, sj) in vs:
                    return sk+tk
                for dx,dy in dirs:
                    x, y = si+dx, sj+dy
                    if x >= 0 and x < m and y >= 0 and y < n and (x,y) not in vt and A[x][y]=='.':
                        vt.add((x,y))
                        nxt.append((x,y))                        
            tk += 1
            qt = nxt
        return -1


if __name__ == "__main__":
    maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
    print(Solution().nearestExit(maze, [1,2]))
    print(Solution().nearestExit2(maze, [1,2]))
    maze = [["+","+","+"],[".",".","."],["+","+","+"]]
    print(Solution().nearestExit(maze, [1,0]))
    print(Solution().nearestExit2(maze, [1,0]))


