'''

-Medium-
*Greedy*

You are given an integer array coins of length n which represents the n coins that you own. The value of the ith coin is coins[i]. You can make some value x if you can choose some of your n coins such that their values sum up to x.

Return the maximum number of consecutive integer values that you can make with your coins starting from and including 0.

Note that you may have multiple coins of the same value.

 

Example 1:

Input: coins = [1,3]
Output: 2
Explanation: You can make the following values:
- 0: take []
- 1: take [1]
You can make 2 consecutive integer values starting from 0.
Example 2:

Input: coins = [1,1,1,4]
Output: 8
Explanation: You can make the following values:
- 0: take []
- 1: take [1]
- 2: take [1,1]
- 3: take [1,1,1]
- 4: take [4]
- 5: take [4,1]
- 6: take [4,1,1]
- 7: take [4,1,1,1]
You can make 8 consecutive integer values starting from 0.
Example 3:

Input: nums = [1,4,10,3,1]
Output: 20
 

Constraints:

coins.length == n
1 <= n <= 4 * 104
1 <= coins[i] <= 4 * 104


'''
from typing import List

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        res = 1 # res means the next value we want to make,
                # and we can already make 0,1,2,3...res-1.
        for a in sorted(coins):
            if a > res: break # res can not be made by 'a'
            # If a <= res, we could make from 0 to res - 1,
            # now with 'a', we can make from a to res + a - 1,
            # and a <= res, so our next goal becomes res + a now.
            # so in this case, we simply res += a
            res += a  
        return res

        

if __name__ == "__main__":
    print(Solution().getMaximumConsecutive(coins = [1,1,1,4]))