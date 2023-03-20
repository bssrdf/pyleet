'''
-Medium-

Given an integer array nums and an integer k, return the number of subarrays of nums where the least common multiple of the subarray's elements is k.

A subarray is a contiguous non-empty sequence of elements within an array.

The least common multiple of an array is the smallest positive integer that is divisible by all the array elements.

 

Example 1:

Input: nums = [3,6,2,7,1], k = 6
Output: 4
Explanation: The subarrays of nums where 6 is the least common multiple of all the subarray's elements are:
- [3,6,2,7,1]
- [3,6,2,7,1]
- [3,6,2,7,1]
- [3,6,2,7,1]
Example 2:

Input: nums = [3], k = 2
Output: 0
Explanation: There are no subarrays of nums where 2 is the least common multiple of all the subarray's elements.
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i], k <= 1000

'''
from math import gcd
from typing import List
class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):            
            if k % nums[i] != 0:
                continue
            g = nums[i]
            m = nums[i]            
            m1 = m             
            if m == k:
                ans += 1
            for j in range(i+1, n):
                if k % nums[j] == 0:
                    g = gcd(g, nums[j])
                    m = m1 * nums[j]
                    if m//g == k:
                        ans += 1  
                else:
                    break              
                g = nums[j]
                m1 = nums[j]
        return ans

    def subarrayLCM2(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        def lcm(a, b):
            return a * b // gcd(a,b)
        for i in range(n):            
            l = nums[i]
            for j in range(i, n):
                l = lcm(l, nums[j])
                if l == k: ans += 1  
                elif l > k:
                    break              
        return ans
                    
print(Solution().subarrayLCM([2,1,1,5], 5))      
print(Solution().subarrayLCM([3,6,2,7,1], 6))
print(Solution().subarrayLCM2([2,1,1,5], 5))      
print(Solution().subarrayLCM2([3,6,2,7,1], 6))