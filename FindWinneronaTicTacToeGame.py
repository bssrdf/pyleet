'''
-Medium-

Tic-tac-toe is played by two players A and B on a 3 x 3 grid.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player A always places "X" characters, while the second player B always places "O" characters.
"X" and "O" characters are always placed into empty squares, never on filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given an array moves where each element is another array of size 2 corresponding to the row and column 
of the grid where they mark their respective character in the order in which A and B play.

Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw", 
if there are still movements to play return "Pending".

You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty 
and A will play first.

 

Example 1:

Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: "A" wins, he always plays first.
"X  "    "X  "    "X  "    "X  "    "X  "
"   " -> "   " -> " X " -> " X " -> " X "
"   "    "O  "    "O  "    "OO "    "OOX"
Example 2:

Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: "B" wins.
"X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"
"   " -> " O " -> " O " -> " O " -> "XO " -> "XO " 
"   "    "   "    "   "    "   "    "   "    "O  "
Example 3:

Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.
"XXO"
"OOX"
"XOX"
Example 4:

Input: moves = [[0,0],[1,1]]
Output: "Pending"
Explanation: The game has not finished yet.
"X  "
" O "
"   "
 

Constraints:

1 <= moves.length <= 9
moves[i].length == 2
0 <= moves[i][j] <= 2
There are no repeated elements on moves.
moves follow the rules of tic tac toe.


'''

class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        board = [[' ']*3 for _ in range(3)]
        def winner(x,y,c):
            cnt = 0   
            for i in range(3):
                if board[i][y] == c: cnt += 1
            if cnt == 3: return True
            cnt = 0   
            for j in range(3):
                if board[x][j] == c: cnt += 1
            if cnt == 3: return True                        
            if y-x == 0:
                cnt = 0   
                for i in range(3):
                    if board[i][i] == c: cnt += 1
                if cnt == 3: return True
            if y+x == 2:
                cnt = 0   
                for i in range(3):
                    if board[i][2-i] == c: cnt += 1
                if cnt == 3: return True
            return False
        steps = 0
        for i, (x,y) in enumerate(moves):
            (c,p) = ('X','A') if i%2==0 else ('O','B')
            board[x][y] = c
            steps += 1
            if steps >= 5:
               if winner(x, y, c): return p            
        return 'Draw' if steps == 9 else 'Pending'


if __name__ == "__main__":
    print(Solution().tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))
    print(Solution().tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))
    print(Solution().tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]))
    print(Solution().tictactoe([[2,0],[1,0],[1,1],[0,2]]))