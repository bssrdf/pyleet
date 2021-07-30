'''
-Medium-

*BFS*
*Bidirectional BFS*

You are starving and you want to eat food as quickly as possible. You want to find the 
shortest path to arrive at a food cell.

You are given an m x n character matrix, grid, of these different types of cells:

'*' is your location. There is exactly one '*' cell.
'#' is a food cell. There may be multiple food cells.
'O' is free space, and you can travel through these cells.
'X' is an obstacle, and you cannot travel through these cells.
Return the length of the shortest path for you to reach any food cell. If there is no 
path for you to reach food, return -1.

 

Example 1:


Input: grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
Output: 3
Explanation: It takes 3 steps to reach the food.
Example 2:


Input: grid = [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]
Output: -1
Explanation: It is not possible to reach the food.
Example 3:


Input: grid = [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]
Output: 6
Explanation: There can be multiple food cells. It only takes 6 steps to reach the bottom food.
Example 4:

Input: grid = [["O","*"],["#","O"]]
Output: 2
Example 5:

Input: grid = [["X","*"],["#","X"]]
Output: -1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
grid[row][col] is '*', 'X', 'O', or '#'.
The grid contains exactly one '*'.

'''


from collections import deque

class Solution(object):
    def shortestPath(self, grid):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        Q = deque()
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    Q.append((i, j, 0))
                    visited[i][j] = True
        while Q:
            i,j,d = Q.popleft()
            if grid[i][j] == '#':
                return d
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                x, y = i+dx, j+dy
                if x < 0 or x > m-1 or y < 0 or y > n-1 or visited[x][y] or grid[x][y] == 'X':
                    continue
                visited[x][y] = True
                Q.append((x,y,d+1))
        return -1
    
    def shortestPathBidirBFS(self, grid):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        user = deque()
        food = deque()
        vis_user = set()
        vis_food = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    user.append((i, j))
                    vis_user.add((i,j))
                if grid[i][j] == '#':
                    food.append((i, j))
                    vis_food.add((i,j))
        cur_vis = vis_user
        oth_vis = vis_food
        steps = 0
        while user:                        
            next_lev = deque()
            for _ in range(len(user)):
                i,j = user.popleft()
                #if grid[i][j] == '#':
                #    return steps
                if (i,j) in oth_vis:
                    return steps                     
                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    x, y = i+dx, j+dy
                    if x < 0 or x > m-1 or y < 0 or y > n-1 or (x,y) in cur_vis or grid[x][y] == 'X':
                        continue
                    cur_vis.add((x,y))
                    next_lev.append((x,y))
            if len(next_lev) < len(food):
                user = next_lev
            else:
                user, food = food, next_lev
                cur_vis, oth_vis = oth_vis, cur_vis            
            steps += 1
            #print(steps, next_lev, user, cur_vis)
            #print(steps, food, oth_vis)
        return -1

if __name__ == "__main__":
    grid = [["X","X","X","X","X","X","X","X"],
            ["X","*","O","X","O","#","O","X"],
            ["X","O","O","X","O","O","X","X"],
            ["X","O","O","O","O","#","O","X"],
            ["X","X","X","X","X","X","X","X"]]
    print(Solution().shortestPath(grid))
    print(Solution().shortestPathBidirBFS(grid))
    grid = [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]
    print(Solution().shortestPath(grid))
    print(Solution().shortestPathBidirBFS(grid))
    grid = [["O","*"],["#","O"]]
    print(Solution().shortestPath(grid))
    print(Solution().shortestPathBidirBFS(grid))
    grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
    print(Solution().shortestPath(grid))
    print(Solution().shortestPathBidirBFS(grid))
    grid = [["X","*"],["#","X"]]
    print(Solution().shortestPath(grid))
    print(Solution().shortestPathBidirBFS(grid))