'''
-Hard-
*Memoization*
*DP*
*Minimax*

A game is played by a cat and a mouse named Cat and Mouse.

The environment is represented by a grid of size rows x cols, where each 
element is a wall, floor, player (Cat, Mouse), or food.

Players are represented by the characters 'C'(Cat),'M'(Mouse).
Floors are represented by the character '.' and can be walked on.
Walls are represented by the character '#' and cannot be walked on.
Food is represented by the character 'F' and can be walked on.
There is only one of each character 'C', 'M', and 'F' in grid.
Mouse and Cat play according to the following rules:

Mouse moves first, then they take turns to move.
During each turn, Cat and Mouse can jump in one of the four directions 
(left, right, up, down). They cannot jump over the wall nor outside of 
the grid.
catJump, mouseJump are the maximum lengths Cat and Mouse can jump at a 
time, respectively. Cat and Mouse can jump less than the maximum length.
Staying in the same position is allowed.
Mouse can jump over Cat.
The game can end in 4 ways:

If Cat occupies the same position as Mouse, Cat wins.
If Cat reaches the food first, Cat wins.
If Mouse reaches the food first, Mouse wins.
If Mouse cannot get to the food within 1000 turns, Cat wins.
Given a rows x cols matrix grid and two integers catJump and mouseJump, 
return true if Mouse can win the game if both Cat and Mouse play 
optimally, otherwise return false.

 

Example 1:



Input: grid = ["####F","#C...","M...."], catJump = 1, mouseJump = 2
Output: true
Explanation: Cat cannot catch Mouse on its turn nor can it get the 
food before Mouse.
Example 2:



Input: grid = ["M.C...F"], catJump = 1, mouseJump = 4
Output: true
Example 3:

Input: grid = ["M.C...F"], catJump = 1, mouseJump = 3
Output: false
Example 4:

Input: grid = ["C...#","...#F","....#","M...."], catJump = 2, mouseJump = 5
Output: false
Example 5:

Input: grid = [".M...","..#..","#..#.","C#.#.","...#F"], catJump = 3, 
mouseJump = 1
Output: true
 

Constraints:

rows == grid.length
cols = grid[i].length
1 <= rows, cols <= 8
grid[i][j] consist only of characters 'C', 'M', 'F', '.', and '#'.
There is only one of each character 'C', 'M', and 'F' in grid.
1 <= catJump, mouseJump <= 8

'''

from functools import lru_cache

class Solution(object):
    def canMouseWin(self, grid, catJump, mouseJump):
        """
        :type grid: List[str]
        :type catJump: int
        :type mouseJump: int
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        available = 0
        ci, cj = 0, 0
        mi, mj = 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != '#':
                    available += 1
                if grid[i][j] == 'C':
                    ci, cj = i, j
                if grid[i][j] == 'M':
                    mi, mj = i, j
        @lru_cache(None)            
        def dfs(turns, msi, msj, cti, ctj):
            if turns == 2*available:
                return False
            if turns % 2 == 0:
                for dx, dy in dirs:
                    for jumps in range(mouseJump+1):
                        nx, ny = msi+dx*jumps, msj+dy*jumps
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != '#':
                            if dfs(turns+1, nx, ny, cti, ctj) or \
                                grid[nx][ny] == 'F': return True
                        else:
                            break
                return False
            else:
                for dx, dy in dirs:
                    for jumps in range(catJump+1):
                        nx, ny = cti+dx*jumps, ctj+dy*jumps
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != '#':
                            if not dfs(turns+1, msi, msj, nx, ny) or \
                                (nx==msi and ny == msj) or \
                                grid[nx][ny] == 'F': return False
                        else:
                            break
                return True
        return dfs(0, mi, mj, ci, cj)


if __name__ == "__main__":
    print(Solution().canMouseWin(["####F","#C...","M...."], 1, 2))