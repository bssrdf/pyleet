'''
Given an unsorted array nums, reorder it such that 
nums[0] < nums[1] > nums[2] < nums[3]....

Example 1:

Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].
Example 2:

Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].
Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?



'''

from QuickSelect import quickselect_median

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        mid = quickselect_median(nums)                
        print(mid)
        i = (n - 1) // 2 * 2
        j = i
        k = 1
        '''
        https://leetcode.com/discuss/76965/3-lines-python-with-explanation-proof

        (1) elements smaller than the 'median' are put into the last even slots

        (2) elements larger than the 'median' are put into the first odd slots

        (3) the medians are put into the remaining slots.

        '''
        for c in range(n):       
            if (nums[j] < mid):
                nums[i], nums[j] = nums[j], nums[i] 
                i -= 2
                j -= 2
                if j < 0: j = n // 2 * 2 - 1
            elif (nums[j] > mid): 
                nums[j], nums[k] = nums[k], nums[j]
                k += 2
            else:
                j -= 2
                if j < 0: j = n // 2 * 2 - 1


if __name__ == "__main__":
    a = [1, 5, 1, 1, 6, 4]
    Solution().wiggleSort(a)
    print(a)
    a = [1, 3, 2, 2, 3, 1]
    Solution().wiggleSort(a)
    print(a)
    