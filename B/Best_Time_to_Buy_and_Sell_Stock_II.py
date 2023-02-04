class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0        
        profit, buyprice=(0, prices[0])
        max_profit = 0
        prev = prices[0]
        for p in prices[1:]:
            profit = max(profit, p - buyprice)
            if p < prev:
                max_profit += profit
                buyprice = p
                profit   = 0 
            prev = p
        #    print p, buyprice
        max_profit += profit
        return max_profit 

if __name__ == "__main__":
  s = Solution()
  print s.maxProfit([7,1,5,3,6,4]) 
  print s.maxProfit([1,2, 3, 4, 5]) 
