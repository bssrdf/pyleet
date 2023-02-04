'''
-Medium-


Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many 
transactions as you like (ie, buy one and sell one share of the stock multiple times) 
with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the 
stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]



'''
import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        On any i-th day, we can buy, sell or cooldown

        buy[i]: The maximum profit can be made if the first i days end with buy or wait. 
        E.g "buy, sell, buy" or "buy, cooldown, cooldown"
        sell[i]: The maximum profit can be made if the first i days end with sell or wait. 
        E.g "buy, sell, buy, sell" or "buy, sell, cooldown, cooldown"
        price: prices[i - 1], which is the stock price of the i-th day

        To calculate sell[i]:
        If we sell on the i-th day, the maximum profit is buy[i - 1] + price, because we 
        have to buy before we can sell.
        If we cooldown on the i-th day, the maximum profit is same as sell[i - 1] since 
        we did not do anything on the i-th day.
        So sell[i] is the larger one of (buy[i - 1] + price, sell[i - 1])

        To calculate buy[i]:
        If we buy on the i-th day, the maximum profit is sell[i - 2] - price, because 
        on the (i-1)th day we can only cooldown.
        If we cooldown on the i-th day, the maximum profit is same as buy[i - 1] since 
        we did not do anything on the i-th day.
        So buy[i] is the larger one of (sell[i - 2] - price, buy[i - 1])
        """

        if not prices or len(prices) < 1:
            return 0
        n = len(prices)
        buy = [0] * (n+1)
        sell = [0] *(n+1)
        buy[1] = -prices[0] # first day is buy, profit is -prices[0]
                            # first day can not sell, profit is 0
        for i in range(2, n+1):
            price = prices[i-1]
            buy[i] = max(sell[i-2]-price, buy[i-1])
            sell[i] = max(buy[i-1]+price, sell[i-1])
        return sell[n]

    def maxProfitFramework(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
        """
        n = len(prices)
        dp_i_0, dp_i_1 = 0, -sys.maxsize
        dp_pre_0 = 0 # 代表 dp[i-2][0]
        for i in range(n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
            dp_pre_0 = temp
        return dp_i_0



if __name__ == "__main__":
    s=Solution()
    print(s.maxProfit([1,2,3,0,2]))
    print(s.maxProfitFramework([1,2,3,0,2]))
    

        