'''
-Hard-
*DP*

You are given a 0-indexed binary string floor, which represents the colors of 
tiles on a floor:

floor[i] = '0' denotes that the ith tile of the floor is colored black.
On the other hand, floor[i] = '1' denotes that the ith tile of the floor is 
colored white.
You are also given numCarpets and carpetLen. You have numCarpets black 
carpets, each of length carpetLen tiles. Cover the tiles with the given 
carpets such that the number of white tiles still visible is minimum. 
Carpets may overlap one another.

Return the minimum number of white tiles still visible.

 

Example 1:


Input: floor = "10110101", numCarpets = 2, carpetLen = 2
Output: 2
Explanation: 
The figure above shows one way of covering the tiles with the carpets such that only 2 white tiles are visible.
No other way of covering the tiles with the carpets can leave less than 2 white tiles visible.
Example 2:


Input: floor = "11111", numCarpets = 2, carpetLen = 3
Output: 0
Explanation: 
The figure above shows one way of covering the tiles with the carpets such that no white tiles are visible.
Note that the carpets are able to overlap one another.
 

Constraints:

1 <= carpetLen <= floor.length <= 1000
floor[i] is either '0' or '1'.
1 <= numCarpets <= 1000

'''
from functools import lru_cache

class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n, nc, l = len(floor), numCarpets, carpetLen
        dp = [[0]*(nc+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for k in range(nc+1):
                jump = dp[i-1][k] + (1 if floor[i-1] == '1' else 0)
                cover = dp[max(0, i-l)][k-1] if k > 0 else 1000
                dp[i][k] = min(jump, cover)
        return dp[n][nc]

    def minimumWhiteTiles2(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n, nc, l = len(floor), numCarpets, carpetLen
        dpk = [0 for _ in range(n+1)]
        dpk1 = [0 for _ in range(n+1)]
        #for i in range(1,n+1):
        for k in range(nc):
            for i in range(1,n+1):            
                jump = dpk[i-1] + (1 if floor[i-1] == '1' else 0)
                cover = dpk1[max(0, i-l)] if k > 0 else 1000
                dpk[i] = min(jump, cover)
            dpk1, dpk = dpk, dpk1
        return dpk1[n]

    def minimumWhiteTiles3(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        k = numCarpets
        L = carpetLen
        @lru_cache(None)
        def dp(i, t):
            if t < 0: return float("inf")
            if i < 0: return 0
            return min(dp(i - L, t - 1), dp(i - 1, t) + int(floor[i] == "1"))
        
        return dp(len(floor) - 1, k)


        

if __name__ == "__main__":
    print(Solution().minimumWhiteTiles(floor = "10110101", numCarpets = 2, carpetLen = 2))
    print(Solution().minimumWhiteTiles2(floor = "10110101", numCarpets = 2, carpetLen = 2))