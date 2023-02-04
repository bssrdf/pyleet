'''
-Hard-

You are given an integer n. You roll a fair 6-sided dice n times. Determine the total number of distinct sequences of rolls possible such that the following conditions are satisfied:

The greatest common divisor of any adjacent values in the sequence is equal to 1.
There is at least a gap of 2 rolls between equal valued rolls. More formally, if the value of the ith roll is equal to the value of the jth roll, then abs(i - j) > 2.
Return the total number of distinct sequences possible. Since the answer may be very large, return it modulo 109 + 7.

Two sequences are considered distinct if at least one element is different.

 

Example 1:

Input: n = 4
Output: 184
Explanation: Some of the possible sequences are (1, 2, 3, 4), (6, 1, 2, 3), (1, 2, 3, 1), etc.
Some invalid sequences are (1, 2, 1, 3), (1, 2, 3, 6).
(1, 2, 1, 3) is invalid since the first and third roll have an equal value and abs(1 - 3) = 2 (i and j are 1-indexed).
(1, 2, 3, 6) is invalid since the greatest common divisor of 3 and 6 = 3.
There are a total of 184 distinct sequences possible, so we return 184.
Example 2:

Input: n = 2
Output: 22
Explanation: Some of the possible sequences are (1, 2), (2, 1), (3, 2).
Some invalid sequences are (3, 6), (2, 4) since the greatest common divisor is not equal to 1.
There are a total of 22 distinct sequences possible, so we return 22.
 

Constraints:

1 <= n <= 104

'''
from functools import cache


class Solution:
    def distinctSequences(self, n: int) -> int:
        m = [[1,2,3,4,5,6], 
         [2,3,4,5,6],
         [1,3,5],
         [1,2,4,5],
         [1,3,5],
         [1,2,3,4,6],
         [1,5]]
        mod = (10 ** 9) + 7
        @cache
        def dp(prev, pprev, n):
            if n == 0: return 1
            return sum(dp(x, prev, n - 1) for x in m[prev] if pprev != x) % mod
        return dp(0, 0, n)

    def distinctSequences2(self, n: int) -> int:
        mod = 10**9 + 7
        dp = [[0, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 1, 0, 1, 1, 0],
              [1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 0, 1], [1, 0, 0, 0, 1, 0]]
        dp1 = [[0]*6 for _ in range(6)]
        if n == 1:  return 6
        for i in range(3, n+1):
            for d in range(6):
                for p in range(6):
                    dp1[d][p] = 0
                    if dp[d][p] > 0: # if d != p and gcd(d,p) = 1
                        for pp in range(6):
                            if d != pp: #if d != pp
                                dp1[d][p] = (dp1[d][p] + dp[p][pp]) % mod
            dp, dp1 = dp1, dp
        res = 0
        for d in range(6):
            for p in range(6):
                res = (res + dp[d][p]) % mod
        return res
                   
       

if __name__ == "__main__":
    print(Solution().distinctSequences(4))
    print(Solution().distinctSequences2(4))

