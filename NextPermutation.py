'''
-Medium-


Implement next permutation, which rearranges numbers into the lexicographically 
next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest 
possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100

'''

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums) 
        i, j = n - 2,  n - 1
        while i >= 0 and nums[i] >= nums[i + 1]: i -= 1 
        if i >= 0:
            while nums[j] <= nums[i]: j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j = n-1
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1



if __name__ == "__main__":
    a = [1,2,3]
    #Solution().nextPermutation(a)
    #print(a)
    a = [3,2,1]
    Solution().nextPermutation(a)
    print(a)