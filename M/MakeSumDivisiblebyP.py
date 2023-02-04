'''

-Medium-

Given an array of positive integers nums, remove the smallest subarray 
(possibly empty) such that the sum of the remaining elements is divisible by p. 
It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or -1 
if it's impossible.

A subarray is defined as a contiguous block of elements in the array.

 

Example 1:

Input: nums = [3,1,4,2], p = 6
Output: 1
Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.
Example 2:

Input: nums = [6,3,5,2], p = 9
Output: 2
Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.
Example 3:

Input: nums = [1,2,3], p = 3
Output: 0
Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.
Example 4:

Input: nums = [1,2,3], p = 7
Output: -1
Explanation: There is no way to remove a subarray in order to get a sum divisible by 7.
Example 5:

Input: nums = [1000000000,1000000000,1000000000], p = 3
Output: 0
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= p <= 10^9

'''
from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        preSum = [0]
        for i in range(n):
            preSum.append(preSum[-1]+nums[i])
        r = preSum[-1] % p    
        m, res = {}, n+1
        for i in range(n):
            if preSum[i]%p in m:
                res = min(res, i-m[preSum[i]%p]+1)
            m[preSum[i]%p] = i  
        return -1 if res == n+1 else res

    def minSubarray2(self, nums: List[int], p: int) -> int:
        # Then the question become:
        # Find the shortest array with sum % p = need.

        # last[remainder] = index records the last index that
        # (A[0] + A[1] + .. + A[i]) % p = remainder
        A = nums
        need = sum(A) % p
        dp = {0: -1}
        cur = 0
        res = n = len(A)
        for i, a in enumerate(A):
            cur = (cur + a) % p
            dp[cur] = i
            if (cur - need) % p in dp:
                res = min(res, i - dp[(cur - need) % p])
        return res if res < n else -1


if __name__ == "__main__":
    print(Solution().minSubarray(nums = [3,1,4,2], p = 6))