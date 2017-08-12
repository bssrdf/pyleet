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
    
    
    def binary_search_corr(self, L, a):
        #l = -1
        l = 0
        r = len(L)
    #    print l, r
        #while r-l > 1:
        while l<r:
            m = l+(r-l)/2
            if L[m] >= a:
                r = m
            else:
                #l = m
                l = m+1
#            print l, r, m
        return r        
            

import sys
if __name__ == "__main__":
    L = [2, 4, 6, 9, 11, 15]
    #a = sys.argv[1]
    A = [0, 3, 5, 8, 9, 12, 15, 20]
    #print Solution().binary_search_corr(L, a)
    #print bisect.bisect_left(L, a)   
    for a in A:
        assert Solution().binary_search_corr(L, a) == bisect.bisect_left(L, a)   
