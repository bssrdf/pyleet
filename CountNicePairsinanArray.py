'''
-Medium-



You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:

0 <= i < j < nums.length
nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [42,11,1,97]
Output: 2
Explanation: The two pairs are:
 - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
 - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.
Example 2:

Input: nums = [13,10,35,24,76]
Output: 4
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109



'''

from typing import List

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i] - int(str(nums[i])[::-1])
        m, mod = {}, 10**9 + 7        
        ans = 0
        for i in range(n):
            if nums[i] in m:
                ans = (ans + m[nums[i]]) % mod
                m[nums[i]] += 1
            else:
                m[nums[i]] = 1
        return ans

if __name__ == "__main__":
    print(Solution().countNicePairs(nums = [13,10,35,24,76]))