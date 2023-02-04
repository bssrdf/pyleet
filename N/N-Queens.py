'''
-Hard-
*Backtracking*
The n-queens puzzle is the problem of placing n queens on an n×n 
chessboard such that no two queens attack each other.

Each solution contains a distinct board configuration of the n-queens' placement,
 where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
 

Constraints:

1 <= n <= 9

'''

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [['.' for _ in range(n)] for _ in range(n)]
        ans = []
        def isValid(row, col):
            # check if there is already a queen on this col
            # no need to check if there is already a queen on this row
            # because we only put 1 queen on each row
            for i in range(n):
                if board[i][col] == 'Q':
                    return False
            # check diagonal from lower left to upper right  
            # only check rows above because we are always going down      
            i,j = row-1, col+1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            # check diagonal from lower right to upper left  
            # only check rows above because we are always going down   
            i,j = row-1, col-1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            return True

        def backtrack(i):
            if i == n:
                ans.append([''.join(b) for b in board])
                return
            for j in range(n): # check each col               
                if not isValid(i, j): # if not a valid pos
                    continue          # move on to next col
                board[i][j] = 'Q'     # put down the queen
                backtrack(i+1)        # move on to next row 
                board[i][j] = '.'     # back tracking 
        backtrack(0) # start from the 1st queen at row 0
        return ans


if __name__ == "__main__":
    board = Solution().solveNQueens(4)
    for b in board:
        for l in b:
            print(l)
        print('======')