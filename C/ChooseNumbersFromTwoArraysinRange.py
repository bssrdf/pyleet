'''

-Hard-
$$$

*DP*
*Hash Table*

You are given two 0-indexed integer arrays nums1 and nums2 of length n.

A range [l, r] (inclusive) where 0 <= l <= r < n is balanced if:

For every i in the range [l, r], you pick either nums1[i] or nums2[i].
The sum of the numbers you pick from nums1 equals to the sum of the numbers you pick from nums2 (the sum is considered to be 0 if you pick no numbers from an array).
Two balanced ranges from [l1, r1] and [l2, r2] are considered to be different if at least one of the following is true:

l1 != l2
r1 != r2
nums1[i] is picked in the first range, and nums2[i] is picked in the second range or vice versa for at least one i.
Return the number of different ranges that are balanced. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: nums1 = [1,2,5], nums2 = [2,6,3]
Output: 3
Explanation: The balanced ranges are:
- [0, 1] where we choose nums2[0], and nums1[1].
  The sum of the numbers chosen from nums1 equals the sum of the numbers chosen from nums2: 2 = 2.
- [0, 2] where we choose nums1[0], nums2[1], and nums1[2].
  The sum of the numbers chosen from nums1 equals the sum of the numbers chosen from nums2: 1 + 5 = 6.
- [0, 2] where we choose nums1[0], nums1[1], and nums2[2].
  The sum of the numbers chosen from nums1 equals the sum of the numbers chosen from nums2: 1 + 2 = 3.
Note that the second and third balanced ranges are different.
In the second balanced range, we choose nums2[1] and in the third balanced range, we choose nums1[1].
Example 2:

Input: nums1 = [0,1], nums2 = [1,0]
Output: 4
Explanation: The balanced ranges are:
- [0, 0] where we choose nums1[0].
  The sum of the numbers chosen from nums1 equals the sum of the numbers chosen from nums2: 0 = 0.
- [1, 1] where we choose nums2[1].
  The sum of the numbers chosen from nums1 equals the sum of the numbers chosen from nums2: 0 = 0.
- [0, 1] where we choose nums1[0] and nums2[1].
  The sum of the numbers chosen from nums1 equals the sum of the numbers chosen from nums2: 0 = 0.
- [0, 1] where we choose nums2[0] and nums1[1].
  The sum of the numbers chosen from nums1 equals the sum of the numbers chosen from nums2: 1 = 1.
 

Constraints:

n == nums1.length == nums2.length
1 <= n <= 100
0 <= nums1[i], nums2[i] <= 100





'''

from typing import List
from collections import Counter

class Solution:
    def countSubranges(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        offset, MOD = 10000, 10**9 + 7
        nums1 = [0] + nums1
        nums2 = [0] + nums2
        dp = [[0]*(20005) for _ in range(n+1)]
        dp[1][0+offset] = 0
        ret = 0
        def inbound(x):
            return x <= offset and x >= -offset
        for i in range(1, n+1):
            dp[i][offset+nums1[i]] += 1
            dp[i][offset-nums2[i]] += 1
            for sm in range(-offset, offset+1):
                if inbound(sm-nums1[i]):
                    dp[i][sm+offset] += dp[i-1][sm+offset-nums1[i]]
                    dp[i][sm+offset] %= MOD
                if inbound(sm+nums2[i]):
                    dp[i][sm+offset] += dp[i-1][sm+offset+nums2[i]]
                    dp[i][sm+offset] %= MOD    
            ret = (ret + dp[i][0+offset]) % MOD
        return ret
    
    def countSubranges2(self, nums1: List[int], nums2: List[int]) -> int:
        ans, MOD = 0, 10**9 + 7
        # {sum, count}, add if choose from nums1, minus if choose from nums2
        dp = Counter()

        for a, b in zip(nums1, nums2):
            newDp = Counter()
            newDp[a]  += 1
            newDp[-b] += 1

            for prevSum, count in dp.items():
                # choose nums1[i]
                newDp[prevSum + a] += count
                newDp[prevSum + a] %= MOD
                # choose nums2[i]
                newDp[prevSum - b] += count
                newDp[prevSum - b] %= MOD

            dp = newDp
            ans += dp[0]
            ans %= MOD

        return ans

    
if __name__ == "__main__":
    print(Solution().countSubranges(nums1 = [1,2,5], nums2 = [2,6,3]))
    print(Solution().countSubranges2(nums1 = [1,2,5], nums2 = [2,6,3]))


