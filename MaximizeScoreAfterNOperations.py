'''
-Hard-
*DP*
*Bitmask*

You are given nums, an array of positive integers of size 2 * n. You must perform 
n operations on this array.

In the ith operation (1-indexed), you will:

Choose two elements, x and y.
Receive a score of i * gcd(x, y).
Remove x and y from nums.
Return the maximum score you can receive after performing n operations.

The function gcd(x, y) is the greatest common divisor of x and y.

 

Example 1:

Input: nums = [1,2]
Output: 1
Explanation: The optimal choice of operations is:
(1 * gcd(1, 2)) = 1
Example 2:

Input: nums = [3,4,6,8]
Output: 11
Explanation: The optimal choice of operations is:
(1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
Example 3:

Input: nums = [1,2,3,4,5,6]
Output: 14
Explanation: The optimal choice of operations is:
(1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14
 

Constraints:

1 <= n <= 7
nums.length == 2 * n
1 <= nums[i] <= 106


'''


from typing import List
from functools import lru_cache
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        m = len(nums)
        n =  m // 2
        def gcd(a, b):
            while b != 0:
               r = a % b
               a, b = b, r
            return a
        gcds = {}
        for i in range(m):
            for j in range(i+1, m):
                g = gcd(nums[i], nums[j])
                gcds[(i, j)] = g
                gcds[(j, i)] = g
        @lru_cache(None)
        def dp(i, mask):
            if i == n+1: return 0
            ans = 0
            for j in range(m):
                newmask = mask
                if mask & (1<<j) == 0:
                    newmask |= 1 << j 
                    for k in range(j+1, m):
                        if mask & (1<<k) == 0:                  
                            newmask |= 1 << k 
                            ans = max(ans, i*gcds[(j,k)] + dp(i+1, newmask)) 
                            newmask &= ~(1<<k)
            return ans
        return dp(1, 0)

        

if __name__ == "__main__":
    print(Solution().maxScore([1,2]))
    print(Solution().maxScore([3,4,6,8]))
    print(Solution().maxScore([1,2,3,4,5,6]))
