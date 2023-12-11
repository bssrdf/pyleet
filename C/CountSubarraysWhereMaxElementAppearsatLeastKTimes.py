'''

-Medium-

You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.

 

Example 1:

Input: nums = [1,3,2,3,3], k = 2
Output: 6
Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
Example 2:

Input: nums = [1,4,2,1], k = 3
Output: 0
Explanation: No subarray contains the element 4 at least 3 times.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106
1 <= k <= 105


'''
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n, mx = len(nums), max(nums)
        cnt = 0
        preSum = {}
        ans = 0
        for i in range(n):
            cnt += nums[i] == mx
            if cnt > 0 and cnt not in preSum:
                preSum[cnt] = i
            if cnt >= k and  cnt - k + 1 in preSum:
                ans += preSum[cnt-k+1]+1
            # print(i, ans, preSum)
        return ans       



if __name__ == "__main__":
    print(Solution().countSubarrays(nums = [1,3,2,3,3], k = 2))
    print(Solution().countSubarrays( nums = [1,4,2,1], k = 3))



