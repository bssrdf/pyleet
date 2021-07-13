'''

-Medium-
*Binary Search*

A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains 
multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index 
number 5 where the peak element is 6.
 

Constraints:

1 <= nums.length <= 1000
-2^31 <= nums[i] <= 2^31 - 1
nums[i] != nums[i + 1] for all valid i.
 

Follow up: Could you implement a solution with logarithmic complexity?


'''

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        由于题目中提示了要用对数级的时间复杂度，那么我们就要考虑使用类似于二分查找法来缩短时间，
        由于只是需要找到任意一个峰值，那么我们在确定二分查找折半后中间那个元素后，和紧跟的那个
        元素比较下大小，如果大于，则说明峰值在前面，如果小于则在后面。这样就可以找到一个峰值了，

        """
        left,  right = 0, len(nums)
        while left < right: # left open, right close, same as in general binary search pattern
            mid = left + (right - left) // 2
            if mid+1 < len(nums) and nums[mid] < nums[mid + 1]: left = mid + 1
            else: right = mid
        return right


if __name__ == "__main__":
    print(Solution().findPeakElement([1,2,1,3,5,6,4]))
    print(Solution().findPeakElement([1]))
    print(Solution().findPeakElement([3,1,2]))
