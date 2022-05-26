'''


-Hard-
*DP*
*Bitmask*
*Memoization*

You are given two integers m and n. Consider an m x n grid where each cell is initially white. You can paint each cell red, green, or blue. All cells must be painted.

Return the number of ways to color the grid with no two adjacent cells having the same color. Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:


Input: m = 1, n = 1
Output: 3
Explanation: The three possible colorings are shown in the image above.
Example 2:


Input: m = 1, n = 2
Output: 6
Explanation: The six possible colorings are shown in the image above.
Example 3:

Input: m = 5, n = 5
Output: 580986
 

Constraints:

1 <= m <= 5
1 <= n <= 1000


'''
from functools import lru_cache
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        # wrong solution
        MOD = 10**9 + 7
        dp = [[[0]*3 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1 and j == 1:
                    dp[i][j][0] = 1
                    dp[i][j][1] = 1
                    dp[i][j][2] = 1
                else:
                    dp[i][j][0] = dp[i-1][j][1] + dp[i-1][j][2] + dp[i][j-1][1] + dp[i][j-1][2]
                    dp[i][j][1] = dp[i-1][j][0] + dp[i-1][j][2] + dp[i][j-1][0] + dp[i][j-1][2]
                    dp[i][j][2] = dp[i-1][j][0] + dp[i-1][j][1] + dp[i][j-1][0] + dp[i][j-1][1]
        return sum(dp[m][n])

    def colorTheGrid2(self, m: int, n: int) -> int:
        def getColor(mask, pos):  # Get color of the `mask` at `pos`, use 2 bits to store a color
            return (mask >> (2 * pos)) & 3
        
        def setColor(mask, pos, color):  # Set `color` to the `mask` at `pos`, use 2 bits to store a color
            return mask | (color << (2 * pos))

        def dfs(r, curColMask, prevColMask, out):
            if r == m:  # Filled full color for this column
                out.append(curColMask)
                return
            for i in [1, 2, 3]:  # Try colors i in [1=RED, 2=GREEN, 3=BLUE]
                if getColor(prevColMask, r) != i and (r == 0 or getColor(curColMask, r - 1) != i):
                    dfs(r + 1, setColor(curColMask, r, i), prevColMask, out)

        @lru_cache(None)
        def neighbor(prevColMask):  # Generate all possible columns we can draw, if the previous col is `prevColMask`
            out = []
            dfs(0, 0, prevColMask, out)
            return out

        @lru_cache(None)
        def dp(c, prevColMask):
            if c == n: return 1  # Found a valid way
            ans = 0
            for nei in neighbor(prevColMask):
                ans = (ans + dp(c + 1, nei)) % 1_000_000_007
            return ans

        return dp(0, 0)

    
    def colorTheGrid3(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        cand = []
        for state in range(pow(3,m)):
            temp = []
            state0 = state
            flag = True
            for i in range(m):
                color = state0 % 3
                if temp and temp[-1] == color:
                    flag = False
                    break
                temp.append(color)
                state0 //= 3
            if flag:
                cand.append(state)
        k = len(cand)
        dp = [1]*k
        def checkOK(s, t, m):
            for i in range(m):
                if s % 3 == t % 3:
                    return False
                s //= 3
                t //= 3
            return True

        for j in range(1,n):
            dp2 = [0]*k 
            for s in range(k):
                for t in range(k):
                    if checkOK(cand[s], cand[t], m):
                        dp2[s] = (dp2[s] + dp[t]) % MOD
            dp = dp2
        res = 0
        for s in range(k):
            res = (res + dp[s]) % MOD
        return res


if __name__ == "__main__":
    # print(Solution().colorTheGrid(m = 1, n = 1))
    # print(Solution().colorTheGrid(m = 1, n = 2))
    # print(Solution().colorTheGrid(m = 2, n = 2))
    print(Solution().colorTheGrid2(m = 2, n = 2))
    print(Solution().colorTheGrid2(m = 1, n = 3))
    print(Solution().colorTheGrid2(m = 5, n = 5))
    print(Solution().colorTheGrid3(m = 2, n = 2))
    print(Solution().colorTheGrid3(m = 1, n = 3))
    print(Solution().colorTheGrid3(m = 5, n = 5))


