'''

-Hard-
$$$

*DP*
*Sliding Window*
*Monototic Queue*

You are at a fruit market with different types of exotic fruits on display.

You are given a 1-indexed array prices, where prices[i] denotes the number of coins needed to purchase the ith fruit.

The fruit market has the following offer:

If you purchase the ith fruit at prices[i] coins, you can get the next i fruits for free.
Note that even if you can take fruit j for free, you can still purchase it for prices[j] coins to receive a new offer.

Return the minimum number of coins needed to acquire all the fruits.

 

Example 1:

Input: prices = [3,1,2]
Output: 4
Explanation: You can acquire the fruits as follows:
- Purchase the 1st fruit with 3 coins, and you are allowed to take the 2nd fruit for free.
- Purchase the 2nd fruit with 1 coin, and you are allowed to take the 3rd fruit for free.
- Take the 3rd fruit for free.
Note that even though you were allowed to take the 2nd fruit for free, you purchased it because it is more optimal.
It can be proven that 4 is the minimum number of coins needed to acquire all the fruits.
Example 2:

Input: prices = [1,10,1,1]
Output: 2
Explanation: You can acquire the fruits as follows:
- Purchase the 1st fruit with 1 coin, and you are allowed to take the 2nd fruit for free.
- Take the 2nd fruit for free.
- Purchase the 3rd fruit for 1 coin, and you are allowed to take the 4th fruit for free.
- Take the 4th fruit for free.
It can be proven that 2 is the minimum number of coins needed to acquire all the fruits.
 

Constraints:

1 <= prices.length <= 105
1 <= prices[i] <= 105


'''

from typing import List
from math import inf
from collections import deque
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [inf]*(n+1)
        # Let dp[i] denote the minimum number of coins, 
        # such that we bought ith fruit and acquired all 
        # the fruits in the range [i...n].
        # the answer is dp[0] because you must pay for prices[0]
        dp[-1] = 0
        for i in range(n-1,-1,-1):
            k = 2*i+3             
            # for j in range(i+1, i+1+i+1+1):
            for j in range(i+1, k):
                dp[i] = min(dp[i], prices[i] + (dp[j] if j <= n else 0) )
        # print(dp)
        return dp[0]    

    def minimumCoins2(self, prices: List[int]) -> int:
        # We define $f[i]$ as the minimum number of coins needed to buy all fruits starting from 
        # the $i$th fruit. So the answer is $f[1]$.

        # The state transition equation is $f[i] = \min_{i + 1 \le j \le 2i + 1} f[j] + prices[i - 1]$.

        # In implementation, we calculate from back to front, and we can directly perform state transition 
        # on the array $prices$, which can save space.

        # The time complexity of the above method is $O(n^2)$. Since the scale of $n$ in this problem 
        # reaches $10^5$, it will time out.

        # We observe the state transition equation and find that for each $i$, we need to find 
        # the minimum value of $f[i + 1], f[i + 2], \cdots, f[2i + 1]$, and as $i$ decreases, the 
        # range of these values is also decreasing. This is actually finding the minimum value of 
        # a monotonically narrowing sliding window, and we can use a monotonic queue to optimize.

        # We calculate from back to front, maintain a monotonically increasing queue $q$, and the 
        # queue stores the index. If the head element of $q$ is greater than $i \times 2 + 1$, it 
        # means that the elements after $i$ will not be used, so we dequeue the head element. If $i$ is 
        # not greater than $(n - 1) / 2$, then we can add $prices[q[0] - 1]$ to $prices[i - 1]$. If the 
        # price of the fruit corresponding to the tail 
        # element of $q$ is greater than or equal to $prices[i - 1]$, then we dequeue the tail 
        # element until the price of the fruit corresponding to the tail element is less 
        # than $prices[i - 1]$ or the queue is empty, and then add $i$ to the tail of the queue.

        # The time complexity is $O(n)$, and the space complexity is $O(n)$. Where $n$ is the 
        # length of the array $prices$.

        n = len(prices)
        q = deque()
        for i in range(n, 0, -1):
            while q and q[0] > i * 2 + 1:
                q.popleft()
            if i <= (n - 1) // 2:
                prices[i - 1] += prices[q[0] - 1]
            while q and prices[q[-1] - 1] >= prices[i - 1]:
                q.pop()
            q.append(i)
        return prices[0]



if __name__ == "__main__":
    print(Solution().minimumCoins(prices = [3,1,2]))
    print(Solution().minimumCoins(prices = [1,10,1,1]))
    print(Solution().minimumCoins(prices = [26,18,6,12,49,7,45,45]))