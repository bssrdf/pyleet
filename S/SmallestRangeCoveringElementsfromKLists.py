'''
-Hard-

*Sliding Window*
*Priority Queue*

You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

 

Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Example 2:

Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]
 

Constraints:

nums.length == k
1 <= k <= 3500
1 <= nums[i].length <= 50
-105 <= nums[i][j] <= 105
nums[i] is sorted in non-decreasing order.

'''

from typing import List
import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Maintain a sliding window of size k in a min heap
        A = nums
        pq = [(row[0], i, 0) for i, row in enumerate(A)]
        heapq.heapify(pq)
        right = max([row[0] for row in A])
        ans = -10**9, 10**-9
        while pq:
            left, i, j = heapq.heappop(pq)
            if right - left < ans[1]- ans[0]:
                ans = left, right
            if j+1 == len(A[i]):
                return ans
            v = A[i][j+1]
            right = max(right, v)
            heapq.heappush(pq, (v, i, j+1))
        return ans
