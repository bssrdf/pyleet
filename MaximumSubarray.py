'''
Find the contiguous subarray within an array (containing at least one number) which 
has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
'''
import sys

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        sums = [0]*len(nums)
        sums[0] = nums[0]
        res = sums[0]
        for i in range(1, len(nums)):
            sums[i] = sums[i-1]+nums[i] if sums[i-1] > 0 else nums[i]
            res = max(sums[i], res)
        return res

if __name__ == "__main__":
    assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6