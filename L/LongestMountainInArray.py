'''
-Medium-
*Array*
*Two Pointers*

Let's call any (contiguous) subarray B (of A) a mountain if the following 
properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] 
< B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000
Follow up:

Can you solve it using only one pass?
Can you solve it in O(1) space?

'''

class Solution(object):
    def longestMountainTLE(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        """
        although this solution is more clear, but can not pass AC (TLE) 

        """
        if not A: return 0        
        res, n = 0, len(A)
        for i in range(n):
            j = i
            while j+1 < n and A[j+1] > A[j]:
                j += 1
            k = j
            while k+1 < n and A[k+1] < A[k]:
                k += 1
            if j > i and k > j:  
                res = max(res, k-i+1)
        return res


    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A: return 0
        l, peak, r = 0, 0, 1
        res, n = 0, len(A)
        while r < n :
            if A[r] > A[r-1]:
                if l < peak < r-1:
                    res = max(res, r-l)                    
                if peak < r-1:    
                    l = r-1
                peak = r                                    
            elif A[r] == A[r-1]:  
                if l < peak < r-1:                          
                    res = max(res, r-l)
                if peak <= r-1:                    
                    l = r
                    peak = l  
            r += 1    
        if l < peak < r-1:
            res = max(res, r-l)
        return res



if __name__ == "__main__":
    print(Solution().longestMountain([2,1,4,7,3,2,5]))
    print(Solution().longestMountain([2,2,2,1]))
    print(Solution().longestMountain([1,2,4,10,7,4,2]))
    print(Solution().longestMountainTLE([2,1,4,7,3,2,5]))
    print(Solution().longestMountainTLE([2,2,2,1]))
    print(Solution().longestMountainTLE([1,2,4,10,7,4,2]))
    mount = [i for i in range(9999, -1, -1)]
    print(Solution().longestMountain(mount))
    print(Solution().longestMountainTLE(mount))