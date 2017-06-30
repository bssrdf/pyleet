# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 22:57:10 2017

@author: merli
"""

class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        res, curMin, curMax = 0, 10000, -10000
        for arr in arrays:
            res = max(res, arr[-1]-curMin, curMax-arr[0])
            print res, arr[-1]-curMin, curMax-arr[0]
            curMin, curMax = min(curMin, arr[0]), max(curMax, arr[-1])
            print curMin, curMax
        return res            
        
if __name__=="__main__":
    nms = [
    [1,2,3],
    [0,5],
    [1,2,3]
    ]
    print Solution().maxDistance(nms)