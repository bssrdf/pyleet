'''
-Medium-
*Array*
*Two Pointers*

Let's call any (contiguous) subarray B (of A) a valley if the following 
properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] > B[1] > ... B[i-1] 
> B[i] < B[i+1] < ... < B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest valley. 

Return 0 if there is no valley.

Example 1:
Input: [4,3,2,5,3,1,4,8]
Output:    5    
Explanation: The largest valley is [5,3,1,4,8] which has length 5

Input: [2,2,2]
Output: 0
Explanation: There is no valley.
Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000
Follow up:

Can you solve it using only one pass?
Can you solve it in O(1) space?

'''

class Solution(object):

    def longestValley(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3: return 0
        l, trough, r = 0, 0, 1
        res, n = 0, len(A)
        while r < n :
            if A[r] < A[r-1]:
                if l < trough < r-1:
                    res = max(res, r-l)                    
                if trough < r-1:    
                    l = r-1
                trough = r                                    
            elif A[r] == A[r-1]:  
                if l < trough < r-1:                          
                    res = max(res, r-l)
                if trough <= r-1:                    
                    l = r
                    trough = l  
            r += 1    
        if l < trough < r-1:
            res = max(res, r-l)
        return res



if __name__ == "__main__":
    print(Solution().longestValley([4,3,2,5,3,1,4,8]))
    print(Solution().longestValley([2,2,2,1]))
    
