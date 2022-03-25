'''
-Easy-

You are given an integer array nums and an integer k. You want 
to find a subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array 
by deleting some or no elements without changing the order of the 
remaining elements.

 

Example 1:

Input: nums = [2,1,3,3], k = 2
Output: [3,3]
Explanation:
The subsequence has the largest sum of 3 + 3 = 6.
Example 2:

Input: nums = [-1,-2,3,4], k = 3
Output: [-1,3,4]
Explanation: 
The subsequence has the largest sum of -1 + 3 + 4 = 6.
Example 3:

Input: nums = [3,4,3,3], k = 2
Output: [3,4]
Explanation:
The subsequence has the largest sum of 3 + 4 = 7. 
Another possible subsequence is [4, 3].
 

Constraints:

1 <= nums.length <= 1000
-105 <= nums[i] <= 105
1 <= k <= nums.length

'''

from typing import List
from random import randint
from collections import Counter
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        def partition(p, r):           
            x = nums[r]
            i = p-1
            for j in range(p,r):
                if nums[j] < x:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i+1],nums[r] = nums[r], nums[i+1]    
            return i+1     

        def random_partition(p,r):
            ri = randint(p,r)
            nums[ri], nums[r] = nums[r], nums[ri]
            return partition(p, r)     

        def select(p, r, k):
            # returns kth smallest
            if p == r:
                return nums[p]
            q = random_partition(p, r)
            i = q-p+1
            if i == k:
                return nums[q]
            elif k < i:
                return select(p, q-1, k)
            else:
                return select(q+1, r, k-i)
        n = len(nums)    
        arr, ans = nums[:], []

        pivot = select(0, n-1, n-k+1) 
        left = 0
        for i in range(n-k, n):   
            if nums[i] == pivot: left += 1 
        for i in range(n):
            if arr[i] > pivot:
                ans.append(arr[i])
            elif arr[i] == pivot and left-1 >= 0:
                ans.append(arr[i])
                left -= 1
        return ans
        
    
if __name__ == "__main__":
    print(Solution().maxSubsequence(nums = [2,1,3,3], k = 2))
    print(Solution().maxSubsequence(nums = [-1,-2,3,4], k = 3))
    print(Solution().maxSubsequence(nums = [3,4,3,3], k = 2))
    print(Solution().maxSubsequence(nums = [63,-74,61,-17,-55,
    -59,-10,2,-60,-65], k = 9))