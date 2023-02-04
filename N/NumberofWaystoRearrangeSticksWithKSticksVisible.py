'''
-Hard-

*DP*

There are n uniquely-sized sticks whose lengths are integers from 1 to n. You want to arrange the sticks such that exactly k sticks are visible from the left. A stick is visible from the left if there are no longer sticks to the left of it.

For example, if the sticks are arranged [1,3,2,5,4], then the sticks with lengths 1, 3, and 5 are visible from the left.
Given n and k, return the number of such arrangements. Since the answer may be large, return it modulo 109 + 7.

 

Example 1:

Input: n = 3, k = 2
Output: 3
Explanation: [1,3,2], [2,3,1], and [2,1,3] are the only arrangements such that exactly 2 sticks are visible.
The visible sticks are underlined.
Example 2:

Input: n = 5, k = 5
Output: 1
Explanation: [1,2,3,4,5] is the only arrangement such that all 5 sticks are visible.
The visible sticks are underlined.
Example 3:

Input: n = 20, k = 11
Output: 647427950
Explanation: There are 647427950 (mod 109 + 7) ways to rearrange the sticks such that exactly 11 sticks are visible.
 

Constraints:

1 <= n <= 1000
1 <= k <= n


'''


class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        dp = [[0]*(k+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1,n+1):
            for j in range(1,k+1):
                dp[i][j] = dp[i-1][j-1] # put the tallest on the bottom, so it is visible
                                        # the rest of i-1 sticks just need to have j-1 visible
                # if put any stick other than the tallest at the bottom, it will not be visible
                # there are i-1 such sticks; from the rest, we need to have j visible 
                dp[i][j] = (dp[i][j] + (i-1)*dp[i-1][j]) % mod 
        return dp[n][k]        






if __name__ == "__main__":
    print(Solution().rearrangeSticks(n = 3, k = 2))
    print(Solution().rearrangeSticks(n = 5, k = 5))
    print(Solution().rearrangeSticks(n = 20, k = 11))
        