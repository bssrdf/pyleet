# -*- coding: utf-8 -*-
"""
Created on Tue Jul 04 20:52:33 2017

@author: merli
"""

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
        
if __name__ == "__main__":
    #print Solution().threeSum([-1, 0, 1, 2, 3, -4])
    print Solution().dpMakeChange([1, 5, 10, 25], 63)