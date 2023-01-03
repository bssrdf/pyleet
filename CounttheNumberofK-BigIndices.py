'''


-Hard-

$$$

*Fenwick Tree*

You are given a 0-indexed integer array nums and a positive integer k.

We call an index i k-big if the following conditions are satisfied:

There exist at least k different indices idx1 such that idx1 < i and nums[idx1] < nums[i].
There exist at least k different indices idx2 such that idx2 > i and nums[idx2] < nums[i].
Return the number of k-big indices.

 

Example 1:

Input: nums = [2,3,6,5,2,3], k = 2
Output: 2
Explanation: There are only two 2-big indices in nums:
- i = 2 --> There are two valid idx1: 0 and 1. There are three valid idx2: 2, 3, and 4.
- i = 3 --> There are two valid idx1: 0 and 1. There are two valid idx2: 3 and 4.
Example 2:

Input: nums = [1,1,1], k = 3
Output: 0
Explanation: There are no 3-big indices in nums.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i], k <= nums.length





'''

from typing import List

class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        # Wrong
        A = nums
        n = len(nums)
        ans = 0
        left = [0]*n
        right = [0]*n
        stack = []
        for i in range(n):
            while stack and A[stack[-1]] >= A[i]:
                stack.pop()
            left[i] = len(stack)
            stack.append(i)
        stack = []
        for i in range(n-1, -1, -1):
            while stack and A[stack[-1]] >= A[i]:
                stack.pop()
            right[i] = len(stack)
            stack.append(i)
        # print(left)
        # print(right)
        for i in range(n):
            if left[i] >= k and right[i] >= k:
                ans += 1 
        return ans      
    
    def kBigIndices2(self, nums: List[int], k: int) -> int:
        A = nums
        n, ans = len(nums), 0
        bit1, bit2 = [0]*(n+1), [0]*(n+1)
        left, right = [0]*n, [0]*n
        def update(b, i):
            while i <= n:
                b[i] += 1
                i += i & (-i)
        def query(b, i):
            t = 0
            while i > 0:
                t += b[i]
                i -= i & (-i) 
            return t
        
        for i,a in enumerate(A):
            left[i] = query(bit1, a-1)
            update(bit1, a)
        for i,a in enumerate(A[::-1]):
            right[i] = query(bit2, a-1)
            update(bit2, a)
        for i in range(n):
            if left[i] >= k and right[n-i-1] >= k:
                ans += 1 
        return ans      



if __name__ == "__main__":
    # print(Solution().kBigIndices(nums = [2,3,6,5,2,3], k = 2))
    print(Solution().kBigIndices2(nums = [2,3,6,5,2,3], k = 2))
    print(Solution().kBigIndices2(nums = [2,3,6,2,5,3], k = 2))
    print(Solution().kBigIndices2(nums = [1,1,1], k = 3))