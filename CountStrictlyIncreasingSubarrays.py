'''

-Medium-
$$$

*DP*

You are given an array nums consisting of positive integers.

Return the number of subarrays of nums that are in strictly increasing order.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,3,5,4,4,6]
Output: 10
Explanation: The strictly increasing subarrays are the following:
- Subarrays of length 1: [1], [3], [5], [4], [4], [6].
- Subarrays of length 2: [1,3], [3,5], [4,6].
- Subarrays of length 3: [1,3,5].
The total number of subarrays is 6 + 3 + 1 = 10.
Example 2:

Input: nums = [1,2,3,4,5]
Output: 15
Explanation: Every subarray is strictly increasing. There are 15 possible subarrays that we can take.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106


'''

from typing import List


class Solution:
    def countIncreasing(self, nums: List[int]) -> int:
        cnt = 1  
        ans = cnt
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cnt += 1
            else:
                cnt = 1
            ans += cnt
        return ans
            

if __name__ == "__main__":
    print(Solution().countIncreasing(nums = [1,3,5,4,4,6]))
    print(Solution().countIncreasing(nums = [1,2,3,4,5]))
    print(Solution().countIncreasing(nums = [5,4,3,2,1]))