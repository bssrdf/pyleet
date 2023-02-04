'''
-Medium-

*Priority Queue*
*Sorting*

You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k. You must choose a subsequence of indices from nums1 of length k.

For chosen indices i0, i1, ..., ik - 1, your score is defined as:

The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.
It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).
Return the maximum possible score.

A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1} by deleting some or no elements.

 

Example 1:

Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
Output: 12
Explanation: 
The four possible subsequence scores are:
- We choose the indices 0, 1, and 2 with score = (1+3+3) * min(2,1,3) = 7.
- We choose the indices 0, 1, and 3 with score = (1+3+2) * min(2,1,4) = 6. 
- We choose the indices 0, 2, and 3 with score = (1+3+2) * min(2,3,4) = 12. 
- We choose the indices 1, 2, and 3 with score = (3+3+2) * min(1,3,4) = 8.
Therefore, we return the max score, which is 12.
Example 2:

Input: nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1
Output: 30
Explanation: 
Choosing index 2 is optimal: nums1[2] * nums2[2] = 3 * 10 = 30 is the maximum possible score.
 

Constraints:

n == nums1.length == nums2.length
1 <= n <= 105
0 <= nums1[i], nums2[j] <= 105
1 <= k <= n

'''

from typing import List
from collections import deque
import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:        
        # wrong
        n, ans = len(nums1), 0
        arr = [0]*n
        arr1 = [(a,i) for i,a in enumerate(nums2)]
        arr1.sort(reverse=True)        
        for i in range(n):
            arr[i] = nums1[arr1[i][1]]
        sumk = 0
        que = deque()
        print(arr)
        print(arr1)
        for i in range(n):
            sumk += arr[i]
            m2 = arr1[i][0] 
            while que and que[-1] > arr[i]:
                que.pop()      
            que.append(arr[i])              
            if i >= k:
                sumk -= que[0]               
            if i >= k-1: 
               ans = max(ans, sumk * m2)    
            
            print(i, m2, ans, sumk, que)
        return ans        
    
    def maxScore2(self, nums1: List[int], nums2: List[int], k: int) -> int:        
        n, ans = len(nums1), 0
        arr = list(range(n))
        arr.sort(key = lambda x: nums2[x], reverse=True)        
        sumk, pq = 0, []
        for i in range(n):
            sumk += nums1[arr[i]]
            if i >= k:
                sumk -= heapq.heappop(pq)
            if i >= k-1: 
                ans = max(ans, sumk * nums2[arr[i]])    
            heapq.heappush(pq, nums1[arr[i]])
        return ans        
    


    
if __name__ == '__main__':
    # print(Solution().maxScore(nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3))
    # print(Solution().maxScore(nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1))
    print(Solution().maxScore(nums1 = [2,1,14,12], nums2 = [11,7,13,6], k = 3))

    print(Solution().maxScore2(nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3))
    print(Solution().maxScore2(nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1))
    print(Solution().maxScore2(nums1 = [2,1,14,12], nums2 = [11,7,13,6], k = 3))