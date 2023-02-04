'''
-Medium-
*DP*
*Sliding Windows*

There are several cards arranged in a row, and each card has an associated number of points The 
points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to 
take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

 

Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost 
card first will maximize your total score. The optimal strategy is to take the three cards on 
the right, giving a final score of 1 + 6 + 5 = 12.
Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
Example 4:

Input: cardPoints = [1,1000,1], k = 1
Output: 1
Explanation: You cannot take the card in the middle. Your best score is 1. 
Example 5:

Input: cardPoints = [1,79,80,1,1,1,200,1], k = 3
Output: 202
 

Constraints:

1 <= cardPoints.length <= 10^5
1 <= cardPoints[i] <= 10^4
1 <= k <= cardPoints.length

'''

class Solution(object):
    def maxScoreTLE(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        memo = [[-1 for _ in range(n)] for j in range(n)]        
        def helper(l, r, steps):
            if steps == 0: return 0
            if r < l: return 0
            if memo[l][r] != -1:                  
                return memo[l][r]             
            memo[l][r]  = max(cardPoints[l]+helper(l+1,r,steps-1),
                              cardPoints[r]+helper(l,r-1,steps-1))
            return memo[l][r]
        # start from two ends at 0 and n-1 and intial steps k
        return helper(0, n-1, k)

    def maxScore(self, cardPoints, k):
        # Problem Translation: Find the smallest subarray sum of length len(cardPoints) - k
        n = len(cardPoints)
        size = n - k
        minSubArraySum = curr = sum(cardPoints[:size])
        
        for i in range(n - size):
            curr += cardPoints[size + i] - cardPoints[i]
            minSubArraySum = min(minSubArraySum, curr)
            
        return sum(cardPoints) - minSubArraySum    

if __name__ == "__main__":
    print(Solution().maxScore(cardPoints = [1,2,3,4,5,6,1], k = 3))
    print(Solution().maxScore(cardPoints = [2,2,2], k = 2))
    print(Solution().maxScore(cardPoints = [9,7,7,9,7,7,9], k = 7))
    print(Solution().maxScore(cardPoints = [1,1000,1], k = 1))
    print(Solution().maxScore(cardPoints = [1,79,80,1,1,1,200,1], k = 3))