'''
-Medium-

On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].

Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in 
the diagram below.



We may make the following moves:

'U' moves our position up one row, if the position exists on the board;
'D' moves our position down one row, if the position exists on the board;
'L' moves our position left one column, if the position exists on the board;
'R' moves our position right one column, if the position exists on the board;
'!' adds the character board[r][c] at our current position (r, c) to the answer.
(Here, the only positions that exist on the board are positions with letters on them.)

Return a sequence of moves that makes our answer equal to target in the minimum number of moves.  You may return any path that does so.

 

Example 1:

Input: target = "leet"
Output: "DDR!UURRR!!DDD!"
Example 2:

Input: target = "code"
Output: "RR!DDRR!UUL!R!"
 

Constraints:

1 <= target.length <= 100
target consists only of English lowercase letters.

'''

from string import ascii_lowercase
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = {}
        i = j = 0
        for c in ascii_lowercase:
            board[c] = (i,j)
            j += 1
            if j >= 5: 
                i += 1
                j = 0
        x0, y0 = (0, 0)
        res = []
        for c in target:            
            x, y = board[c]
            # Notice that moving down and moving right,
            # may move into a square that doesn't exist.
            # To avoid this, we put L U before R D.
            if y < y0: res.append('L' * (y0 - y))
            if x < x0: res.append('U' * (x0 - x))
            if x > x0: res.append('D' * (x - x0))
            if y > y0: res.append('R' * (y - y0))
            res.append('!')
            x0, y0 = x, y            
        return "".join(res)


if __name__ == "__main__":
    print(Solution().alphabetBoardPath('leet'))
    print(Solution().alphabetBoardPath('zd'))