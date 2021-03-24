'''
-Easy-

Given an array nums, write a function to move all 0's to the end of it while maintaining 
the relative order of the non-zero elements.

Example:

Given nums = [0, 1, 0, 3, 12], 
after calling your function, 
nums should be [1, 3, 12, 0, 0].

'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lastNonZeroFoundAt = 0
        for cur in range(len(nums)):
            if nums[cur]:
                nums[cur], nums[lastNonZeroFoundAt] = nums[lastNonZeroFoundAt], nums[cur]
                lastNonZeroFoundAt += 1
        return

if __name__ == "__main__":
    a = [0,1,0,3,12]
    print(a)
    Solution().moveZeroes(a)
    print(a)
