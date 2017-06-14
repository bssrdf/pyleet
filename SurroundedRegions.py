'''
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
'''

class Solution(object):
    row = [ -1,  0, 0,  1 ]
    col = [  0, -1, 1,  0 ]
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        n=len(board)
        m=len(board[0])
        def DFS(x, y, target, replacement):
            board[x][y] = replacement
            for r,c in zip(self.row, self.col):
                i=x+r
                j=y+c
                if i>=0 and i<len(board) and j>=0 and j<len(board[0]) and board[i][j] == target:        
                    DFS(i, j, target, replacement)
            return
        for r in range(n):
            if board[r][0] == 'O':
                    DFS(r, 0, 'O', 'M')
            if board[r][m-1] == 'O':
                    DFS(r, m-1, 'O', 'M')
        for l in range(m):
            if board[0][l] == 'O':
                    DFS(0, l, 'O', 'M')
            if board[n-1][l] == 'O':
                    DFS(n-1, l, 'O', 'M')
        for r in range(n):
            for l in range(m):
                if board[r][l] == 'M':
                    board[r][l] = 'O'
                else:
                    board[r][l] = 'X'
        return


if __name__ == "__main__":
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X'],
        ['X', 'O', 'X', 'X']
    ]
    for l in board:
        print l
    print
    print
    expected_board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'X', 'X'],
        ['X', 'O', 'X', 'X']
    ]
    Solution().solve(board)
    for l in board:
        print l
    assert board == expected_board
