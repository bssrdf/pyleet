'''
-Hard-
*BFS*

In an n*n grid, there is a snake that spans 2 cells and starts moving from the top left corner at (0, 0) and (0, 1). The grid has empty cells represented by zeros and blocked cells represented by ones. The snake wants to reach the lower right corner at (n-1, n-2) and (n-1, n-1).

In one move the snake can:

Move one cell to the right if there are no blocked cells there. This move keeps the horizontal/vertical position of the snake as it is.
Move down one cell if there are no blocked cells there. This move keeps the horizontal/vertical position of the snake as it is.
Rotate clockwise if it's in a horizontal position and the two cells under it are both empty. In that case the snake moves from (r, c) and (r, c+1) to (r, c) and (r+1, c).

Rotate counterclockwise if it's in a vertical position and the two cells to its right are both empty. In that case the snake moves from (r, c) and (r+1, c) to (r, c) and (r, c+1).

Return the minimum number of moves to reach the target.

If there is no way to reach the target, return -1.

 

Example 1:



Input: grid = [[0,0,0,0,0,1],
               [1,1,0,0,1,0],
               [0,0,0,0,1,1],
               [0,0,1,0,1,0],
               [0,1,1,0,0,0],
               [0,1,1,0,0,0]]
Output: 11
Explanation:
One possible solution is [right, right, rotate clockwise, right, down, down, down, down, rotate counterclockwise, right, down].
Example 2:

Input: grid = [[0,0,1,1,1,1],
               [0,0,0,0,1,1],
               [1,1,0,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,0]]
Output: 9
 

Constraints:

2 <= n <= 100
0 <= grid[i][j] <= 1
It is guaranteed that the snake starts at empty cells.


'''

from typing import List
from collections import deque

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        que = deque([(0, (0,0), (0,1))])
        visited = {((0,0), (0,1))}
        while que:
            steps, t, h = que.popleft()
            if t == (n-1, n-2) and h == (n-1, n-1):
                return steps
            right = (t[0],h[1]), (h[0], h[1]+1)
            if h[1]+1 < n and h[0] == t[0] and grid[h[0]][h[1]+1] == 0 and right not in visited:
                visited.add(right)
                que.append((steps+1, *right))
            right = (t[0],t[1]+1), (h[0], h[1]+1)
            if h[1]+1 < n and h[0] == t[0]+1 and grid[h[0]][h[1]+1] == 0 and grid[t[0]][t[1]+1] == 0 and right not in visited:
                visited.add(right)
                que.append((steps+1, *right))
            down = (h[0], t[1]), (h[0]+1, h[1])
            if h[0]+1 < n and t[1] == h[1] and grid[h[0]+1][h[1]] == 0 and down not in visited:
                visited.add(down)
                que.append((steps+1, *down))
            down = (t[0]+1, t[1]), (h[0]+1, h[1])
            if h[0]+1 < n and t[0] == h[0] and grid[h[0]+1][h[1]] == 0 and grid[t[0]+1][t[1]] == 0 and down not in visited:
                visited.add(down)
                que.append((steps+1, *down))
            clw = (t[0],t[1]), (t[0]+1, t[1])
            if t[0]+1 < n and t[0] == h[0] and grid[t[0]+1][t[1]] == 0 and grid[h[0]+1][h[1]] == 0 and clw not in visited:
                visited.add(clw)
                que.append((steps+1, *clw))
            ccw = (t[0],t[1]), (t[0], t[1]+1)
            if t[1]+1 < n and t[1] == h[1] and grid[t[0]][t[1]+1] == 0 and grid[h[0]][h[1]+1] == 0 and ccw not in visited:
                visited.add(ccw)
                que.append((steps+1, *ccw))
        return -1

    def minimumMoves2(self, grid: List[List[int]]) -> int:
        n = len(grid)
        que = deque([(0, (0,0), (0,1))])
        visited = {((0,0), (0,1))}
        while que:
            steps, t, h = que.popleft()
            if t == (n-1, n-2) and h == (n-1, n-1):
                return steps
            if h[0] == t[0]: # horizonal
                right = (t[0],h[1]), (h[0], h[1]+1)
                if h[1]+1 < n and grid[h[0]][h[1]+1] == 0 and right not in visited:
                    visited.add(right)
                    que.append((steps+1, *right))
                if h[0]+1 < n and grid[h[0]+1][h[1]] == 0 and grid[t[0]+1][t[1]] == 0:
                    down = (t[0]+1, t[1]), (h[0]+1, h[1])
                    if h[0]+1 < n and down not in visited:
                        visited.add(down)
                        que.append((steps+1, *down))
                    clw = (t[0],t[1]), (t[0]+1, t[1])
                    if t[0]+1 < n and clw not in visited:
                        visited.add(clw)
                        que.append((steps+1, *clw))   
            else: # vertical 
                down = (h[0], t[1]), (h[0]+1, h[1])
                if h[0]+1 < n and grid[h[0]+1][h[1]] == 0 and down not in visited:
                    visited.add(down)
                    que.append((steps+1, *down))
                if h[1]+1 < n and grid[h[0]][h[1]+1] == 0 and grid[t[0]][t[1]+1] == 0:
                    right = (t[0],t[1]+1), (h[0], h[1]+1)
                    if h[1]+1 < n and right not in visited:
                        visited.add(right)
                        que.append((steps+1, *right))
                    ccw = (t[0],t[1]), (t[0], t[1]+1)
                    if t[1]+1 < n and ccw not in visited:
                        visited.add(ccw)
                        que.append((steps+1, *ccw))
        return -1
            
            







if __name__ == "__main__":
    grid =    [[0,0,0,0,0,1],
               [1,1,0,0,1,0],
               [0,0,0,0,1,1],
               [0,0,1,0,1,0],
               [0,1,1,0,0,0],
               [0,1,1,0,0,0]]
    print(Solution().minimumMoves(grid))
    print(Solution().minimumMoves2(grid))
    grid =    [[0,0,1,1,1,1],
               [0,0,0,0,1,1],
               [1,1,0,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,0]]
    print(Solution().minimumMoves(grid))
    print(Solution().minimumMoves2(grid))
        