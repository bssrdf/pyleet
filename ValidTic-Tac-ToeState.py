'''

-Medium-

A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player always places "X" characters, while the second player always places "O" characters.
"X" and "O" characters are always placed into empty squares, never filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Example 1:
Input: board = ["O  ", "   ", "   "]
Output: false
Explanation: The first player always plays "X".

Example 2:
Input: board = ["XOX", " X ", "   "]
Output: false
Explanation: Players take turns making moves.

Example 3:
Input: board = ["XXX", "   ", "OOO"]
Output: false

Example 4:
Input: board = ["XOX", "O O", "XOX"]
Output: true
Note:

board is a length-3 array of strings, where each string board[i] has length 3.
Each board[i][j] is a character in the set {" ", "X", "O"}.

'''

class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        rows = [0] * 3
        cols = [0] * 3
        diag, rev_diag, turns = 0, 0, 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'X':
                    turns += 1
                    rows[i] += 1
                    cols[j] += 1
                    diag += 1 if i == j else 0
                    rev_diag += 1 if i+j == 2 else 0
                if board[i][j] == 'O':
                    turns -= 1
                    rows[i] -= 1
                    cols[j] -= 1
                    diag -= 1 if i == j else 0
                    rev_diag -= 1 if i+j == 2 else 0
        xwin = any([r==3 for r in rows]) or any([c==3 for c in cols]) or \
               diag == 3 or rev_diag == 3
        owin = any([r==-3 for r in rows]) or any([c==-3 for c in cols]) or \
               diag == -3 or rev_diag == -3
        if xwin and turns == 0 or owin and turns == 1:
            return False
        return (turns == 1 or turns == 0) and (not xwin or not owin)
                



        

if __name__ == "__main__":
    print(Solution().validTicTacToe(["XXX", "   ", "OOO"]))
    print(Solution().validTicTacToe(["XOX"," X ","   "]))