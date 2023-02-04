'''
-Hard-
*Memoization*
*Backtracking*
You are playing a variation of the game Zuma.

In this variation of Zuma, there is a single row of colored balls on a board, where each 
ball can be colored red 'R', yellow 'Y', blue 'B', green 'G', or white 'W'. You also have 
several colored balls in your hand.

Your goal is to clear all of the balls from the board. On each turn:

Pick any ball from your hand and insert it in between two balls in the row or on either end of the row.
If there is a group of three or more consecutive balls of the same color, remove the group of balls 
from the board.
If this removal causes more groups of three or more of the same color to form, then continue removing 
each group until there are none left.
If there are no more balls on the board, then you win the game.
Repeat this process until you either win or do not have any more balls in your hand.
Given a string board, representing the row of balls on the board, and a string hand, representing the 
balls in your hand, return the minimum number of balls you have to insert to clear all the balls 
from the board. If you cannot clear all the balls from the board using the balls in your hand, return -1.

 

Example 1:

Input: board = "WRRBBW", hand = "RB"
Output: -1
Explanation: It is impossible to clear all the balls. The best you can do is:
- Insert 'R' so the board becomes WRRRBBW. WRRRBBW -> WBBW.
- Insert 'B' so the board becomes WBBBW. WBBBW -> WW.
There are still balls remaining on the board, and you are out of balls to insert.
Example 2:

Input: board = "WWRRBBWW", hand = "WRBRW"
Output: 2
Explanation: To make the board empty:
- Insert 'R' so the board becomes WWRRRBBWW. WWRRRBBWW -> WWBBWW.
- Insert 'B' so the board becomes WWBBBWW. WWBBBWW -> WWWW -> empty.
2 balls from your hand were needed to clear the board.
Example 3:

Input: board = "G", hand = "GGGGG"
Output: 2
Explanation: To make the board empty:
- Insert 'G' so the board becomes GG.
- Insert 'G' so the board becomes GGG. GGG -> empty.
2 balls from your hand were needed to clear the board.
Example 4:

Input: board = "RBYYBBRRB", hand = "YRBGB"
Output: 3
Explanation: To make the board empty:
- Insert 'Y' so the board becomes RBYYYBBRRB. RBYYYBBRRB -> RBBBRRB -> RRRB -> B.
- Insert 'B' so the board becomes BB.
- Insert 'B' so the board becomes BBB. BBB -> empty.
3 balls from your hand were needed to clear the board.
 

Constraints:

1 <= board.length <= 16
1 <= hand.length <= 5
board and hand consist of the characters 'R', 'Y', 'B', 'G', and 'W'.
The initial row of balls on the board will not have any groups of three or more consecutive balls of the same color.

'''
from functools import lru_cache
from collections import Counter

class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        INT_MAX = 10**9
        res = INT_MAX
        m = Counter(hand)
        def removeConsecutive(board):
            j = 0
            for i in range(len(board)+1):
                if i < len(board) and board[i] == board[j]: continue
                if i - j >= 3: return removeConsecutive(board[:j] + board[i:])
                else: j = i
            return board
        #s = 'RRRRBBRR'
        #t = removeConsecutive(s) 
        #print('t= ',t)
        def helper(board,  m):
            #print('before remove: ', board)
            #board = removeConsecutive(board)
            #print('after  remove: ', board)
            if not board: return 0
            cnt, j = INT_MAX, 0
            for i in range(len(board)+1):
                if i < len(board) and board[i] == board[j]: continue
                need = 3 - (i - j)
              #  print(board, need, i, j, board[j])
                if m[board[j]] >= need:
                    m[board[j]] -= need
                    t = helper(board[:j] + board[i:], m)
                    if t != INT_MAX: cnt = min(cnt, t + need)
                    m[board[j]] += need
                j = i
            return cnt        
        res = helper(board, m)
        return -1 if res == INT_MAX else res

    def findMinStepWrong(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        def remove(b):
            i = 0
            for j in range(len(b)+1):
                if j == len(b) or b[j] != b[i]:
                    if j - i >= 3:
                        return remove(b[:i]+b[j:])
                    i = j
            return b
        
        @lru_cache(None)
        def dfs(b, h):
            b = remove(b)
            if b and not h: return float('inf')
            if not b: return 0
            
            res = float('inf')
            for i in range(len(b)+1):
                for j in range(len(h)):
                    res = min(res, 1 + dfs(b[:i] + h[j] + b[i:], h[:j] + h[j+1:]))
            return res
        
        hand = ''.join(filter(lambda x: x in board, hand))
        #print(hand)
        res = dfs(board, hand)
        return res if res != float('inf') else -1

    def findMinStepAC(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        @lru_cache(None)
        def remove(b):
            i = 0
            for j in range(len(b)+1):
                if j == len(b) or b[j] != b[i]:
                    if j - i >= 3:
                        return remove(b[:i]+b[j:])
                    i = j
            return b

        @lru_cache(None)
        def clean(board):
            stack = []
            for b in board:
                if stack and stack[-1][0] != b and stack[-1][1] >= 3:
                    stack.pop()
                if not stack or stack[-1][0] != b:
                    stack += [b, 1],
                else:
                    stack[-1][1] += 1
            if stack and stack[-1][1] >= 3:
                stack.pop()
            return ''.join([a*b for a,b in stack])

        @lru_cache(None)
        def dfs(board, hand):
            if not board:
                return 0
            if not hand:
                return float('inf')
            m = len(board)
            ans = float('inf')
            for j, b in enumerate(hand):
                new_hand = hand[:j] + hand[j+1:]
                for i in range(m + 1):
                    #new_board = clean(board[:i] + b + board[i:])
                    new_board = remove(board[:i] + b + board[i:])
                    ans = min(ans, 1 + dfs(new_board, new_hand))
            return ans
        
        ans = dfs(board, hand)
        return ans if ans < float('inf') else -1

if __name__ == "__main__": 
    #print(Solution().findMinStep(board = "WRRBBW", hand = "RB"))
    #print(Solution().findMinStep(board = "RBYYBBRRB", hand = "YRBGB"))
    #print(Solution().findMinStep("RRWWRRBBRR", "WB"))
    #print(Solution().findMinStepAC("RRWWRRBBRR", "WB"))
    print(Solution().findMinStepAC("RRYGGYYRRYYGGYRR","GGBBB"))