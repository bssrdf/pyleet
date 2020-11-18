'''
-Medium-
*DP*
*Memoization*
*DFS*

On an NxN chessboard, a knight starts at the r-th row and c-th column and 
attempts to make exactly K moves. The rows and columns are 0 indexed, so 
the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. 
Each move is two squares in a cardinal direction, then one square in an 
orthogonal direction.


 

Each time the knight is to move, it chooses one of eight possible moves 
uniformly at random (even if the piece would go off the chessboard) and 
moves there.

The knight continues moving until it has made exactly K moves or has moved 
off the chessboard. Return the probability that the knight remains on the 
board after it has stopped moving.

 

Example:

Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight 
on the board.
From each of those positions, there are also two moves that will keep the 
knight on the board.
The total probability the knight stays on the board is 0.0625.
 

Note:

N will be between 1 and 25.
K will be between 0 and 100.
The knight always initially starts on the board.


'''


class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        if K == 0: return 1.0
        if N <= 2: return 0.0
        dirs = [(-2, 1), (-1, 2), (1, 2), (2, 1),
                (-2, -1), (-1, -2), (1, -2), (2, -1)]
        memo = [[[-1 for _ in range(K)] for _ in range(N)] for _ in range(N)]  
        def dfs(i,j,k):
            if i < 0 or i > N-1 or j < 0 or j > N-1:
                return 0.0
            if k == K:
                return (1/8)**k
            if memo[i][j][k] != -1:
                return memo[i][j][k]   
            ib = 0    
            for di, dj in dirs:
                ib += dfs(i+di, j+dj, k+1)                
            memo[i][j][k] = ib                
            return memo[i][j][k]       
        return dfs(r,c,0)
        
if __name__ == "__main__":
    print(Solution().knightProbability(3, 2, 0, 0))