'''

-Medium-
*DP*

You are given two positive integers startPos and endPos. Initially, you are standing at position startPos on an infinite number line. With one step, you can move either one position to the left, or one position to the right.

Given a positive integer k, return the number of different ways to reach the position endPos starting from startPos, such that you perform exactly k steps. Since the answer may be very large, return it modulo 109 + 7.

Two ways are considered different if the order of the steps made is not exactly the same.

Note that the number line includes negative integers.

 

Example 1:

Input: startPos = 1, endPos = 2, k = 3
Output: 3
Explanation: We can reach position 2 from 1 in exactly 3 steps in three ways:
- 1 -> 2 -> 3 -> 2.
- 1 -> 2 -> 1 -> 2.
- 1 -> 0 -> 1 -> 2.
It can be proven that no other way is possible, so we return 3.
Example 2:

Input: startPos = 2, endPos = 5, k = 10
Output: 0
Explanation: It is impossible to reach position 5 from position 2 in exactly 10 steps.
 

Constraints:

1 <= startPos, endPos, k <= 1000


'''

from functools import lru_cache
from math import comb

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10**9 + 7
        @lru_cache(None)
        def dfs(cur, steps):
            if abs(cur-endPos) > steps:
                return 0  
            if cur == endPos and steps == 0:
                return 1
            # if steps == 0:
            #     return 0
            ans = (dfs(cur-1, steps-1) + dfs(cur+1, steps-1)) % MOD
            return ans
        return dfs(startPos, k)
    
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        # Two sufficient and necessary conditions from a to b with k steps:

        # abs(a - b) <= k
        # (a - b - k) % 2 == 0
        # Otherwice no ways, directly return 0

        # Now two eqations
        # left + right = k
        # right - left = b - a

        # So we can have right = (b - a + k) / 2.
        # The combinations is to pick right steps from k steps to go right.
        # return result combination(k, right)

        a, b = startPos, endPos
        if (a - b - k) % 2: return 0
        return comb(k, (b - a + k) // 2) % (10 ** 9 + 7)    

if __name__ == "__main__":
    print(Solution().numberOfWays(startPos = 1, endPos = 2, k = 3))
    print(Solution().numberOfWays(startPos = 2, endPos = 5, k = 10))
    print(Solution().numberOfWays(startPos = 989, endPos = 1000, k = 99))