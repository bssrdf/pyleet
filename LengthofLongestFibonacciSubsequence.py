'''
-Medium-

A sequence x1, x2, ..., xn is Fibonacci-like if:

n >= 3
xi + xi+1 == xi+2 for all i + 2 <= n
Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.

A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].

 

Example 1:

Input: arr = [1,2,3,4,5,6,7,8]
Output: 5
Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].
Example 2:

Input: arr = [1,3,7,11,12,14,18]
Output: 3
Explanation: The longest subsequence that is fibonacci-like: [1,11,12], [3,11,14] or [7,11,18].
 

Constraints:

3 <= arr.length <= 1000
1 <= arr[i] < arr[i + 1] <= 109


'''

from typing import List
from collections import Counter
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        dp = Counter()
        ans = 0
        dp[arr[0]] = 1
        dp[arr[1]] = 2
        for i,a in enumerate(arr):
            for j in range(i):
                b = a + arr[j]
                dp[b] = max(dp[b], dp[arr[j]]+2)


        
            # print(i, a, dp)
        return max(dp[a] for a in arr)

    def lenLongestFibSubseq2(self, arr: List[int]) -> int:
        A = arr
        dp = Counter()
        s = set(A)
        for j in range(len(A)):
            for i in range(j):
                if A[j] - A[i] < A[i] and A[j] - A[i] in s:
                    dp[A[i], A[j]] = dp.get((A[j] - A[i], A[i]), 2) + 1
        return max(dp.values() or [0])      
 

if __name__ == "__main__":
    print(Solution().lenLongestFibSubseq(arr = [1,2,3,4,5,6,7,8]))
    print(Solution().lenLongestFibSubseq(arr = [1,3,7,11,12,14,18]))
    print(Solution().lenLongestFibSubseq2(arr = [1,2,3,4,5,6,7,8]))
    print(Solution().lenLongestFibSubseq2(arr = [1,3,7,11,12,14,18]))
        
        