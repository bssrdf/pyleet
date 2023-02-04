'''
Say you have an array for which the i-th element is the price of a given 
stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k 
transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must 
sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), 
profit = 4-2 = 2.


Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), 
             profit = 3-0 = 3.


'''


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """


        '''
        Another way of using dynamic programming is to define dp[i,k] as the 
        largest profit we could make on day i with transaction k. Therefore 
        the transition function is:
           dp[i][k] = max(dp[i-1][k], price[i]-price[j]+dp[j-1][k-1] for j < i)
        With a small tweak of the function, instead of looking for 
        max(prices[i]-prices[j]+dp[j-1,k-1]), we can look for 
        max(dp[j-1,k-1]-prices[j], for j in [0,i-1]), so that we can store this value along with 
        the outer iteration

        '''
        if len(prices) < 2:
            return 0
        if k >= len(prices)//2:
            ret = 0
            for i in range(1,len(prices)):
                ret += max(0,prices[i]-prices[i-1])
            return ret
        dp = [[0 for _ in range(k+1)] for _ in range(len(prices))]         
        for kk in range(1,k+1):               
            tmpMax = -prices[0]
            for i in range(1,len(prices)):                            
                dp[i][kk] = max(dp[i-1][kk], prices[i]+tmpMax)
                tmpMax = max(tmpMax, dp[i-1][kk-1]-prices[i])

        return dp[-1][-1]



if __name__ == "__main__":
    s=Solution()
    print(s.maxProfit(2, [3,2,6,5,0,3]))