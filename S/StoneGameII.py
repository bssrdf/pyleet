'''
Alex and Lee continue their games with piles of stones.  There are a number of piles 
arranged in a row, and each pile has a positive integer number of stones piles[i].  
The objective of the game is to end with the most stones. 

Alex and Lee take turns, with Alex starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining 
piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alex and Lee play optimally, return the maximum number of stones Alex 
can get.

 

Example 1:

Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alex takes one pile at the beginning, Lee takes two piles, then 
Alex takes 2 piles again. Alex can get 2 + 4 + 4 = 10 piles in total. If Alex 
takes two piles at the beginning, then Lee can take all three piles left. 
In this case, Alex get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
 

Constraints:

1 <= piles.length <= 100
1 <= piles[i] <= 10 ^ 4

'''

class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)
        total = [0]*n
        dp = [[0]*n for _ in range(n)]
        total[n-1] = piles[n-1]
        for i in range(n-2, -1, -1):
            total[i] = total[i+1]+piles[i]
        '''        
        DP is the way. What are the states? Playing this game requires one to choose
        x piles from the remaining ones and 1<=x<=2M. This should give a hint for (i,M)
        Then the game is played by two players. so another dimension could be (2). 
        But we can also skip the 2 players dimention. and let F(i,M) be the most stones
        one player can get if the first i piles were not there.(as i changes, F corresponds
        to either player).        

        Here DP with memoization can be used. The recursion is on 2 state variables,
        i and M. The value we are computing is defined as above;
        Each call of helper function represents one player's play. 
         
        '''
        def helper(i, M):
            if i==n: return 0
            #when M is big enough, one player can take all what are left
            if 2*M >= n - i:
                return total[i]
            if dp[i][M] != 0: return dp[i][M]
            tmp = 10**7
            # the way the recursion is done is playing the game reversely
            #  
            for x in range(1, 2*M+1): 
                tmp = min(tmp, helper(i+x, max(M, x)))
            dp[i][M] = total[i] - tmp
            return dp[i][M]

        return helper(0, 1)
        
        
if __name__ == "__main__":
    print(Solution().stoneGameII([2,7,9,4,4]))