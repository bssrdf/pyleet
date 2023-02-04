'''

-Easy-

Given a sorted array of distinct integers and a target value, return the index if 
the target is found. If not, return the index where it would be if it were 
inserted in order.
 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0
Example 5:

Input: nums = [1], target = 0
Output: 0
 

Constraints:

1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4

'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target: 
                left = mid+1
            elif nums[mid] > target: 
                right = mid
        return left

            


if __name__ == "__main__":
    print(Solution().searchInsert([1,3,5,6], 5))
    print(Solution().searchInsert([1,3,5,6], 2))
    print(Solution().searchInsert([1,3,5,6], 7))
    print(Solution().searchInsert([1,3,5,6], 0))