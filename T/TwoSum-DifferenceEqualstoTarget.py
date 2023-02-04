'''

-Medium-

*Two Pointers*

Given an sorted array of integers, find two numbers that their difference equals to a target value.
Return a list with two number like [num1, num2] that the difference of num1 and num2 equals to 
target value, and num1 is less than num2.

It's guaranteed there is only one available solution.
Note: Requires O(1) space complexity to comple

样例
Example 1:

Input: nums = [2, 7, 15, 24], target = 5 
Output: [2, 7] 
Explanation:
(7 - 2 = 5)
Example 2:

Input: nums = [1, 1], target = 0
Output: [1, 1] 
Explanation:
(1 - 1 = 0)


'''

class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (num1 < num2)
    """
    def twoSum7(self, nums, target):
        # write your code here
        ## already sorted
        if len(nums) == 0 or len(nums) == 1: return []
        
        i = 0
        if target < 0: target = -target
        for j in range(1, len(nums)):
            # advance j until nums[j] - nums[i] > target
            # move i to the right until i==j or nums[j] - nums[i] <= target
            while i < j and nums[j] - nums[i] > target:
                i += 1
            # check whether nums[j] - nums[i] == target    
            if nums[j] - nums[i] == target and i != j:
                return [nums[i], nums[j]]
        return []


if __name__ == "__main__":
    print(Solution().twoSum7(nums = [2, 7, 15, 24], target = 5))
    print(Solution().twoSum7(nums = [1, 1], target = 0))