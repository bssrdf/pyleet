# -*- coding: utf-8 -*-
"""
Created on Thu Jul 06 22:08:37 2017

We are given two arrays ar1[0…m-1] and ar2[0..n-1] and a number x, 
we need to find the pair ar1[i] + ar2[j] such that absolute value 
of (ar1[i] + ar2[j] – x) is minimum.
@author: merli
"""
import sys

class Solution():
    def closestPair(self, l1, l2, x):
        i, j, dist = 0, 0, sys.maxint
        l3 = [x-n for n in l2][::-1]
        #print l3
        i1, j1 = 0, 0
        while i < len(l1) and j < len(l3):
            d = abs(l1[i]-l3[j])
            if d < dist:
                dist = d
                i1, j1 = i,j
            if l1[i] < l3[j]:
                i += 1
            else:
                j += 1
        #print i1, j1
        return [l1[i1], l2[len(l2)-(j1+1)]]
    
    
if __name__ == "__main__":
     ar1 = [ 1,  4,  5,  7]
     ar2 = [10, 20, 30, 40]
     print Solution().closestPair(ar1, ar2, 32)
     print Solution().closestPair(ar1, ar2, 50)