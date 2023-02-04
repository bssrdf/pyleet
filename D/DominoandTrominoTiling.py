'''
-Medium-
*DP*

You have two types of tiles: a 2 x 1 domino shape and a tromino shape. 
You may rotate these shapes.


Given an integer n, return the number of ways to tile an 2 x n board. 
Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are 
different if and only if there are two 4-directionally adjacent cells 
on the board such that exactly one of the tilings has both squares 
occupied by a tile.

 

Example 1:


Input: n = 3
Output: 5
Explanation: The five different ways are show above.
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 1000

'''
class Solution:
    def numTilings(self, n: int) -> int:
        # Use dynamic programming. For N <= 2, the results are 
        # straightforward. If N equals 0 or 1, the result is 1 
        # (note that when N equals 0, no tile is needed, which 
        # counts for one way). If N equals 2, the result is 2.

        # For N >= 3, the board can be tiled by adding one vertical 
        # domino after N - 1 columns, which counts for one way, or 
        # adding two horizontal dominoes after N - 2 columns, 
        # which counts for one way, or adding two trominoes and 
        # several dominoes after N - k columns where 3 <= k <= N, 
        # which count for two ways for each k.

        # Let f(N) be the number of ways to tile a 2 x N board. 
        # It can be seen that f(0) = 1, f(1) = 1, f(2) = 2, and 
        # for N >= 3, f(N) = f(N - 1) + f(N - 2) + (f(0) + f(1) + … + f(N - 3)) * 2. 
        # Apply the same recurrence formula for f(N - 1), and it can be 
        # induced that for N >= 3, f(N) = f(N - 1) * 2 + f(N - 3). Apply 
        # this formula to obtain f(N).

        if n == 0:  return 1
        if n <= 2:  return n
        MODULO = 1000000007
        prev2, prev1, cur = 1, 1, 2
        for i in range(3, n+1):
            next = (cur * 2 % MODULO + prev2) % MODULO
            prev2 = prev1
            prev1 = cur
            cur = next
        return cur

    
if __name__ == "__main__":
    print(Solution().numTilings(3))
        
