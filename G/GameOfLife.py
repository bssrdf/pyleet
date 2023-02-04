'''
-Medium-
*Bit Manipulation*

According to Wikipedia's article: "The Game of Life, also known simply as 
Life, is a cellular automaton devised by the British mathematician John 
Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an 
initial state: live (represented by a 1) or dead (represented by a 0). 
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) 
using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by 
under-population.
Any live cell with two or three live neighbors lives on to the next 
generation.
Any live cell with more than three live neighbors dies, as if by 
over-population.
Any dead cell with exactly three live neighbors becomes a live cell, 
as if by reproduction.
The next state is created by applying the above rules simultaneously to 
every cell in the current state, where births and deaths occur simultaneously. 
Given the current state of the m x n grid board, return the next state.

 

Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
 

Follow up:

Could you solve it in-place? Remember that the board needs to be updated 
simultaneously: You cannot update some cells first and then use their 
updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, 
the board is infinite, which would cause problems when the active area 
encroaches upon the border of the array (i.e., live cells reach the border). 
How would you address these problems?


'''
from itertools import product
class Solution(object):
    def gameOfLifeBit(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i, j in product(range(m), range(n)):
            cnt = 0
            for di, dj in product(range(-1, 2), repeat=2):
                if di != 0 or dj != 0:
                    ii, jj = i + di, j + dj
                    if 0 <= ii < m and 0 <= jj < n:
                        cnt += board[ii][jj] & 1  # get old state info from lower bit
            if cnt == 3 or (cnt == 2 and board[i][j] & 1): # Game-of-Life rule
                board[i][j] |= 2 # record updated state at higher bit
        # print(board)
        for i, j in product(range(m), range(n)):
            board[i][j] >>= 1 # finally update the board by shifting 
                              # to 1 bit to right (higher bit overwrites lower bit)

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        """
        位运算（bit manipulation）
        由于细胞只有两种状态0和1，因此可以使用二进制来表示细胞的生存状态
        更新细胞状态时，将细胞的下一个状态用高位进行存储
        全部更新完毕后，将细胞的状态右移一位
        """
        m, n = len(board), len(board[0])
        dx = [-1, -1, -1, 0, 1, 1, 1, 0]
        dy = [-1, 0, 1, 1, 1, 0, -1, -1]
        for i in range(m):
            for j in range(n):
                lives = 0
                for d1, d2 in zip(dx, dy):
                    x, y = i+d1, j+d2
                    # 0 : 上一轮是0，这一轮过后还是0
                    # 1 : 上一轮是1，这一轮过后还是1
                    # 2 : 上一轮是1，这一轮过后变为0
                    # 3 : 上一轮是0，这一轮过后变为1
                    # 对于一个节点来说，如果它周边的点是1或者2，就说明那个点
                    # 上一轮是活的
                    if 0 <= x < m and 0 <= y < n and   \
                       (board[x][y] == 1 or board[x][y] == 2):
                       lives += 1
                if board[i][j] == 1 and (lives < 2 or lives > 3):
                    board[i][j] = 2 # 上一轮是1，这一轮过后变为0
                elif board[i][j] == 0 and lives == 3: 
                    board[i][j] = 3 # 上一轮是0，这一轮过后变为1
        for i in range(m):
            for j in range(n):
                board[i][j] %= 2   
        return

if __name__ == "__main__":
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    for b in board: print(b)
    Solution().gameOfLife(board)
    for b in board: print(b)
    board = [[1,1],[1,0]]
    for b in board: print(b)
    Solution().gameOfLife(board)
    for b in board: print(b)

    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    for b in board: print(b)
    Solution().gameOfLifeBit(board)
    for b in board: print(b)