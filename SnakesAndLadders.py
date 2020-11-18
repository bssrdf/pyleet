'''
Medium
*BFS*

On an N x N board, the numbers from 1 to N*N are written boustrophedonically starting from 
the bottom left of the board, and alternating direction each row.  For example, for a 6 x 6 
board, the numbers are written as follows:

You start on square 1 of the board (which is always in the last row and first column).  Each 
move, starting from square x, consists of the following:

You choose a destination square S with number x+1, x+2, x+3, x+4, x+5, or x+6, provided 
this number is <= N*N.
(This choice simulates the result of a standard 6-sided die roll: ie., there are always at 
most 6 destinations, regardless of the size of the board.)
If S has a snake or ladder, you move to the destination of that snake or ladder.  Otherwise, 
you move to S.
A board square on row r and column c has a "snake or ladder" if board[r][c] != -1.  The 
destination of that snake or ladder is board[r][c].

Note that you only take a snake or ladder at most once per move: if the destination to a 
snake or ladder is the start of another snake or ladder, you do not continue moving.  
(For example, if the board is `[[4,-1],[-1,3]]`, and on the first move your destination 
square is `2`, then you finish your first move at `3`, because you do not continue moving 
to `4`.)

Return the least number of moves required to reach square N*N.  If it is not possible, 
return -1.

Example 1:

Input: [
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation: 
At the beginning, you start at square 1 [at row 5, column 0].
You decide to move to square 2, and must take the ladder to square 15.
You then decide to move to square 17 (row 3, column 5), and must take the snake to square 13.
You then decide to move to square 14, and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
It can be shown that you need at least 4 moves to reach the N*N-th square, so the answer is 4.
'''
from collections import deque


class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        n2 = n * n
        snake_ladder = [-1] * n2    
        def map_pos(i,j):
            if (n-i) % 2 == 1:
                return n*(n-i-1)+j+1
            else:
                return n*(n-i)-j       
        
        for i in range(n):
            for j in range(n):
                pos = map_pos(i,j)            
                snake_ladder[pos-1] = board[i][j] 
              
        dq = deque([(1,0)])
        visited = [False] * n2        
        visited[0] = True
        while dq:
            p, moves = dq.popleft()
            if p == n2: return moves
            # 0) at a ladder position, the next move is also via dice; if the last move
            #  is a dice move, we jump
            # 1) always find the next position using a dice, even at a ladder/snake
            # 2) p could be a ladder/snake position which must be due to the last move
            #   being a ladder (can't do more than 2 ladders in one move)
            for nxt in range(p+1, p+7): 
                nxt = min(nxt, n2)
                if snake_ladder[nxt-1] > -1:   # if next move arrives at a ladder, immediately
                    dest = snake_ladder[nxt-1] # jump to the ladder postion; this counts as one move                      
                else:
                    dest = nxt 
                if not visited[dest-1]:
                    visited[dest-1] = True                    
                    dq.append((dest, moves+1))
        return -1

if __name__ == "__main__":
    input = [
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]
 ]
    print(Solution().snakesAndLadders(input))
    input = [[-1,1,2,-1],
             [2,13,15,-1],
             [-1,10,-1,-1],
             [-1,6,2,8]]

    print(Solution().snakesAndLadders(input))
    input = [[-1,-1,30,14,15,-1],
             [23,9,-1,-1,-1,9],
             [12,5,7,24,-1,30],
             [10,-1,-1,-1,25,17],
             [32,-1,28,-1,-1,32],
             [-1,-1,23,-1,13,19]]
    print(Solution().snakesAndLadders(input))