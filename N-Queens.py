'''
The n-queens puzzle is the problem of placing n queens on an n×n 
chessboard such that no two queens attack each other.

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
            for i in range(n):
                if board[i][col] == 'Q':
                    return False
            i,j = row-1, col+1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
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
            for j in range(n):                
                if not isValid(i, j):
                    continue 
                board[i][j] = 'Q'
                backtrack(i+1)
                board[i][j] = '.'
        backtrack(0)
        return ans


if __name__ == "__main__":
    board = Solution().solveNQueens(4)
    for b in board:
        for l in b:
            print(l)
        print('======')