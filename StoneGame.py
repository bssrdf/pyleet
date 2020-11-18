


'''
Alex and Lee play a game with piles of stones.  There are an even number of piles 
arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones 
is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the 
entire pile of stones from either the beginning or the end of the row.  This continues 
until there are no more piles left, at which point the person with the most stones 
wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

 

Example 1:

Input: piles = [5,3,4,5]
Output: true
Explanation: 
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
 

Constraints:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles) is odd.


'''
'''

This is a Minimax problem. Each player plays optimally to win, but you can't greedily 
choose the optimal strategy so you have to try all strategies, this is DP now.

What does it mean for Alex to win? Alex will win if score(Alex) >= score(Lee), but 
this also means score(Alex) - score(Lee) >= 0, so here you have a common parameter 
which is a score variable. The score parameter really means score = score(Alex) - 
score(Lee).

Now, if each player is suppoed to play optimally, how do you decide this with one 
variable?

Well since Alex is playing optimally, he wants to maximize the score variable 
because remember, Alex only wins if score = score(Alex) - score(Lee) >= 0 Alex 
should add to the score because he wants to maximize it.

Since Lee is also playing optimally, he wants to minimize the score variable, since 
if the score variable becomes negative, Lee has more individual score than Alex. 
But since we have only one variable, Lee should damage the score (or in other words,
 subtract from the score).

Now, let's think of the brute force solution. You are at the current state, say this 
is Alex's turn. Alex can choose either left or right, but he can't greedily pick so 
you try both of them, this is O(2^n) for runtime.

But realize the state you are in. You can easily memoize the this, the varying 
parameters are l, r, ID, where ID is the player ID (1 for Alex, 0 for Lee), hence 
you can make a DP/Cache table and return answer if you have discovered the state.

Finally, in your main function you call this helper function and check if you were 
able to get a score >= 0.


'''


from collections import deque

class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        '''
        Greedy approach does not work. One can try a few cases to see this.
        DP is the way. What are the states? Playing this game requires one to choose
        from either left end or right end. This should give a hint for (l,r) or (i,j)
        Then the game is played by two players. so another deimension is (2). 
        The state is (l,r,id) with id is 1 or 0. Hence the 3-d memo array

        Here DP with memoization can be used. The rrecursion is on 3 state variables,
        l , r, and id. The value we are computing is a minmax function:
         max for Alex and min for Lee 
        '''
        memo = [[[-1]*2 for _ in range(n)] for j in range(n)]        
        def helper(l, r, ID):
            if r < l:
                return 0
            if memo[l][r][ID] != -1:                  
                return memo[l][r][ID] 
            ne = 1 if ID == 0 else 1       
            if ID == 1:
                memo[l][r][ID] = max(piles[l]+helper(l+1,r,ne),
                                     piles[r]+helper(l,r-1,ne))
            else:
                memo[l][r][ID] = min(-piles[l]+helper(l+1,r,ne),
                                     -piles[r]+helper(l,r-1,ne))            
            return memo[l][r][ID]      
        # start from two ends at 0 and n-1 with Alex playing first
        return helper(0, n-1, 1) >= 0
        
        
if __name__ == "__main__":
    print(Solution().stoneGame([5,7,2,3]))
        