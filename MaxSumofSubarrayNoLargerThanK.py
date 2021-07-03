'''

-Medium-

Given an array nums and an integer k, return the max sum of a 
subarray in the array such that its sum is no larger than k.

It is guaranteed that there will be a subarray with a sum no larger than k.

Example 1:


Input: nums = [0,-2,3], k = 2
Output: 1
Explanation:

'''

import bisect

class Solution(object):
    def maxSumSubarray(self, nums, k):
        cumSum = [0]
        cum, maxSum = 0, -float('inf')
        for num in nums:
            cum += num
            left = bisect.bisect_left(cumSum, cum-k)
            if left < len(cumSum):
                maxSum = max(maxSum, cum - cumSum[left])
            bisect.insort(cumSum, cum)
        return maxSum


if __name__ == "__main__":
    print(Solution().maxSumSubarray(nums = [0,-2,3], k = 2))
