'''
Given an array A of integers, return the number of (contiguous, 
non-empty) subarrays that have a sum divisible by K.

 

Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], 
[-2, -3]
 

Note:

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000

'''
from collections import defaultdict

class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        m = defaultdict(int)
        n = len(A)
        S = [0]*(n+1)
        ans = 0        
        for i,num in enumerate(A):
            S[i+1] = S[i]+num             
        m[S[0]]+=1
        for s in S[1:]:
            t = s%K
            if t in m:
                ans += m[t]
            m[t] += 1
        return ans

if __name__ == "__main__":
    print(Solution().subarraysDivByK([4,5,0,-2,-3,1], 5))