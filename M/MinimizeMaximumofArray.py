'''
-Medium-
*Binary Search*

You are given a 0-indexed array nums comprising of n non-negative integers.

In one operation, you must:

Choose an integer i such that 1 <= i < n and nums[i] > 0.
Decrease nums[i] by 1.
Increase nums[i - 1] by 1.
Return the minimum possible value of the maximum integer of nums after performing any number of operations.

 

Example 1:

Input: nums = [3,7,1,6]
Output: 5
Explanation:
One set of optimal operations is as follows:
1. Choose i = 1, and nums becomes [4,6,1,6].
2. Choose i = 3, and nums becomes [4,6,2,5].
3. Choose i = 1, and nums becomes [5,5,2,5].
The maximum integer of nums is 5. It can be shown that the maximum number cannot be less than 5.
Therefore, we return 5.
Example 2:

Input: nums = [10,1]
Output: 10
Explanation:
It is optimal to leave nums as is, and since 10 is the maximum value, we return 10.
 

Constraints:

n == nums.length
2 <= n <= 105
0 <= nums[i] <= 109


'''

from typing import List

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        # Wrong
        A, n = nums, len(nums)
        i = 1
        j = 0
        ans = 0
        while i < n:
            while i < n and A[i] >= A[i-1]:
                i += 1
            while j <= i and A[j]==A[j+1]:
                j += 1
            ans = max(ans, A[j]+(A[i-1]-A[j]+1)//2)
            j = i
            i += 1
        return ans    

    def minimizeArrayValue2(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, max(nums)+1
        def valid(m):
            i, a = n-1, nums[n-1] 
            while i > 0:
                b = nums[i-1] + (a - m if a > m else 0)
                a = b
                i -= 1
            return b <= m         
        while l < r:
            mid = l + (r-l)//2
            if valid(mid):
                r = mid
            else:
                l = mid + 1
            # print(l, r, mid)
        return l

    
if __name__ == "__main__":
    print(Solution().minimizeArrayValue2(nums = [3,7,1,6]))
    print(Solution().minimizeArrayValue2(nums = [13,13,20,0,8,9,9]))