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
        l = -1
        r = len(L)
        print l, r
        while r-l > 1:
            m = l+(r-l)/2
            if L[m] >= a:
                r = m
            else:
                l = m
            print l, r, m
        return r        
        
        
    def lengthOfLIS_nlogn(self, A):
        if not A:
            return 0         
            
        def binary_search(L, T, l, r, a):
        
            while r-l > 1:
                m = l+(r-l)/2
                if L[T[m]] >= a:
                    r = m
                else:
                    l = m                
            return r         
                    
        bis=[0]*len(A)        
        prev = [-1]*len(A)
        ll = 1
        for i in range(1, len(A)):       

                #ind = binary_search(bis, a)
            if A[i] < A[bis[0]]:
                bis[0] = i # new smallest value
            elif A[i] > A[bis[ll-1]]:
                prev[i] = bis[ll-1]
                bis[ll] = i
                ll +=1
            else:                
                ind = binary_search(A, bis, -1, ll, A[i])            
                prev[i] = bis[ind-1]
                bis[ind] = i
        for i in bis[:ll]:
            print A[i]
        print '******************************'
        print prev
        print '******************************'
        i = bis[ll-1]
        while i>=0:
            print A[i]
            i = prev[i]
                
           # print a, ind, bis
        #print bis
        return ll
                    
            

    def lengthOfLIS_dp(self, A):
        """
        dp

        let F[i] be the LIS length ends at A[i]
        F[i] = max(F[j]+1 for all j < i if A[i] > A[j])

        avoid max() arg is an empty sequence

        O(n^2)
        :type nums: List[int]
        :rtype: int
        """
        if not A:
            return 0
        F=[1]*len(A)        
        maxa = 1
        for i in range(1, len(A)):
            for j in range(i):
                if A[i] > A[j] and F[i] < 1+F[j]:
                    F[i] = 1+F[j]
                #else:
                 #   F[i] = 1
            maxa = max(maxa, F[i])
        #print F
        return maxa       

if __name__ == "__main__":
    #assert Solution().lengthOfLIS_dp([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    #assert Solution().lengthOfLIS_nlogn([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert Solution().lengthOfLIS_nlogn([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6
    #assert Solution().lengthOfLIS_dp([2, 4, 6, 8, 10, 1]) == 5    
    #assert Solution().lengthOfLIS_nlogn([2, 4, 6, 8, 10, 1]) == 5    
    L = [2, 4, 6, 9, 11, 15]
    a = 8
    #print Solution().binary_search_corr(L, a)
    #print bisect.bisect_left(L, a)   