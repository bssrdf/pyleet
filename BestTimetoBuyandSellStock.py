# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 22:50:19 2018

@author: merli
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        profit,buyprice=(0, prices[0])
        for p in prices:
            profit = max(profit, p-buyprice)
            buyprice = min(buyprice, p)
        return profit
    
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        
        The transition relation is constructed by the following four equations. 
        Actually, sell2 is the only state we record for iterations. The others are 
        intermediate states.

         buy1 and *sell1 *are for the first transaction

         Transition relation:

         buy1[i] = max( - prices[i], buy1[i - 1])
         sell1[i] = max(buy1[i - 1] + price[i], sell1[i - 1])
         
        
        """
        if len(prices) <= 1: return 0
        sell1=0
        buy1=-sys.maxsize
        for p in prices:
            buy1 = max(buy1, -p)
            sell1 = max(sell1, p+buy1)
        return sell1

if __name__ == "__main__":
    s=Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([7,6,4,3,1]))
    print(s.maxProfit1([7,1,5,3,6,4]))
    print(s.maxProfit1([7,6,4,3,1]))