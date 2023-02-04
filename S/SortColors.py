'''
Given an array nums with n objects colored red, white, or blue, sort them in-place 
o that objects of the same color are adjacent, with the colors in the order red, 
white, and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and 
blue respectively.

Follow up:

Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?
 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
Example 3:

Input: nums = [0]
Output: [0]
Example 4:

Input: nums = [1]
Output: [1]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is 0, 1, or 2.

'''

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        '''
        maintain three pointers(counters), r,w and b with the following invariants:
        r:   # of red   (0) elements found
        w-r: # of white (1) elements found
        n-b: # of blue  (2) elements found
        '''
        n = len(nums)
        r, w, b = 0, 0, n
        while b != w:
            if nums[w] == 0:
                nums[r], nums[w] = nums[w], nums[r]
                r += 1
                w += 1
            elif nums[w] == 1:
                w += 1
            elif nums[w] == 2:
                b -= 1
                nums[b], nums[w] = nums[w], nums[b]
                

if __name__ == "__main__":
    a = [2,0,2,1,1,0]
    print(Solution().sortColors(a))
    print(a)