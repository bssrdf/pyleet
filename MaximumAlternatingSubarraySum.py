'''

-Medium-

The alternating sum of a 0-indexed array is defined as the sum of the elements 
at even indices minus the sum of the elements at odd indices.

Given an array find the maximum alternating subarray sum.

Example: [-1,2,-1,4,7]
Output is 7
Explanation:
Subarray [2,-1,4] has sum 2-(-1)+4=7
Subarray [7] has also sum 7

'''

from typing import List

class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:
        ans = -float('inf')
        even = 0  # subarray sum starting from an even index
        odd = 0  # subarray sum starting from an odd index

        for i in range(len(nums)):
            if (i & 1) == 0:  # must pick
                even += nums[i]
            else:  # fresh start or minus
                even = max(0, even - nums[i])
            ans = max(ans, even)

        for i in range(1, len(nums)):
            if i & 1:  # must pick
                odd += nums[i]
            else:  # fresh start or minus
                odd = max(0, odd - nums[i])
            ans = max(ans, odd)

        return ans

if __name__ == "__main__":

    print(Solution().maximumAlternatingSubarraySum([-1,2,-1,4,7]))