# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 21:49:23 2017

@author: merli
"""
import math

class Solution(object):
    
    def getSumUtil(self, st, ss, se, qs, qe, si):
        if qs <= ss and se <= qe:
            return st[si]
        elif qe<ss or se<qs:
            return 0
        else:
            mid = ss + (se-ss)/2
            return self.getSumUtil(st, ss, mid, qs, qe, 2*si+1) + self.getSumUtil(st, mid+1, se, qs, qe, 2*si+2)    
            
    def getSum(self, st, n, qs, qe):
        
        return self.getSumUtil(st, 0, n-1, qs, qe, 0)
    
    def constructSTUtil(self, nums, ss, se, st, si):
        if ss == se:
            st[si] = nums[ss]
            return nums[ss]
        mid = ss + (se - ss)/2
        st[si] = self.constructSTUtil(nums, ss, mid, st, 2*si+1) + self.constructSTUtil(nums, mid+1, se, st, 2*si+2) 
        return st[si]          
        
    def constructSegTree(self, nums):
        n = len(nums)
        x = int(math.ceil(math.log(n, 2)))
        max_size = 2*int(math.pow(2,x))-1
        st = [0]*max_size
        self.constructSTUtil(nums, 0, n-1, st, 0)
        #print n, x, max_size
        #print st
        return st
        
    def sumOfRange(self, nums, m, n):        
        st = self.constructSegTree(nums)
        return self.getSum(st, len(nums), m, n)
        
        
if __name__ == "__main__":
   print Solution().sumOfRange([3, 1, 7, 8, 5, 10, 2], 2, 5)   
   # Solution().sumOfRange([3, 1, 7, 8, 5, 10, 2], 2, 5)             