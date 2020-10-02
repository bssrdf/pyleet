class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        self.solveSudokuRec(board,0,0)
    
    def solveSudokuRec(self, board,row,col):
        if row == 9:
            return True
        if col == 8:
            nextRow = row +1
            nextCol = 0
        else:
            nextRow = row
            nextCol = col+1
        if board[row][col]!='.':
            return self.solveSudokuRec(board,nextRow,nextCol)
        for c in range(1,10):
            if self.canPut(board,str(c),row,col):
                board[row][col] = str(c)
                if self.solveSudokuRec(board,nextRow,nextCol):
                    return True
                board[row][col] = '.'
        return False
    
    def canPut(self, board, char, row, col):
        for i in range(0,9):
            if board[row][i] == char:
                return False
            if board[i][col] == char:
                return False
        rowGroup = (row//3) * 3
        colGroup = (col//3) * 3 
        for i in range(rowGroup, rowGroup+3):
            for j in range(colGroup, colGroup+3):
                if board[i][j] == char:
                    return False
        return True

if __name__=="__main__":
    s = [
  ["2",".",".",".",".",".",".",".","4"],
  [".",".",".","4","8",".","7",".","."],
  ["9","4","8","2",".",".",".",".","."],
  [".","5",".",".",".",".",".","3","."],
  [".",".",".","6","7","4","9",".","5"],
  [".","9","2","1",".",".","4",".","8"],
  ["1","3",".","8",".","9",".",".","6"],
  [".",".","7","5",".","1",".",".","."],
  ["4",".",".",".",".",".",".",".","."]
  ]
    Solution().solveSudoku(s)
    for l in s:
       print(l)
