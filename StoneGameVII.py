'''
-Medium-

Alice and Bob take turns playing a game, with Alice starting first.

There are n stones arranged in a row. On each player's turn, they can remove 
either the leftmost stone or the rightmost stone from the row and receive points 
equal to the sum of the remaining stones' values in the row. The winner is the 
one with the higher score when there are no stones left to remove.

Bob found that he will always lose this game (poor Bob, he always loses), so 
he decided to minimize the score's difference. Alice's goal is to maximize 
the difference in the score.

Given an array of integers stones where stones[i] represents the value of the 
ith stone from the left, return the difference in Alice and Bob's score if 
they both play optimally.

 

Example 1:

Input: stones = [5,3,1,4,2]
Output: 6
Explanation: 
- Alice removes 2 and gets 5 + 3 + 1 + 4 = 13 points. Alice = 13, Bob = 0, stones = [5,3,1,4].
- Bob removes 5 and gets 3 + 1 + 4 = 8 points. Alice = 13, Bob = 8, stones = [3,1,4].
- Alice removes 3 and gets 1 + 4 = 5 points. Alice = 18, Bob = 8, stones = [1,4].
- Bob removes 1 and gets 4 points. Alice = 18, Bob = 12, stones = [4].
- Alice removes 4 and gets 0 points. Alice = 18, Bob = 12, stones = [].
The score difference is 18 - 12 = 6.
Example 2:

Input: stones = [7,90,5,1,100,10,10,2]
Output: 122
 

Constraints:

n == stones.length
2 <= n <= 1000
1 <= stones[i] <= 1000

'''
from itertools import accumulate

class Solution(object):
    def stoneGameVIITLE(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        memo = [[[-1]*2 for _ in range(n)] for j in range(n)] 
        sm = sum(stones)       
        def helper(l, r, ID, left):
            #print('A', ID, l, r, left)
            if r < l:
                return 0
            if memo[l][r][ID] != -1:                  
                return memo[l][r][ID] 
            ne = 1 if ID == 0 else 0  
            #print('C', ne, l, r, left)    
            if ID == 1:
                memo[l][r][ID] = max(left-stones[l]+helper(l+1,r,ne,left-stones[l]),
                                     left-stones[r]+helper(l,r-1,ne,left-stones[r]))
            else:
                memo[l][r][ID] = min(stones[l]-left+helper(l+1,r,ne,left-stones[l]),
                                     stones[r]-left+helper(l,r-1,ne,left-stones[r]))            
            #print('B', ID, l, r, memo[l][r][ID])
            return memo[l][r][ID]      
        # start from two ends at 0 and n-1 with Alex playing first
        return helper(0, n-1, 1, sm)
        #return memo[0][n-1][1]
    def stoneGameVII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """   
        s = stones
        dp = [[0] * len(s) for _ in range(len(s))]
        p_sum = [0] + list(accumulate(s))
        def dfs(i: int, j: int) -> int:
            if i == j:
                return 0
            if dp[i][j] == 0:
                sum = p_sum[j + 1] - p_sum[i]
                dp[i][j] = max(sum - s[i] - dfs(i + 1, j), sum - s[j] - dfs(i, j - 1))
            return dp[i][j]
        res = dfs(0, len(s) - 1)
        return res 
    def stoneGameVIIDP(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """    
        """
        dp[i][j]: max score difference when stones[i:j+1] are left
        dp[i][j] = max(score_taking_i  - dp[i+1][j],
                       score_taking_j  - dp[i][j+1] )
        """
        s = stones
        dp = [[0] * len(s) for _ in range(len(s))]
        p_sum = [0] + list(accumulate(s))
        for i in range(len(s) - 2, -1, -1): # go from len(s) to 0 because 
                                            # dp[i][j] depends on dp[i+1][j]
            for j in range(i + 1, len(s)):
                score_taking_i = p_sum[j + 1] - p_sum[i + 1]
                score_taking_j = p_sum[j] - p_sum[i]
                dp[i][j] = max(score_taking_i - dp[i + 1][j], 
                               score_taking_j - dp[i][j - 1])
        return dp[0][len(s) - 1]   

if __name__ == "__main__":
    print(Solution().stoneGameVIIDP(stones = [5,3,1,4,2]))
    print(Solution().stoneGameVII(stones = [7,90,5,1,100,10,10,2]))