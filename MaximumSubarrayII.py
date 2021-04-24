'''
-Medium-

Given an array of integers, find two non-overlapping subarrays which have the largest sum.

The number in each subarray should be contiguous.

Return the largest sum.

Notice: The subarray should contain at least one number

Example
For given [1, 3, -1, 2, -1, 2], the two subarrays are [1, 3] and [2, -1, 2] or [1, 3, -1, 2] and [2], 
they both have the largest sum 7.

'''

class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        # write your code here
        n = len(nums)
        maxLeft, maxRight = [-float('inf')]*n, [-float('inf')]*n
        sums, mx = 0, -float('inf')
        for i in range(n):
            sums += nums[i]
            mx = max(sums, mx)
            if sums < 0: sums = 0
            maxLeft[i] = mx
        sums, mx = 0, -float('inf')
        for i in range(n-1,-1,-1):
            sums += nums[i]
            mx = max(sums, mx)
            if sums < 0: sums = 0
            maxRight[i] = mx
        res = -float('inf')
        for i in range(n-1):
            print(i, maxLeft[i], maxRight[i+1])
            res = max(res, maxLeft[i]+maxRight[i+1])
        return res

if __name__ == "__main__":
    print(Solution().maxTwoSubArrays([1, 3, -1, 2, -1, 2]))
    print(Solution().maxTwoSubArrays([-2, -1, 1, 3, -1, 2, -1, 2]))