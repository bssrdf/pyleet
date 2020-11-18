'''
You are given coins of different denominations and a total amount of money. 
Write a function to compute the number of combinations that make up that amount. 
You may assume that you have infinite number of each kind of coin.

 

Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10] 
Output: 1
 

Note:

You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer

'''

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0]*(amount+1)                
        dp[0] = 1        
        # the order of the loop must be as below:
        for c in coins:
            for cents in range(1,amount+1):           
                if c <= cents:
                   dp[cents] += dp[cents-c]                              
        return dp[amount]

    def change2dDP(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [[0]*(amount+1) for i in range(len(coins)+1)]
        dp[0][0] = 0
        for i in range(len(coins)+1):
            dp[i][0] = 1
            for cents in range(1,amount+1):   
                # dp[i][cents]: the number of ways taking ith coin and giving 
                # amount of cents should equal:
                # dp[i-1][cents]: the number of ways taking (i-1)th coin and giving 
                # the same amount                           
                # plus
                # dp[i][cents-coins[i]]: the number of ways taking ith coin and giving 
                # amount of cents-coins[i]                           
                dp[i][cents] = dp[i-1][cents] +  \
                               dp[i][cents-coins[i]] if coins[i]<=cents else 0                             
        return dp[len(coins)][amount]
    
    
    def changeTopdown(self, amount, coins):
        m = {}
        def ways(amount, coins, i):
            if (amount,i) in m:
                return m[(amount,i)]
            
            if amount == 0: 
                return 1 

            if amount < 0 or len(coins) == 0:
                return 0 

            m[(amount,i)] = ways(amount - coins[-1], coins, i) + ways(amount, coins[:-1], i-1)
            return m[(amount,i)]
        
        return ways(amount, coins, len(coins)-1)

        

if __name__ == "__main__":        
    print(Solution().change(5, [1,2,5]))
    
    print(Solution().change(3, [2]))
    print(Solution().change(10, [10]))
    print(Solution().change(5, [1,2,5]))
    print(Solution().changeTopdown(5, [1,2,5]))
    #print(Solution().changeTopdown(3, [2]))
    #print(Solution().changeTopdown(10, [10]))
