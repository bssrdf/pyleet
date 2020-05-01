"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one
LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""
import bisect

__author__ = 'Daniel'


class Solution(object):    
    
    
    def bisect_diy(self, L, a):
        #l = -1
        l = 0
        r = len(L)
    #    print l, r
        #while r-l > 1:
        while l<r:
            m = l+(r-l)//2
            if L[m] >= a:
                r = m
            else:
                #l = m
                l = m+1
#            print l, r, m
        return r  
    
    def bisect_diynew(self, L, a):        
        l = 0
        r = len(L)-1
  
        while l<=r:
            m = l+(r-l)//2
            if L[m] > a:
                r = m-1
            elif L[m] < a:                
                l = m+1
            else:
                return m
       # print(l, r, m)
        return l
    
    def binary_search(self, L, a):        
        l = 0
        r = len(L)-1
  
        while l<=r:
            m = l+(r-l)//2
            if L[m] > a:
                r = m-1
            elif L[m] < a:                
                l = m+1
            else:
                return m
       # print(l, r, m)
        return -1
    
    def binary_search_pos(self, L, a):        
        l = 0
        r = len(L)
  
        while l != r:
            m = l+(r-l)//2
            if L[m] < a:
                l = m+1
            else:
                r = m
        return l
       # print(l, r, m)
        
    
            

import sys
if __name__ == "__main__":
    L = [2, 4, 6, 9, 11, 15]
    #a = sys.argv[1]
    A = [0, 3, 5, 8, 9, 12, 15, 20]
    #print Solution().binary_search_corr(L, a)
    #print bisect.bisect_left(L, a)   
    print(bisect.bisect_left(L, 9))
    print(bisect.bisect(L, 9))

    #for a in A:
        #assert Solution().bisect_diynew(L, a) == bisect.bisect_left(L, a)   
        #assert Solution().binary_search_pos(L, a) == bisect.bisect_left(L, a)   
     #   assert Solution().binary_search_pos(L, a) == bisect.bisect(L, a)   
    #for a in A:
      #  print(Solution().binary_search(L, a))
   # print(Solution().binary_search_pos(L, 10))
