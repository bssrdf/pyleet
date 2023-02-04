'''
-Hard-
*DP*
*BFS*

There are n oranges in the kitchen and you decided to eat some of these oranges every day as follows:

Eat one orange.
If the number of remaining oranges n is divisible by 2 then you can eat n / 2 oranges.
If the number of remaining oranges n is divisible by 3 then you can eat 2 * (n / 3) oranges.
You can only choose one of the actions per day.

Given the integer n, return the minimum number of days to eat n oranges.

 

Example 1:

Input: n = 10
Output: 4
Explanation: You have 10 oranges.
Day 1: Eat 1 orange,  10 - 1 = 9.  
Day 2: Eat 6 oranges, 9 - 2*(9/3) = 9 - 6 = 3. (Since 9 is divisible by 3)
Day 3: Eat 2 oranges, 3 - 2*(3/3) = 3 - 2 = 1. 
Day 4: Eat the last orange  1 - 1  = 0.
You need at least 4 days to eat the 10 oranges.
Example 2:

Input: n = 6
Output: 3
Explanation: You have 6 oranges.
Day 1: Eat 3 oranges, 6 - 6/2 = 6 - 3 = 3. (Since 6 is divisible by 2).
Day 2: Eat 2 oranges, 3 - 2*(3/3) = 3 - 2 = 1. (Since 3 is divisible by 3)
Day 3: Eat the last orange  1 - 1  = 0.
You need at least 3 days to eat the 6 oranges.
 

Constraints:

1 <= n <= 2 * 109


'''
from functools import lru_cache

class Solution:
    def minDays(self, n: int) -> int:
        @lru_cache(None)
        def dp(i):
            if i <= 1: return i
            # if i == 1: return 1
            return 1+min((i%2)+dp(i//2), (i%3)+dp(i//3)) # 1 is for the day you eat n/2 or 2n/3 apples
        return dp(n)
    
    def minDays2(self, n: int) -> int:
        ans = 0
        queue = [n]
        seen = set()
        while queue: #bfs 
            newq = []
            for x in queue: 
                if x == 0: return ans 
                seen.add(x)
                if x-1 not in seen: newq.append(x-1)
                if x % 2 == 0 and x//2 not in seen: newq.append(x//2)
                if x % 3 == 0 and x//3 not in seen: newq.append(x//3)
            ans += 1
            queue = newq 

            





if __name__ == "__main__":
    print(Solution().minDays(10))
    print(Solution().minDays(6))
    print(Solution().minDays(10**6))

        