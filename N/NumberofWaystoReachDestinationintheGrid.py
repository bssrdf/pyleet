'''

-Hard-
$$$

You are given two integers n and m which represent the size of a 1-indexed grid. You are also given an integer k, a 1-indexed integer array source and a 1-indexed integer array dest, where source and dest are in the form [x, y] representing a cell on the given grid.

You can move through the grid in the following way:

You can go from cell [x1, y1] to cell [x2, y2] if either x1 == x2 or y1 == y2.
Note that you can't move to the cell you are already in e.g. x1 == x2 and y1 == y2.
Return the number of ways you can reach dest from source by moving through the grid exactly k times.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: n = 3, m = 2, k = 2, source = [1,1], dest = [2,2]
Output: 2
Explanation: There are 2 possible sequences of reaching [2,2] from [1,1]:
- [1,1] -> [1,2] -> [2,2]
- [1,1] -> [2,1] -> [2,2]
Example 2:

Input: n = 3, m = 4, k = 3, source = [1,2], dest = [2,3]
Output: 9
Explanation: There are 9 possible sequences of reaching [2,3] from [1,2]:
- [1,2] -> [1,1] -> [1,3] -> [2,3]
- [1,2] -> [1,1] -> [2,1] -> [2,3]
- [1,2] -> [1,3] -> [3,3] -> [2,3]
- [1,2] -> [1,4] -> [1,3] -> [2,3]
- [1,2] -> [1,4] -> [2,4] -> [2,3]
- [1,2] -> [2,2] -> [2,1] -> [2,3]
- [1,2] -> [2,2] -> [2,4] -> [2,3]
- [1,2] -> [3,2] -> [2,2] -> [2,3]
- [1,2] -> [3,2] -> [3,3] -> [2,3]
 

Constraints:

2 <= n, m <= 109
1 <= k <= 105
source.length == dest.length == 2
1 <= source[1], dest[1] <= n
1 <= source[2], dest[2] <= m



'''
from typing import List

class Solution:
    def numberofWays(self, n: int , m : int, k : int, source : List[int], dest:  List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2900-2999/2912.Number%20of%20Ways%20to%20Reach%20Destination%20in%20the%20Grid
        mod = 10**9 + 7
        # a represents the number of ways to move from source to source itself;
        # b represents the number of ways to move from source to another row in the same column;
        # c represents the number of ways to move from source to another column in the same row;
        # d represents the number of ways to move from source to another row and another column.
        # Initially, a = 1 and the other states are all 
        a, b, c, d = 1, 0, 0, 0
        for i in range(k):
            # For each state, we can calculate the current state based on the previous state, as follows:        
            aa = ((n - 1) * b + (m - 1) * c) % mod
            bb = (a + (n - 2) * b + (m - 1) * d) % mod
            cc = (a + (m - 2) * c + (n - 1) * d) % mod
            dd = (b + c + (n - 2) * d + (m - 2) * d) % mod
            a, b, c, d = aa, bb, cc, dd
            print(i,a,b,c,d)
        if source[0] == dest[0]:
            return a if source[1] == dest[1] else c
        return b if source[1] == dest[1] else d


if __name__ == "__main__":
    # print(Solution().numberofWays(n = 3, m = 2, k = 2, source = [1,1], dest = [2,2]))
    print(Solution().numberofWays(n = 3, m = 4, k = 3, source = [1,2], dest = [2,3]))