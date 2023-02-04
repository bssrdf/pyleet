'''

-Medium-

*Probability*
*DP*

You have some coins. The i-th coin has a probability prob[i] of facing heads when tossed.

Return the probability that the number of coins facing heads equals target if you 
toss every coin exactly once.

Example 1:

Input: prob = [0.4], target = 1

Output: 0.40000

Example 2:

Input: prob = [0.5,0.5,0.5,0.5,0.5], target = 0

Output: 0.03125

Constraints:

1 <= prob.length <= 1000
0 <= prob[i] <= 1
0 <= target <= prob.length
Answers will be accepted as correct if they are within 10^-5 of the correct


'''

from typing import List

class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        # Use dynamic programming. Let length be the length of array prob, 
        # and it can be seen that length equals the number of coins.

        # Create a 2D array dp with length + 1 rows and target + 1 columns. 
        # The element at dp[i][j] stands for the probability that after the 
        # first i coins are tossed, there are j coins facing heads.

        # Obviously, if no coin is tossed, then definitely no coin faces heads, 
        # which has a probability 1, so dp[0][0] = 1. Each time a coin is tossed, 
        # the number of coins facing heads either remains the same or increase by 1, 
        # depending on the current coin’s probability of facing heads. So 
        # the probability can be calculated. For the case j equals 0, 
        # dp[i][0] only depends on prob[i - 1] and dp[i - 1][0]. For 
        # other cases, dp[i][j] depends on prob[i - 1], dp[i - 1][j - 1] and dp[i - 1][j].

        # Finally, return dp[length][target] for the result.

        n = len(prob)
        dp = [[0]*(target+1) for _ in range(n+1)]
        dp[0][0] = 1.0 # if no coin is tossed, then definitely no coin faces heads, 
                       # which has a probability 1
        for i in range(1, n+1):
            curProb = prob[i-1]
            dp[i][0] = dp[i-1][0] * (1.0 - curProb)
            for j in range(1, target+1):
                dp[i][j] = curProb*dp[i-1][j-1] + (1.0-curProb)*dp[i-1][j]
        return dp[n][target]



if __name__ == "__main__":
    print(Solution().probabilityOfHeads(prob = [0.5,0.5,0.5,0.5,0.5], target = 0))