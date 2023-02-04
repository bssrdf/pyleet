'''
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated 
according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

The Sudoku board could be partially filled, where empty cells are filled with the 
character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true

'''
from collections import defaultdict

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n = 9        
        for i in range(n):            
            digits = set()
            for j in range(n):
                if board[i][j] != '.':
                    if board[i][j] in digits:                        
                        return False                       
                    else:
                        digits.add(board[i][j])
        for j in range(n):            
            digits = set()
            for i in range(n):
                if board[i][j] != '.':
                    if board[i][j] in digits:                        
                        return False                       
                    else:
                        digits.add(board[i][j])
        
        for rowGroup in range(0,3):
            for colGroup in range(0,3):
                digits = set()
                for i in range(rowGroup*3, rowGroup*3+3):
                    for j in range(colGroup*3, colGroup*3+3):                        
                        if board[i][j] != '.':
                            if board[i][j] in digits:                        
                               return False                       
                            else:
                               digits.add(board[i][j])
                     
        return True
                    




if __name__ == "__main__":
    '''
    s = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
  ]
    '''
    '''
    s = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
'''
    s = [
    [".",".",".",".","5",".",".","1","."],
    [".","4",".","3",".",".",".",".","."],
    [".",".",".",".",".","3",".",".","1"],
    ["8",".",".",".",".",".",".","2","."],
    [".",".","2",".","7",".",".",".","."],
    [".","1","5",".",".",".",".",".","."],
    [".",".",".",".",".","2",".",".","."],
    [".","2",".","9",".",".",".",".","."],
    [".",".","4",".",".",".",".",".","."]
    ]
    print(Solution().isValidSudoku(s))