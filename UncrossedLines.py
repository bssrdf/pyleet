'''
-Medium-
*DP*

You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.

We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:

nums1[i] == nums2[j], and
the line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).

Return the maximum number of connecting lines we can draw in this way.

 

Example 1:


Input: nums1 = [1,4,2], nums2 = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2.
Example 2:

Input: nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
Output: 3
Example 3:

Input: nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
Output: 2
 

Constraints:

1 <= nums1.length, nums2.length <= 500
1 <= nums1[i], nums2[j] <= 2000


'''

from typing import List

import heapq

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # greedy doesn't work 
        A, B, pq = nums1, nums2, []
        m, n = len(nums1), len(nums2)
        for i in range(m):
            for j in range(n):
                if A[i] == B[j]:
                    heapq.heappush(pq, (abs(i-j), i, j))
        ans = 0
        a, b = -1, -1
        while a < m and b < n and pq:
            d, i, j = heapq.heappop(pq)
            if i > a and j > b:
               ans += 1
               a = i
               b = j
        return ans 

    def maxUncrossedLines2(self, nums1: List[int], nums2: List[int]) -> int:
        A, B = nums1, nums2
        m, n = len(nums1), len(nums2)
        dp = [[0]*(n+1) for i in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], 
                              dp[i-1][j-1] + 1 if A[i-1] == B[j-1] else 0)
        return dp[m][n]
        

if __name__ == "__main__":
    nums1 = [1,4,2]; nums2 = [1,2,4]
    print(Solution().maxUncrossedLines2(nums1, nums2))
    nums1 = [2,5,1,2,5]; nums2 = [10,5,2,1,5,2]
    print(Solution().maxUncrossedLines2(nums1, nums2))
    nums1 = [1,3,7,1,7,5]; nums2 = [1,9,2,5,1]
    print(Solution().maxUncrossedLines2(nums1, nums2))
