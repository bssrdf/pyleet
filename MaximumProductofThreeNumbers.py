'''

-Easy-

Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6
 

Constraints:

3 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000




'''


from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1 = max2 = max3 = -float('inf')
        min1 = min2 = float('inf')
        for i in nums:
            if i > max1:
                max3, max2, max1 = max2, max1, i
            elif i > max2:
                max3, max2 = max2, i
            elif i > max3:
                max3 = i
            if i < min1:
                min2, min1 = min1, i
            elif i < min2:
                min2 = i
        return max(max1*max2*max3, min1*min2*max1)



        

if __name__ == '__main__':
    print(Solution().maximumProduct([1,2,3]))