'''
-Medium-


You are given a 0-indexed integer array nums. For each index i (1 <= i <= nums.length - 2) the beauty of nums[i] equals:

2, if nums[j] < nums[i] < nums[k], for all 0 <= j < i and for all i < k <= nums.length - 1.
1, if nums[i - 1] < nums[i] < nums[i + 1], and the previous condition is not satisfied.
0, if none of the previous conditions holds.
Return the sum of beauty of all nums[i] where 1 <= i <= nums.length - 2.

 

Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation: For each index i in the range 1 <= i <= 1:
- The beauty of nums[1] equals 2.
Example 2:

Input: nums = [2,4,6,4]
Output: 1
Explanation: For each index i in the range 1 <= i <= 2:
- The beauty of nums[1] equals 1.
- The beauty of nums[2] equals 0.
Example 3:

Input: nums = [3,2,1]
Output: 0
Explanation: For each index i in the range 1 <= i <= 1:
- The beauty of nums[1] equals 0.
 

Constraints:

3 <= nums.length <= 105
1 <= nums[i] <= 105


'''


from typing import List
from collections import deque

class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        A, n = nums, len(nums) 
        f, b = [-1]*n, [10**5+1]*n    
        for i in range(1, n):
            # f[i] max in [0, i-1]
            f[i] = max(f[i-1], A[i-1])
        for i in range(n-2, -1, -1):
            # b[i] min in [i+1, n-1]
            b[i] = min(b[i+1], A[i+1])
        ans = 0
        for i in range(1, len(A)-1):
            if A[i] > f[i] and A[i] < b[i]:
                ans += 2
            elif A[i-1] < A[i] < A[i+1]:
                ans += 1 
        return ans
        

        
    
    def sumOfBeauties2(self, nums: List[int]) -> int:
        A, n = nums, max(nums)
        BIT = [0]*(n+1)
        left, right = [-1]*len(nums), [-1]*len(nums)
        def update(x, val):
            while x <= n:
                BIT[x] += val
                x += x & (-x)
        def query(x):
            sums = 0
            while x > 0:
                sums += BIT[x]
                x -= x & (-x) 
            return sums 
        for i, a in enumerate(A):
            left[i] = query(a-1)
            update(a, 1)
        BIT = [0]*(n+1)
        for i in range(len(A)-1, -1, -1):
            right[i] = query(n) - query(A[i])
            update(A[i], 1)
        ans = 0
        for i in range(1, len(A)-1):
            if left[i] == i and right[i] == (len(A)-i-1):
                ans += 2
            elif A[i-1] < A[i] < A[i+1]:
                ans += 1 
        # print(left)
        # print(right)
        return ans



        
        
if __name__ == "__main__":
    print(Solution().sumOfBeauties(nums = [4,2,4,6,7,8]))
    print(Solution().sumOfBeauties(nums = [1,2,3]))
    print(Solution().sumOfBeauties(nums = [2,4,6,4]))
    print(Solution().sumOfBeauties(nums = [3,2,1]))
    print(Solution().sumOfBeauties2(nums = [4,2,4,6,7,8]))
    print(Solution().sumOfBeauties2(nums = [1,2,3]))
    print(Solution().sumOfBeauties2(nums = [2,4,6,4]))
    print(Solution().sumOfBeauties2(nums = [3,2,1]))