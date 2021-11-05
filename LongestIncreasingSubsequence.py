"""
Given an unsorted array of integers, find the length of longest increasing 
subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. 
Note that there may be more than one LIS combination, it is only necessary 
for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""
import bisect

__author__ = 'Daniel'


class Solution(object):    
    
    def binary_search_corr(self, L, a):
        l = -1
        r = len(L)
        print(l, r)
        while r-l > 1:
            m = l+(r-l)/2
            if L[m] >= a:
                r = m
            else:
                l = m
            print(l, r, m)
        return r        
        
        
    def lengthOfLIS_nlogn(self, A):
        if not A:
            return 0         
        def bisect_diy(l, r, a):    
            while l<r:
                m = l+(r-l)//2
                if A[bis[m]] >= a:
                    r = m
                else:
                    l = m+1
            return r  
        # bis[k] : the index the best increasing sequence of length k ends at            
        # k = 0, ll-1
        bis=[0]*len(A)        
        prev = [-1]*len(A)
        ll = 1 # length of LIS, which is 1 initially for len(A)=1
        for i in range(1, len(A)):       
            if A[i] < A[bis[0]]:
                bis[0] = i # new smallest value
            elif A[i] > A[bis[ll-1]]: # A[i] can extend the LIS found so far
                prev[i] = bis[ll-1]
                bis[ll] = i # after the extension the longest IS ends at i  
                ll +=1 # after the extension the longest length is ll  
            else:                                
                j = bisect_diy(0, ll, A[i]) # find a location j in [0, ll)  
                prev[i] = bis[j-1]   # such that A[bis[j-1]] < A[i] < A[bis[j]]
                bis[j] = i  # replace bis[j] with i, indicating we have found a
                            # better bis[j] ending with A[i]                           
        #for i in bis[:ll]:
        #    print(A[i])
        #print('******************************')
        #print(prev)
        #print('******************************')
        i = bis[ll-1]
        while i>=0:
        #    print(i, A[i])
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
            # starting from index i, traverse back until index 0,
            # if A[i] > any given number A[j], we have a potential 
            # new LIS with length F[j]+1, update F[i] and the result
            for j in range(i):
                if A[i] > A[j] and F[i] < 1+F[j]:
                    F[i] = 1+F[j]
            maxa = max(maxa, F[i])
        print(F)
        return maxa     

    def lengthOfLIS_nlogn2(self, nums):
        lis = []
        for i, x in enumerate(nums):
            if len(lis) == 0 or lis[-1] < x:  # Append to LIS if new element is >= last element in LIS
                lis.append(x)
            elif x < lis[0]:
                lis[0] = x
            else:
                idx = bisect.bisect_left(lis, x)  # Find the index of the smallest number > x
                if idx < len(lis):
                    lis[idx] = x  # Replace that number with x                
        return len(lis)

if __name__ == "__main__":
    #assert Solution().lengthOfLIS_dp([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    #print(Solution().lengthOfLIS_dp([5, 10, 4, 4, 3, 8, 9]))
    print(Solution().lengthOfLIS_nlogn([5, 10, 6, 4, 3, 8, 9]))
    print(Solution().lengthOfLIS_nlogn2([5, 10, 6, 4, 3, 8, 9]))
    print(Solution().lengthOfLIS_nlogn([0,1,0,3,2,3]))
    print(Solution().lengthOfLIS_nlogn2([0,1,0,3,2,3]))
    print(Solution().lengthOfLIS_nlogn([7,7,7,7,7,7,7]))
    print(Solution().lengthOfLIS_nlogn2([7,7,7,7,7,7,7]))
    assert Solution().lengthOfLIS_nlogn([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert Solution().lengthOfLIS_nlogn2([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    print(Solution().lengthOfLIS_nlogn([4,10,4,3,8,9]))
    print(Solution().lengthOfLIS_nlogn2([4,10,4,3,8,9]))
    #assert
    #  Solution().lengthOfLIS_nlogn([0, 8, 4, 12, 2, 10, 6, 14,
    #                                     1, 9, 5, 13, 3, 11, 7, 15]) == 6
    #assert Solution().lengthOfLIS_dp([2, 4, 6, 8, 10, 1]) == 5    
    #assert Solution().lengthOfLIS_nlogn([2, 4, 6, 8, 10, 1]) == 5    
    L = [2, 4, 6, 9, 11, 15]
    a = 8
    #print Solution().binary_search_corr(L, a)
    #print bisect.bisect_left(L, a)   