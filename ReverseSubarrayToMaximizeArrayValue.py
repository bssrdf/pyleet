'''
-Hard-
*Greedy*
*Math*


You are given an integer array nums. The value of this array is defined as the sum of |nums[i] - nums[i + 1]| for all 0 <= i < nums.length - 1.

You are allowed to select any subarray of the given array and reverse it. You can perform this operation only once.

Find maximum possible value of the final array.

 

Example 1:

Input: nums = [2,3,1,5,4]
Output: 10
Explanation: By reversing the subarray [3,1,5] the array becomes [2,5,1,3,4] whose value is 10.
Example 2:

Input: nums = [2,4,9,24,2,1,10]
Output: 68
 

Constraints:

1 <= nums.length <= 3 * 104
-105 <= nums[i] <= 105

'''
import math
from typing import List
class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        maxi, mini = -math.inf, math.inf
        
        for a, b in zip(nums, nums[1:]):
            maxi = max(min(a, b), maxi)
            mini = min(max(a, b), mini)
        change = max(0, (maxi - mini) * 2)
        
        # solving the boundary situation
        for a, b in zip(nums, nums[1:]):
            tmp1 = - abs(a - b) + abs(nums[0] - b)
            tmp2 = - abs(a - b) + abs(nums[-1] - a)
            change = max([tmp1, tmp2, change])
			
        original_value = sum(abs(a - b) for a, b in zip(nums, nums[1:]))
        return  original_value + change
    

if __name__ == "__main__":
    print(Solution().maxValueAfterReverse(nums = [2,3,1,5,4]))