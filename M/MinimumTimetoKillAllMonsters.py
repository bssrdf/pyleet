'''

-Hard-
$$$

*DP*
*Bitmask*

You are given an integer array power where power[i] is the power of the ith monster.

You start with 0 mana points, and each day you increase your mana points by gain where gain initially is equal to 1.

Each day, after gaining gain mana, you can defeat a monster if your mana points are greater than or equal to the power of that monster. When you defeat a monster:

your mana points will be reset to 0, and
the value of gain increases by 1.
Return the minimum number of days needed to defeat all the monsters.

 

Example 1:

Input: power = [3,1,4]
Output: 4
Explanation: The optimal way to beat all the monsters is to:
- Day 1: Gain 1 mana point to get a total of 1 mana point. Spend all mana points to kill the 2nd monster.
- Day 2: Gain 2 mana points to get a total of 2 mana points.
- Day 3: Gain 2 mana points to get a total of 4 mana points. Spend all mana points to kill the 3rd monster.
- Day 4: Gain 3 mana points to get a total of 3 mana points. Spend all mana points to kill the 1st monster.
It can be proven that 4 is the minimum number of days needed. 
Example 2:

Input: power = [1,1,4]
Output: 4
Explanation: The optimal way to beat all the monsters is to:
- Day 1: Gain 1 mana point to get a total of 1 mana point. Spend all mana points to kill the 1st monster.
- Day 2: Gain 2 mana points to get a total of 2 mana points. Spend all mana points to kill the 2nd monster.
- Day 3: Gain 3 mana points to get a total of 3 mana points.
- Day 4: Gain 3 mana points to get a total of 6 mana points. Spend all mana points to kill the 3rd monster.
It can be proven that 4 is the minimum number of days needed. 
Example 3:

Input: power = [1,2,4,9]
Output: 6
Explanation: The optimal way to beat all the monsters is to:
- Day 1: Gain 1 mana point to get a total of 1 mana point. Spend all mana points to kill the 1st monster.
- Day 2: Gain 2 mana points to get a total of 2 mana points. Spend all mana points to kill the 2nd monster.
- Day 3: Gain 3 mana points to get a total of 3 mana points.
- Day 4: Gain 3 mana points to get a total of 6 mana points.
- Day 5: Gain 3 mana points to get a total of 9 mana points. Spend all mana points to kill the 4th monster.
- Day 6: Gain 4 mana points to get a total of 4 mana points. Spend all mana points to kill the 3rd monster.
It can be proven that 6 is the minimum number of days needed.
 

Constraints:

1 <= power.length <= 17
1 <= power[i] <= 109



'''
from typing import List
from functools import lru_cache
import math
class Solution:
    def minimumTime(self, power: List[int]) -> int:
        @lru_cache(None)
        def dfs(mask):
            gain = mask.bit_count() + 1 # initially gain is 1 when mask = 0
            if gain == len(power) + 1:
                return 0
            ans = math.inf
            for i, v in enumerate(power):
                if mask & (1 << i):
                    continue
                # to beat monster i, the required mana >= v
                # the number of days to gain this amount of mana is (v + gain - 1) // gain
                ans = min(ans, dfs(mask | 1 << i) + (v + gain - 1) // gain)
            return ans

        return dfs(0)

if __name__ == '__main__':   
    print(Solution().minimumTime(power = [3,1,4]))
    print(Solution().minimumTime(power = [1,2,4,9]))