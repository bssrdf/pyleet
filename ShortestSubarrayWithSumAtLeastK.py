'''
-Hard-
*Monotonic Queue*
*Deque*

Return the length of the shortest, non-empty, contiguous subarray of A 
with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.

 

Example 1:

Input: A = [1], K = 1
Output: 1
Example 2:

Input: A = [1,2], K = 4
Output: -1
Example 3:

Input: A = [2,-1,2], K = 3
Output: 3
 

Note:

1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9

'''
from collections import deque

class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = len(A)
        q = deque()
        preSum = [0]*(n+1)
        res = n+1
        for i in range(1, n+1):
            preSum[i] = preSum[i-1] + A[i-1]
        for i in range(n+1):
            while q and preSum[i]-preSum[q[0]] >= K:
                res = min(res, i-q[0])
                q.popleft()
            while q and preSum[i] <= preSum[q[-1]]:                
                q.pop()
            q.append(i)
        return -1 if res == n+1 else res


if __name__ == "__main__":
    print(Solution().shortestSubarray([2,-1,2], 3))