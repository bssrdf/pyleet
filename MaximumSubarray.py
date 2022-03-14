'''
-Easy-
*Two Passes*
*DP*
*Kadane's Algorithm*


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
          #  print(i, sums[i], res)
        return res

    def maxSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        localMaxSum, globalMaxSum  = nums[0], nums[0] 

        for i in range(1, len(nums)):
            # localMaxSum(i) defined as the maxmimum between 
            # 1. localMaxSum(i-1)  + nums[i] which is the accumulated maxSum so far + current one
            # 2. nums[i]
            localMaxSum = max(localMaxSum+nums[i], nums[i])
            globalMaxSum = max(globalMaxSum, localMaxSum)
        return globalMaxSum
        
        

if __name__ == "__main__":
    assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert Solution().maxSubArray([-2, -6]) == -2
    assert Solution().maxSubArray2([-2, -6]) == -2