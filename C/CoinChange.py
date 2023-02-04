# -*- coding: utf-8 -*-
"""

-Medium-
*DP*

You are given coins of different denominations and a total amount of money 
amount. Write a function to compute the fewest number of coins that you 
need to make up that amount. If that amount of money cannot be made up 
by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
Example 4:

Input: coins = [1], amount = 1
Output: 1
Example 5:

Input: coins = [1], amount = 2
Output: 2
 

Constraints:


1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4

"""
import sys

class Solution:
    
    def dpMakeChange(self, coins, amount):
        minCoins = [amount+1]*(amount+1)                
        minCoins[0] = 0
        
        # the order can be switched like below. Either works

        #for cents in range(1,amount+1):           
        #    for j in [c for c in coins if c <= cents]:
        #        minCoins[cents] = min(minCoins[cents], 1+minCoins[cents-j])       
        for j in coins:
            for cents in range(1,amount+1):           
                if j <= cents:
                    minCoins[cents] = min(minCoins[cents], 1+minCoins[cents-j])           
        return -1 if minCoins[amount] > amount else minCoins[amount]
        
    def dpMakeChangeTopDown(self, coins, amount):
        minCoins = [-1]*(amount+1)
        '''
        The recursion function helper computes the minimum amount 
        of coins need to make 'change' money. minCoins array is used for 
        the memoization
        '''
        q = self.helper(coins, amount, minCoins)        
        #print(minCoins)
        return -1 if q == sys.maxsize else q
        
    def helper(self, cList, ch, mins):
        #print(ch,mins)
        if mins[ch] >= 0:
            return mins[ch]
        if ch == 0:
            q = 0
        else:
            q = sys.maxsize
            # take every coin valued at j from the list, 
            # use helper to compute the min. amound need to make change-j money
            # return the result by plus 1
            for j in [c for c in cList if c <= ch]:
                q = min(q, 1+self.helper(cList, ch-j, mins))
        mins[ch] = q        
        return q
        
if __name__ == "__main__":    
    #print(Solution().dpMakeChangeTopDown([1, 2, 5], 11))
    print(Solution().dpMakeChange([2], 3))
    print(Solution().dpMakeChange([1,2,5], 11))
    #print(Solution().dpMakeChangeTopDown([1, 5, 10, 25], 63))