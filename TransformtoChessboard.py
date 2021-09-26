'''
-Hard-

You are given an n x n binary grid board. In each move, you can swap any two rows with each other, 
or any two columns with each other.

Return the minimum number of moves to transform the board into a chessboard board. If the task is 
impossible, return -1.

A chessboard board is a board where no 0's and no 1's are 4-directionally adjacent.

 

Example 1:


Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
Output: 2
Explanation: One potential sequence of moves is shown.
The first move swaps the first and second column.
The second move swaps the second and third row.
Example 2:


Input: board = [[0,1],[1,0]]
Output: 0
Explanation: Also note that the board with 0 in the top left corner, is also a valid chessboard.
Example 3:


Input: board = [[1,0],[1,0]]
Output: -1
Explanation: No matter what sequence of moves you make, you cannot end with a valid chessboard.
 

Constraints:

n == board.length
n == board[i].length
2 <= n <= 30
board[i][j] is either 0 or 1.

'''

class Solution(object):
    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        b = board
        N = len(b)
        if any(b[0][0] ^ b[i][0] ^ b[0][j] ^ b[i][j] for i in range(N) for j in range(N)): return -1
        if not N // 2 <= sum(b[0]) <= (N + 1) // 2: return -1
        if not N // 2 <= sum(b[i][0] for i in range(N)) <= (N + 1) // 2: return -1
        # Check the first row and first row, how many matches 1010101...
        # 1) When matching 01010101..., we count the row/col that matches this pattern, say nr/nc, 
        #    (there is another underlying matching pattern 10101010... that is also valid, but the count 
        #    would be N-nr or N-nc, so only one matching test is needed).
        # 2) Now the key point in the logic is the number of row/cols that are NOT in their proper position 
        #    must be even, since each such row/col must swap with another such row/col.
        # 3) So if n is even, then that's the number of row/col that are NOT in proper position (since N-n 
        #    is odd and can't be the row/col not in proper position). The underlying matching case is the 
        #    other case (10101010...).
        #    If n is odd, then N-n is the number of row/col that are not in proper position since n can't be. 
        #    The underlying matching case is 01010101...
        col = sum(b[0][i] == i % 2 for i in range(N))
        row = sum(b[i][0] == i % 2 for i in range(N))
        #print(col, row)
        if N % 2: # N is odd, mismatches must be even
            if col % 2: col = N - col # if number of mismatches is odd, match 010101....
            if row % 2: row = N - row # if number of mismatches is odd, match 010101....
        else:     # N is even
            col = min(N - col, col)
            row = min(N - row, row)
        return (col + row) // 2

if __name__ == "__main__":
    board = [[0,1,1,0],
             [0,1,1,0],
             [1,0,0,1],
             [1,0,0,1]]
    print(Solution().movesToChessboard(board))
    board = [[0,1,0,1],
             [1,0,1,0],
             [0,1,0,1],
             [1,0,1,0]]
    print(Solution().movesToChessboard(board))
    board = [[1,0,1,0],
             [0,1,0,1],
             [1,0,1,0],
             [0,1,0,1]]
    print(Solution().movesToChessboard(board))
