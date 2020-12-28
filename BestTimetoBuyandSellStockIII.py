# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 22:29:11 2018
Say you have an array for which the ith element is the price of a given stock 
on day i.

Design an algorithm to find the maximum profit. You may complete at most two 
transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you 
must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), 
profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), 
             profit = 4-1 = 3.
             
@author: merli
"""
import sys

class Solution(object):

    def maxProfitDpPattern(self, prices):
        """
        :type prices: List[int]
        :rtype: int      
        """
        if len(prices) <= 1: return 0
        K, n = 2, len(prices)
        dp = [[[0]*2 for _ in range(K+1)] for _ in range(len(prices))]        
        for i in range(n):
           for k in range(K, 0, -1):            
               if i-1 == -1:
                    # i = 0 
                    # 解释：
                    # dp[i][k][0] 
                    # = max(dp[-1][k][0], dp[-1][k][1] + prices[i])
                    # = max(0, -infinity + prices[i]) = 0
                    dp[i][k][0] = 0
                    #解释：
                    #  dp[i][k][1] 
                    # = max(dp[-1][k][1], dp[-1][k][0] - prices[i])
                    # = max(-infinity, 0 - prices[i]) 
                    # = -prices[i]
                    dp[i][k][1] = -prices[0]
                    continue
               dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i])
               dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i])
             
        return dp[n-1][K][0]
    
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        f[k, ii] represents the max profit up until prices[ii] (Note: NOT 
        ending with prices[ii]) using at most k transactions. 
        f[k, ii] = max(f[k, ii-1], prices[ii] - prices[jj] + f[k-1, jj]) { jj in range of [0, ii-1] }
                 = max(f[k, ii-1], prices[ii] + max(f[k-1, jj] - prices[jj]))
        f[0, ii] = 0; 0 times transation makes 0 profit
        f[k, 0] = 0; if there is only one price data point you can't make any money no matter how many times you can trade
        
        """
        if len(prices) <= 1: return 0
        K = 2
        maxProf = 0
        f = [[0]*len(prices) for _ in range(K+1)]        
        for kk in range(1, K+1):
           tmpMax = f[kk-1][0] - prices[0] 
           for ii in range(1,len(prices)):
             f[kk][ii] = max(f[kk][ii-1], prices[ii]+tmpMax)
             tmpMax = max(tmpMax, f[kk-1][ii]-prices[ii])
             maxProf = max(maxProf, f[kk][ii])          
        return maxProf
    
    def maxProfitO1Space(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        
        The transition relation is constructed by the following four equations. 
        Actually, sell2 is the only state we record for iterations. The others 
        are intermediate states.

         buy1 and *sell1 *are for the first transaction. buy2 and *sell2 *are 
         for the second transaction.

         Transition relation:

         buy1[i] = max( - prices[i], buy1[i - 1])
         sell1[i] = max(buy1[i - 1] + price[i], sell1[i - 1])
         buy2[i] = max( sell1[i -1] - prices[i], buy2[i - 1])
         sell2[i] = max(buy2[i - 1] + price[i], sell2[i - 1])
        
        """
        if len(prices) <= 1: return 0
        sell1,sell2=0,0
        buy1,buy2 = -sys.maxsize, -sys.maxsize
        for p in prices:
            buy1 = max(buy1, -p)
            sell1 = max(sell1, p+buy1)
            buy2 = max(buy2, sell1-p)
            sell2 = max(sell2, p+buy2)
        return sell2
        
if __name__ == "__main__":
    s=Solution()
    print(s.maxProfit([3,3,5,0,0,3,1,4]))
    print(s.maxProfit([1,2,3,4,5]))
    print(s.maxProfit([7,6,4,3,1]))
    print(s.maxProfitDpPattern([3,3,5,0,0,3,1,4]))
    print(s.maxProfitDpPattern([1,2,3,4,5]))
    print(s.maxProfitDpPattern([7,6,4,3,1]))
    print(s.maxProfitO1Space([3,3,5,0,0,3,1,4]))
    print(s.maxProfitO1Space([1,2,3,4,5]))
    print(s.maxProfitO1Space([7,6,4,3,1]))