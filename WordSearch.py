# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 17:58:20 2017
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" 
cells are those horizontally or vertically neighboring. The same letter cell may not be 
used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.


@author: merli
"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False
    # check whether can find word, start at (i,j) position    
    def dfs(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian 
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
        or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res
    
    def exist2(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        # check whether can find word, start at (i,j) position    
        def dfs(board, i, j, k):
            if k == len(word): # all the characters are checked
                return True
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[k]!=board[i][j]:
                return False
            tmp = board[i][j]  # first character is found, check the remaining part
            board[i][j] = "#"  # avoid visit agian 
            # check whether can find "word" along one direction
            res = dfs(board, i+1, j, k+1) or dfs(board, i-1, j, k+1) \
                 or dfs(board, i, j+1, k+1) or dfs(board, i, j-1, k+1)
            board[i][j] = tmp
            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, i, j, 0):
                    return True
        return False
    
        
if __name__ == "__main__":
    board = [
  ['A','B','C','E'],
  ['S','F','E','S'],
  ['A','D','E','E']
              ]
#    print Solution().exist(board, "ABCCED")
#    print Solution().exist(board, "SEE")
#    print Solution().exist(board, "ABCB")
#    print Solution().exist(board, "AA")
    print(Solution().exist(board, "ABCESEEEFS"))
    print(Solution().exist2(board, "ABCESEEEFS"))