'''

-Medium-

You are given two identical eggs and you have access to a building with n floors labeled from 1 to n.

You know that there exists a floor f where 0 <= f <= n such that any egg dropped at a floor higher than 
f will break, and any egg dropped at or below floor f will not break.

In each move, you may take an unbroken egg and drop it from any floor x (where 1 <= x <= n). If the egg 
breaks, you can no longer use it. However, if the egg does not break, you may reuse it in future moves.

Return the minimum number of moves that you need to determine with certainty what the value of f is.

 

Example 1:

Input: n = 2
Output: 2
Explanation: We can drop the first egg from floor 1 and the second egg from floor 2.
If the first egg breaks, we know that f = 0.
If the second egg breaks but the first egg didn't, we know that f = 1.
Otherwise, if both eggs survive, we know that f = 2.
Example 2:

Input: n = 100
Output: 14
Explanation: One optimal strategy is:
- Drop the 1st egg at floor 9. If it breaks, we know f is between 0 and 8. Drop the 2nd egg starting
  from floor 1 and going up one at a time to find f within 7 more drops. Total drops is 1 + 7 = 8.
- If the 1st egg does not break, drop the 1st egg again at floor 22. If it breaks, we know f is between 9
  and 21. Drop the 2nd egg starting from floor 10 and going up one at a time to find f within 12 more
  drops. Total drops is 2 + 12 = 14.
- If the 1st egg does not break again, follow a similar process dropping the 1st egg from floors 34, 45,
  55, 64, 72, 79, 85, 90, 94, 97, 99, and 100.
Regardless of the outcome, it takes at most 14 drops to determine f.


'''
from functools import lru_cache

class Solution(object):
      
    @lru_cache(None)
    def twoEggDrop(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        imple Recursion
        In the solution below, we drop an egg from each floor and find the number of throws for these two cases:

        We lost an egg but we reduced the number of floors to i.
        Since we only have one egg left, we can just return i - 1 to check all floors.
        The egg did not break, and we reduced the number of floors to n - i.
        Solve this recursively to get the number of throws for n - i floors.
        This way, we find a floor for which the number of throws - maximum from these two cases - is minimal.
        """
        return min((1 + max(i - 1, self.twoEggDrop(n - i)) for i in range (1, n)), default = 1)

    def twoEggDropDP(self, n):
        def twoEggDropGeneralize(n, k=2):
            dp = [0]*(k+1)
            m = 0
            while dp[k] < n: 
                m += 1
                for j in range(k, 0, -1):
                    dp[j] += dp[j - 1] + 1
            return m
        return twoEggDropGeneralize(n, 2)

if __name__ == "__main__":
    print(Solution().twoEggDrop(100))
    print(Solution().twoEggDropDP(100))

