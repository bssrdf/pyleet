'''

-Medium-

You are given a 0-indexed integer array nums.

The effective value of three indices i, j, and k is defined as ((nums[i] | nums[j]) & nums[k]).

The xor-beauty of the array is the XORing of the effective values of all the possible triplets of indices (i, j, k) where 0 <= i, j, k < n.

Return the xor-beauty of nums.

Note that:

val1 | val2 is bitwise OR of val1 and val2.
val1 & val2 is bitwise AND of val1 and val2.
 

Example 1:

Input: nums = [1,4]
Output: 5
Explanation: 
The triplets and their corresponding effective values are listed below:
- (0,0,0) with effective value ((1 | 1) & 1) = 1
- (0,0,1) with effective value ((1 | 1) & 4) = 0
- (0,1,0) with effective value ((1 | 4) & 1) = 1
- (0,1,1) with effective value ((1 | 4) & 4) = 4
- (1,0,0) with effective value ((4 | 1) & 1) = 1
- (1,0,1) with effective value ((4 | 1) & 4) = 4
- (1,1,0) with effective value ((4 | 4) & 1) = 0
- (1,1,1) with effective value ((4 | 4) & 4) = 4 
Xor-beauty of array will be bitwise XOR of all beauties = 1 ^ 0 ^ 1 ^ 4 ^ 1 ^ 4 ^ 0 ^ 4 = 5.
Example 2:

Input: nums = [15,45,20,2,34,35,5,44,32,30]
Output: 34
Explanation: The xor-beauty of the given array is 34.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109



'''

from typing import List

class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        n = len(nums)
        n3, n2 = n**3, n**2
        bit0 = [0]*31
        for a in nums:
            for i in range(31):
                if (1 << i) & a == 0:
                    bit0[i] += 1
        ones = [n3]*31
        for i in range(31):
            for a in nums:
                if (1 << i) & a == 0:
                    ones[i] -= n2
                else:
                    ones[i] -= bit0[i]**2
        s = ''.join('1' if i % 2 == 1 else '0' for i in ones)
        # print(s[::-1])
        return int(s[::-1], base = 2)

                


if __name__ == "__main__":
    print(Solution().xorBeauty(nums = [1,4]))
    print(Solution().xorBeauty(nums = [15,45,20,2,34,35,5,44,32,30]))
