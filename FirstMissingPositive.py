'''
Given an unsorted integer array, find the smallest missing positive 
integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Follow up:

Your algorithm should run in O(n) time and uses constant extra space.

'''
import sys
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 1
        n = len(nums)
        print(n)
        for i,num in enumerate(nums):            
            while 0 < nums[i] <= n and nums[i] != nums[nums[i]-1]:              
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]              
            print(nums)
        for i,num in enumerate(nums):
            if num != i+1:
                return i+1
        return n+1        
        


if __name__ == "__main__":
    #print(Solution().firstMissingPositive([3,4,-1,1]))
    #print(Solution().firstMissingPositive([1,2,0]))
    #print(Solution().firstMissingPositive([7,8,9,11,12]))
    #print(Solution().firstMissingPositive([1]))
    print(Solution().firstMissingPositive([3,-1,23,7,21,12,8,9
    18,21,-1,16,1,13,-3,22,23,13,7,14,3,6,4,-3]))