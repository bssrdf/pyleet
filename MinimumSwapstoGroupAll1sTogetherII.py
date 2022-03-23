'''

-Medium-


A swap is defined as taking two distinct positions in an array and swapping the 
values in them.

A circular array is defined as an array where we consider the first element and 
the last element to be adjacent.

Given a binary circular array nums, return the minimum number of swaps required 
to group all 1's present in the array together at any location.

 

Example 1:

Input: nums = [0,1,0,1,1,0,0]
Output: 1
Explanation: Here are a few of the ways to group all the 1's together:
[0,0,1,1,1,0,0] using 1 swap.
[0,1,1,1,0,0,0] using 1 swap.
[1,1,0,0,0,0,1] using 2 swaps (using the circular property of the array).
There is no way to group all 1's together with 0 swaps.
Thus, the minimum number of swaps required is 1.
Example 2:

Input: nums = [0,1,1,1,0,0,1,1,0]
Output: 2
Explanation: Here are a few of the ways to group all the 1's together:
[1,1,1,0,0,0,0,1,1] using 2 swaps (using the circular property of the array).
[1,1,1,1,1,0,0,0,0] using 2 swaps.
There is no way to group all 1's together with 0 or 1 swaps.
Thus, the minimum number of swaps required is 2.
Example 3:

Input: nums = [1,1,0,0,1]
Output: 0
Explanation: All the 1's are already grouped together due to the circular property of the array.
Thus, the minimum number of swaps required is 0.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.



'''

from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = sum(nums)    
        nums = nums + nums
        
        l, r = 0, 0
        cnt, mx = 0, 0
        while r < len(nums):
            if nums[r] == 1:
                cnt += 1
            r += 1
            while r-l == n:
                mx = max(mx, cnt)
                if nums[l] == 1:
                    cnt -= 1
                l += 1
        return n-mx

    def minSwaps2(self, nums: List[int]) -> int:
        k = sum(nums)    
        nums = nums + nums
        cnt, mx = 0, 0
        for i in range(len(nums)//2+k):            
            if nums[i] == 1:
                cnt += 1
            if i-k >= 0:
                if nums[i-k] == 1:
                    cnt -= 1 
            if i >= k-1:
                mx = max(mx, cnt)
              
        return k-mx