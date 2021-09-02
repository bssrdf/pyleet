'''
-Medium-

Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next 
element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a 
subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

 

Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3
Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
Example 3:

Input: nums = [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
Example 4:

Input: nums = [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
Example 5:

Input: nums = [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1
 

Constraints:

n == nums.length
1 <= n <= 3 * 10^4
-3 * 10^4 <= nums[i] <= 3 * 10^4


'''

class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        n = len(nums)
        maxSums, minSums = nums[0], nums[0]
        maxSum, minSum = maxSums, minSums
        total = nums[0]
        for i in range(1, n):
            maxSums = max(maxSums+nums[i], nums[i])
            minSums = min(minSums+nums[i], nums[i])
            total += nums[i]            
            maxSum = max(maxSum, maxSums)
            minSum = min(minSum, minSums)
       # print(total, minSum, maxSum)
        return max(maxSum, total-minSum) if maxSum > 0 else maxSum

        
if __name__ == "__main__":
    print(Solution().maxSubarraySumCircular([1,-2,3,-2]))
    print(Solution().maxSubarraySumCircular([5,-3,5]))
    print(Solution().maxSubarraySumCircular([-2,-3,-1]))