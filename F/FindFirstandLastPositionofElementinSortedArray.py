'''

-Medium-


Given an array of integers nums sorted in ascending order, find the starting and 
ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non-decreasing array.
-10^9 <= target <= 10^9
'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        found = False
        l, r = 0, n
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                r = mid
                found = True                 
            elif nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid+1
        left = l
        l, r = 0, n
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                l = mid+1
            elif nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid+1
        right = l - 1    
        return  [left, right] if found else [-1, -1]

if __name__ == "__main__":
    print(Solution().searchRange([5,7,7,8,8,10], 8))
    print(Solution().searchRange([5,7,7,8,8,10], 6))