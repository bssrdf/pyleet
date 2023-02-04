'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
i.e., 0 
(1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        l,r=0,len(nums)-1
        while r-l > 1:
            m = l+(r-l)/2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m+1
            #if nums[m] > nums[l]:
            #    if nums[m] < nums[r]:
            #        r = m
            #    else:
            #        l = m+1
        return min(nums[l], nums[r])

if __name__ == "__main__":
    assert Solution().findMin([3, 1, 2]) == 1
    assert Solution().findMin([1, 2, 3, 4, 5]) == 1
    assert Solution().findMin([2, 3, 4, 5, 1]) == 1
    assert Solution().findMin([5, 1, 2, 3, 4]) == 1
    assert Solution().findMin([9, 10, 11, 12, 0, 1, 2, 3, 4, 5, 6]) == 0
