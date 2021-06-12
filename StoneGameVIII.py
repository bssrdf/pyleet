'''
-Hard-

Alice and Bob take turns playing a game, with Alice starting first.

There are n stones arranged in a row. On each player's turn, while the number of stones is 
more than one, they will do the following:

Choose an integer x > 1, and remove the leftmost x stones from the row.
Add the sum of the removed stones' values to the player's score.
Place a new stone, whose value is equal to that sum, on the left side of the row.
The game stops when only one stone is left in the row.

The score difference between Alice and Bob is (Alice's score - Bob's score). Alice's goal 
is to maximize the score difference, and Bob's goal is the minimize the score difference.

Given an integer array stones of length n where stones[i] represents the value of the ith stone 
from the left, return the score difference between Alice and Bob if they both play optimally.

 

Example 1:

Input: stones = [-1,2,-3,4,-5]
Output: 5
Explanation:
- Alice removes the first 4 stones, adds (-1) + 2 + (-3) + 4 = 2 to her score, and places a stone of
  value 2 on the left. stones = [2,-5].
- Bob removes the first 2 stones, adds 2 + (-5) = -3 to his score, and places a stone of value -3 on
  the left. stones = [-3].
The difference between their scores is 2 - (-3) = 5.
Example 2:

Input: stones = [7,-6,5,10,5,-2,-6]
Output: 13
Explanation:
- Alice removes all stones, adds 7 + (-6) + 5 + 10 + 5 + (-2) + (-6) = 13 to her score, and places a
  stone of value 13 on the left. stones = [13].
The difference between their scores is 13 - 0 = 13.
Example 3:

Input: stones = [-10,-12]
Output: -22
Explanation:
- Alice can only make one move, which is to remove both stones. She adds (-10) + (-12) = -22 to her
  score and places a stone of value -22 on the left. stones = [-22].
The difference between their scores is (-22) - 0 = -22.
 

Constraints:

n == stones.length
2 <= n <= 10^5
-10^4 <= stones[i] <= 10^4


'''

from itertools import accumulate

class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        '''
        Let prefix sum prefix[i] = A[0] + ... + A[i].

        Let dp[i] be the maximum score difference the current player can get when the game starts 
        at i, i.e. stones 0 ~ i are already merged as a new stone i whose value is prefix[i].

        Consider dp[i]: assume the current player chooses to merge stones 0 ~ j (i < j < N), according 
        to the dp definition, the maximum score difference the next player can get using the remaining 
        stones is dp[j]. So the score difference the current player gets is prefix[j] - dp[j].

        The current player will need to try all i < j < N and use the maximum prefix[j] - dp[j] as dp[i]. 
        Thus, we have:

        dp[i] = max( prefix[j] - dp[j] | i < j <= N - 2 )
        dp[N - 2] = prefix[N - 1] // when there are only two stones left, the current player must take 
        them all.      
        The anser is dp[0].

        We can simplify the above formula into the following form. 
        dp[i] = max( prefix[j] - dp[j] | i < j <= N - 2 )
              = max(prefix[i + 1] - dp[i + 1], prefix[i + 2] - dp[i + 2], ..., prefix[N - 2] - dp[N - 2])
        dp[i + 1] =                        max(prefix[i + 2] - dp[i + 2], ..., prefix[N - 2] - dp[N - 2])

        // so
        dp[i] = max(prefix[i + 1] - dp[i + 1], dp[i + 1])
        
        In this way, dp doesn't have to be an array; we just need to store the latest dp value.

        dp[i] = max( dp[i + 1], prefix[i + 1] - dp[i + 1] )   where 0 <= i < N - 2
        dp[N - 2] = prefix[N - 1]

        the most critical step here is to reduce the time complexity from O(N^2) to O(N), I am trying 
        to explain why we can simplify dp[i] = max( prefix[j] - dp[j] | i < j <= N - 2 ) to
        dp[i] = max( dp[i + 1], prefix[i + 1] - dp[i + 1] ):

        Assume we have 3 remaining stones, and Alice will take her turn:
        [XXXXXX]OOO
        dp[N - 3] = max (sum[N - 2] - dp[N - 2] , sum[N - 1] - dp[N - 1])

        Assume we have 4 remaining stones, and Alice will take her turn:
        [XXXXX]OOOO
        dp[N - 4] = max(sum[N - 3] - dp[N - 3], sum[N - 2] - dp[N - 2] , sum[N - 1] - dp[N - 1])
        Note that max(sum[N - 2] - dp[N - 2] , sum[N - 1] - dp[N - 1]) is what we already got from dp[N - 3]
        So, dp[N - 4] = max(sum[N - 3] - dp[N - 3], dp[N - 3])

        This is why the final formula is dp[i] = max( dp[i + 1], prefix[i + 1] - dp[i + 1] )



        '''
        n = len(stones)
        #dp = [0] * n
        for i in range(1,n):
            stones[i] += stones[i-1]
        dp = stones[-1] # dp[n-2] when there are only two stones left, the current player must take thme all
       # print(dp,'---')
        for i in range(n-2, 0, -1): # i only runs to 1 -> dp stops at 0
            dp = max(dp, stones[i]-dp) # dp[i - 1] = max(dp[i], A[i] - dp[i]) 
            #print(i,dp) 
        return dp
        

        
if __name__ == "__main__":
    print(Solution().stoneGameVIII([-1,2,-3,4,-5]))
    print(Solution().stoneGameVIII([7,-6,5,10,5,-2,-6]))
    print(Solution().stoneGameVIII([1,2,3,4]))