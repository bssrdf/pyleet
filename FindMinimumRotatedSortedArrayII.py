"""
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
"""
import sys

__author__ = 'Danyang'


class Solution(object):
    def findMin(self, nums):
        """
        similar to find target in rotated sorted array

        :type A: list
        :param A: a list of integer
        :return: an integer
        """
        if not nums:
            return None
        l,r=0,len(nums)-1
        while r-l > 1:
            m = l+(r-l)/2
            if nums[m] < nums[r]:
                r = m
            elif nums[m] > nums[r]:
                l = m+1
            else:
                r -= 1
        return min(nums[l], nums[r])

if __name__ == "__main__":
    num = [7, 1, 2, 2, 3, 4, 5, 6]
    #num = [10, 1, 10, 10, 10]
    #num = [3,3,1,3]
    assert Solution().findMin(num) == 1
