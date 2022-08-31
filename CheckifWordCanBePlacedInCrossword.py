'''

-Medium-

You are given an m x n matrix board, representing the current state of a crossword puzzle. The crossword contains lowercase English letters (from solved words), ' ' to represent any empty cells, and '#' to represent any blocked cells.

A word can be placed horizontally (left to right or right to left) or vertically (top to bottom or bottom to top) in the board if:

It does not occupy a cell containing the character '#'.
The cell each letter is placed in must either be ' ' (empty) or match the letter already on the board.
There must not be any empty cells ' ' or other lowercase letters directly left or right of the word if the word was placed horizontally.
There must not be any empty cells ' ' or other lowercase letters directly above or below the word if the word was placed vertically.
Given a string word, return true if word can be placed in board, or false otherwise.

 

Example 1:


Input: board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], word = "abc"
Output: true
Explanation: The word "abc" can be placed as shown above (top to bottom).
Example 2:


Input: board = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], word = "ac"
Output: false
Explanation: It is impossible to place the word because there will always be a space/letter above or below it.
Example 3:


Input: board = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], word = "ca"
Output: true
Explanation: The word "ca" can be placed as shown above (right to left). 
 

Constraints:

m == board.length
n == board[i].length
1 <= m * n <= 2 * 105
board[i][j] will be ' ', '#', or a lowercase English letter.
1 <= word.length <= max(m, n)
word will contain only lowercase English letters.



'''

from typing import List

class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        B, W = board, word
        m, n = len(board), len(board[0])
        left, right = [[-1]*n for _ in range(m)], [[n]*n for _ in range(m)] 
        up, down = [[-1]*n for _ in range(m)], [[m]*n for _ in range(m)] 
        for i in range(m):
            k = -1            
            for j in range(n):
                if B[i][j] != '#': left[i][j] = k
                else: k = j 
            k = n            
            for j in range(n-1, -1, -1):
                if B[i][j] != '#': right[i][j] = k
                else: k = j 
        for j in range(n):
            k = -1            
            for i in range(m):
                if B[i][j] != '#': up[i][j] = k
                else: k = i 
            k = m            
            for i in range(m-1, -1, -1):
                if B[i][j] != '#': down[i][j] = k
                else: k = i 
        for i in range(m):
            for j in range(n):
                if B[i][j] != '#':
                    if j == 0 or B[i][j-1] == '#':
                        if right[i][j] - j == len(W):
                            valid = True
                            for k in range(len(W)):
                                if B[i][j+k] != ' ' and B[i][j+k] != W[k]:
                                    valid = False
                                    break
                            if valid: return True 
                    if j == n-1 or B[i][j+1] == '#':
                        if j - left[i][j] == len(W):
                            valid = True
                            for k in range(len(W)):
                                if B[i][j-k] != ' ' and B[i][j-k] != W[k]:
                                    valid = False
                                    break
                            if valid: return True 
        for j in range(n):
            for i in range(m):
                if B[i][j] != '#':
                    if i == 0 or B[i-1][j] == '#':
                        if down[i][j] - i == len(W):
                            valid = True
                            for k in range(len(W)):
                                if B[i+k][j] != ' ' and B[i+k][j] != W[k]:
                                    valid = False
                                    break
                            if valid: return True 
            
                    if i == m-1 or B[i+1][j] == '#':
                        if i - up[i][j] == len(W):
                            valid = True
                            for k in range(len(W)):
                                if B[i-k][j] != ' ' and B[i-k][j] != W[k]:
                                    valid = False
                                    break
                            if valid: return True 
        return False
    
    def placeWordInCrossword2(self, board: List[List[str]], word: str) -> bool:
        words=[word,word[::-1]]
        n=len(word)
        for B in board,zip(*board):
            for row in B:
                q=''.join(row).split('#')
                for w in words:
                    for s in q:
                        if len(s)==n:
                            if all(s[i]==w[i] or s[i]==' ' for i in range(n)):
                                return True
        return False

                                  

        






if __name__ == "__main__":
    board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]]
    word = "abc"
    print(Solution().placeWordInCrossword(board = board, word = word))
    board = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]]
    word = "ac"
    print(Solution().placeWordInCrossword(board = board, word = word))
    board = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]]
    word = "ca"
    print(Solution().placeWordInCrossword(board = board, word = word))
    board = [[" "],["#"],["o"],[" "],["t"],["m"],["o"],[" "],["#"],[" "]]
    word = "octmor"
    print(Solution().placeWordInCrossword(board = board, word = word))


        