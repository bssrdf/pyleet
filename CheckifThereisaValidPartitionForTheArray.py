'''
-Medium-
*DP*

You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.

We call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:

The subarray consists of exactly 2 equal elements. For example, the subarray [2,2] is good.
The subarray consists of exactly 3 equal elements. For example, the subarray [4,4,4] is good.
The subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements is 1. For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.
Return true if the array has at least one valid partition. Otherwise, return false.

 

Example 1:

Input: nums = [4,4,4,5,6]
Output: true
Explanation: The array can be partitioned into the subarrays [4,4] and [4,5,6].
This partition is valid, so we return true.
Example 2:

Input: nums = [1,1,1,2]
Output: false
Explanation: There is no valid partition for this array.
 

Constraints:

2 <= nums.length <= 105
1 <= nums[i] <= 106


--> Key points: after partitioning, all subarrays only contain
    2 equal elements, or
    3 equal elements, or
    3 elements with difference between them = 1

'''


from typing import List

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        #We are setting all of them to be true because if 
        # we take any number of steps from last index, the answer is true

        dp_1 = True #represents (i+1) state
        dp_2 = True #represents (i+2) state
        dp_3 = True #represents (i+3) state
        
        for i in range(len(nums)-1, -1, -1):
            cur = False #current dp state
            if i+1 < len(nums) and nums[i] == nums[i+1]:
                cur = cur or dp_2
            if i+2 < len(nums):
                if nums[i] == nums[i+1] == nums[i+2]:
                    cur = cur or dp_3
                elif nums[i+1]-nums[i] == nums[i+2]-nums[i+1] == 1:
                    cur = cur or dp_3
            dp_1, dp_2, dp_3 = cur, dp_1, dp_2
        return dp_1


        

if __name__ == "__main__":
    print(Solution().validPartition(nums = [4,4,4,5,6]))