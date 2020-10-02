'''
In an array A of 0s and 1s, how many non-empty subarrays have sum S?

 

Example 1:

Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation: 
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Note:

A.length <= 30000
0 <= S <= A.length
A[i] is either 0 or 1.

'''
import collections

class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        c = collections.Counter({0: 1})
        psum = res = 0
        for i in A:
            psum += i
            # c[psum-S] is the # of subarrays with sum = psum-S
            # but starting from the index just after these subarrays, 
            # the sum will accumulate to S at i. So c[psum-S] is exactly 
            # what we need.  
            # another way of thinking: using prefix sum 
            # sum(i,j) = psum_i - psum_j (j < i)
            # let sum(i,j) = S, psum_j = psum_i - S
            # we know the # of occurances of psum_j which is c[psum_j]
            # that's the same as the # of subarrays A[j...i] which sums to S 
            psum_j = psum - S 
            res += c[psum_j]
            c[psum] += 1
            print(i, res,  psum, c)
        return res

if __name__ == "__main__":
    #print(Solution().numSubarraysWithSum([1,0,1,0,1],2))
    print(Solution().numSubarraysWithSum([1,0,1,0,0,1,0,1,0,0,1,1],2))