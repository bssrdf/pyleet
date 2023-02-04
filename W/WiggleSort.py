'''
Given an unsorted array nums, reorder it in-place such that 
nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:

Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]

'''
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        for i in range(1,n):
            if ( (i+1)%2 == 0 and nums[i] < nums[i-1] or
                 (i+1)%2 == 1 and nums[i] > nums[i-1] ):
                nums[i], nums[i-1] = nums[i-1], nums[i]
            
        






if __name__ == "__main__":
    a = [3,5,2,1,6,4]
    print(Solution().sortColors(a))
    print(a)