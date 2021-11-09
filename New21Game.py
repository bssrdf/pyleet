'''

-Medium-

Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points and draws numbers while she has less than k points. 
During each draw, she gains an integer number of points randomly from 
the range [1, maxPts], where maxPts is an integer. Each draw is independent 
and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets k or more points.

Return the probability that Alice has n or fewer points.

Answers within 10-5 of the actual answer are considered accepted.

 

Example 1:

Input: n = 10, k = 1, maxPts = 10
Output: 1.00000
Explanation: Alice gets a single card, then stops.
Example 2:

Input: n = 6, k = 1, maxPts = 10
Output: 0.60000
Explanation: Alice gets a single card, then stops.
In 6 out of 10 possibilities, she is at or below 6 points.
Example 3:

Input: n = 21, k = 17, maxPts = 10
Output: 0.73278
 

Constraints:

0 <= k <= n <= 10^4
1 <= maxPts <= 10^4

'''

class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        

        # When the game ends, the point is between K and K-1+W
        # What is the probability that the the point is less than N?
        # - If N is greater than K-1+W, probability is 1
        # - If N is less than K, probability is 0
        
        # If W == 3 and we want to find the probability to get a 5
        # - You can get a card with value 1, 2, or 3 with equal probability (1/3)
        # - If you had a 4 and you get a 1: prob(4) * (1/3)
        # - If you had a 3 and you get a 2: prob(3) * (1/3)
        # - If you had a 2 and you get a 3: prob(2) * (1/3)
        # - If you had a 1, you can never reach a 5 in the next draw
        # - prob(5) = prob(4) / 3 + prob(3) / 3 + prob(2) /3
        
        # To generalize:
        # The probability to get point K is
        # p(K) = p(K-1) / W + p(K-2) / W + p(K-3) / W + ... p(K-W) / W
        
        # let wsum = p(K-1) + p(K-2) + ... + p(K-W)
        # p(K) = wsum / W
        
        # dp is storing p(i) for i in [0 ... N]
        # - We need to maintain the window by
        # adding the new p(i), 
        # and getting rid of the old p(i-w)
        # - check i >= W because we would not have negative points before drawing a card
        # For example, we can never get a point of 5 if we drew a card with a value of 6
        # - check i < K because we cannot continue the game after reaching K
        # For example, if K = 21 and W = 10, the eventual point is between 21 and 30
        # To get a point of 27, we can have:
        # - a 20 point with a 7
        # - a 19 point with a 8
        # - a 18 point with a 9
        # - a 17 point with a 10
        # - but cannot have 21 with a 6 or 22 with a 5 because the game already ends

        if K == 0 or N >= K + W: return 1
        dp = [1.0] + [0.0] * N
        Wsum = 1.0
        for i in range(1, N + 1):
            dp[i] = Wsum / W
            if i < K: Wsum += dp[i]
            if i - W >= 0: Wsum -= dp[i - W]
        return sum(dp[K:])
        

if __name__ == "__main__":
    print(Solution().new21Game(10, 1, 10))