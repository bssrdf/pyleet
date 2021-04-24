'''
-Medium-

Given an integer arrays, find a contiguous subarray which has the largest sum and length should be 
greater or equal to given lengthk.
Return the largest sum, return 0 if there are fewer than k elements in the array.

Notice
Ensure that the result is an integer type.

Have you met this question in a real interview?

Yes

Example

Given the array[-2,2,-3,4,-1,2,1,-5,3] and k =5, the contiguous subarray[2,-3,4,-1,2,1] 
has the largest sum = 5.

'''

class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxSubArrays(self, nums, k):
        # write your code here
        n = len(nums)
        if k > n: return 0
        sums = [0]*(n+1)
        minPre = 0
        res = -float('inf')
        for i in range(1, n+1):
            sums[i] = sums[i-1] + nums[i-1] 
            if i < k: continue
            minPre = min(minPre, sums[i-k])            
            res = max(res, sums[i]-minPre)
        return res

if __name__ == "__main__":
    print(Solution().maxSubArrays([-2,2,-3,4,-1,2,1,-5,3], 5))

