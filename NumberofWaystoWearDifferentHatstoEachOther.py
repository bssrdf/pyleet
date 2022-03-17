'''

-Hard-
*DP*
*Bitmask*

There are n people and 40 types of hats labeled from 1 to 40.

Given a 2D integer array hats, where hats[i] is a list of all hats preferred 
by the ith person.

Return the number of ways that the n people wear different hats to each other.

Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: hats = [[3,4],[4,5],[5]]
Output: 1
Explanation: There is only one way to choose hats given the conditions. 
First person choose hat 3, Second person choose hat 4 and last one hat 5.
Example 2:

Input: hats = [[3,5,1],[3,5]]
Output: 4
Explanation: There are 4 ways to choose hats:
(3,5), (5,3), (1,3) and (1,5)
Example 3:

Input: hats = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
Output: 24
Explanation: Each person can choose hats labeled from 1 to 4.
Number of Permutations of (1,2,3,4) = 24.
 

Constraints:

n == hats.length
1 <= n <= 10
1 <= hats[i].length <= 40
1 <= hats[i][j] <= 40
hats[i] contains a list of unique integers.


'''

from functools import lru_cache
from typing import List

class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        n, mod = len(hats), 10**9+7
        allmask = (1 << n) - 1
        dp = [[-1 for i in range(2 ** n)] for j in range(41)]
        h2p = [[] for _ in range(41)] # h2p[i] indicates the list of people who can wear i_th hat
        for i in range(n):
            for h in hats[i]:
                h2p[h].append(i)
        #print(h2p)
        #@lru_cache(None)
        def dfs(hat, assignedPeople):
            if assignedPeople == allmask: return 1 # Check if assigned different hats to all people
            if hat > 40: return 0 #  no more hats to process
            if dp[hat][assignedPeople] != -1:
                return dp[hat][assignedPeople]
            ans = dfs(hat+1, assignedPeople) #  Don't wear this hat
            for p in h2p[hat]:
                #if assignedPeople & (1 << p) > 0: # Skip if person `p` was assigned hat
                if ((assignedPeople >> p) & 1) == 1: # Skip if person `p` was assigned hat
                    continue
                ans += dfs(hat+1, assignedPeople | (1 << p))
                ans %= mod
            dp[hat][assignedPeople] = ans
            return ans
        return dfs(1, 0)

if __name__ == "__main__":
    print(Solution().numberWays([[3,4],[4,5],[5]]))