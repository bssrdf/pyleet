'''

-Easy-

Given an integer array nums and an integer k, modify the array in the following way:

choose an index i and replace nums[i] with -nums[i].
You should apply this process exactly k times. You may choose the same index i 
multiple times.

Return the largest possible sum of the array after modifying it in this way.

 

Example 1:

Input: nums = [4,2,3], k = 1
Output: 5
Explanation: Choose index 1 and nums becomes [4,-2,3].
Example 2:

Input: nums = [3,-1,0,2], k = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and nums becomes [3,1,0,2].
Example 3:

Input: nums = [2,-3,-1,5,-4], k = 2
Output: 13
Explanation: Choose indices (1, 4) and nums becomes [2,3,-1,5,4].
 

Constraints:

1 <= nums.length <= 10^4
-100 <= nums[i] <= 100
1 <= k <= 10^4

'''

from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
            else:
                if k % 2 == 1: 
                    if i > 0 and nums[i-1] < nums[i]:
                        nums[i-1] = -nums[i-1]
                    else:
                        nums[i] = -nums[i]
                k = 0
                break
            if k == 0: break
        if k > 0 and k % 2 == 1:                 
            nums[-1] = -nums[-1]
        return sum(nums) 


if __name__ == "__main__":
    #print(Solution().largestSumAfterKNegations(nums = [2,-3,-1,5,-4], k = 2))
    print(Solution().largestSumAfterKNegations(nums = [4,2,3], k = 1))
    #print(Solution().largestSumAfterKNegations(nums = [3,-1,0,2], k = 3))
    #print(Solution().largestSumAfterKNegations([-8,3,-5,-3,-5,-2], 6))