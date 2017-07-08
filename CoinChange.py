# -*- coding: utf-8 -*-
"""
Created on Tue Jul 04 20:52:33 2017

@author: merli
"""
import sys

class Solution:
    
    def dpMakeChange(self, coinValueList, change):
        minCoins = [0]*(change+1)
        coinsUsed = [0]*(change+1)
        for cents in range(change+1):
            coinCount = cents
            for j in [c for c in coinValueList if c <= cents]:
                if minCoins[cents-j] + 1 < coinCount:
                    coinCount = minCoins[cents-j]+1
                    coinsUsed[cents] = j 
            minCoins[cents] = coinCount
        coinCur = coinsUsed[change]        
        allCoins = [coinCur] 
        changeLeft = change - coinCur
        while changeLeft > 0:            
            coinCur = coinsUsed[changeLeft]
            allCoins.append(coinCur)
            changeLeft -= coinCur                                                        
        print allCoins[::-1] 
        return minCoins[change]
        
    def dpMakeChangeTopDown(self, coinValueList, change):
        minCoins = [-1]*(change+1)
        q = self.helper(coinValueList, change, minCoins)        
        print minCoins
        return q
        
    def helper(self, cList, ch, mins):
        if mins[ch] >= 0:
            return mins[ch]
        if ch == 0:
            q = 0
        else:
            q = sys.maxint
            for j in [c for c in cList if c <= ch]:
                q = min(q, 1+self.helper(cList, ch-j, mins))
        mins[ch] = q        
        return q
        
if __name__ == "__main__":    
    print Solution().dpMakeChange([1, 5, 10, 25], 63)
    print Solution().dpMakeChangeTopDown([1, 5, 10, 25], 63)