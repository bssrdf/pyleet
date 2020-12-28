'''
-Medium-

Suppose an array sorted in ascending order is rotated at some pivot unknown to 
you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, 
otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums 
may contain duplicates.
Would this affect the run-time complexity? How and why?

'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(nums)-1
        while left <= right:
           mid = left + (right-left)//2
           if nums[mid] == target:
               return True           
           if nums[mid] < nums[right]:
               if nums[mid] < target and nums[right] >= target:
                   left = mid + 1
               else:
                   right = mid - 1
           elif nums[mid] > nums[right]:
               if nums[left] <= target and nums[mid] > target:
                   right = mid - 1
               else:
                   left = mid + 1
           else:
               right -= 1
        return False

        
if __name__ == "__main__":
    s = Solution()
    print(s.search([2,5,6,0,0,1,2], 0))
    print(s.search([2,5,6,0,0,1,2], 3))
    print(s.search([3,1,1], 3))
    print(s.search([1,1,3,1], 3))
