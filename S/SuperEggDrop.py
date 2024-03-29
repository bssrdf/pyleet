'''

-Hard-
*DP*
*Binary Search*

You are given K eggs, and you have access to a building with N floors from 
1 to N. 

Each egg is identical in function, and if an egg breaks, you cannot drop it 
again.

You know that there exists a floor F with 0 <= F <= N such that any egg 
dropped at a floor higher than F will break, and any egg dropped at or 
below floor F will not break.

Each move, you may take an egg (if you have an unbroken one) and drop it 
from any floor X (with 1 <= X <= N). 

Your goal is to know with certainty what the value of F is.

What is the minimum number of moves that you need to know with certainty 
what F is, regardless of the initial value of F?

 

Example 1:

Input: K = 1, N = 2
Output: 2
Explanation: 
Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty 
that F = 1.
If it didn't break, then we know with certainty F = 2.
Hence, we needed 2 moves in the worst case to know what F is with certainty.
Example 2:

Input: K = 2, N = 6
Output: 3
Example 3:

Input: K = 3, N = 14
Output: 4
 

Note:

1 <= K <= 100
1 <= N <= 10000

'''

class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        """
        定义 dp[k][m] 代表 K 个鸡蛋，M 次移动能检查的最大楼层。考虑某一步 t 应该在哪
        一层丢鸡蛋呢？一个正确的选择是在 dp[k-1][t-1] + 1 层丢鸡蛋，
        结果分两种情况：

        如果鸡蛋碎了，我们首先排除了该层以上的所有楼层（不管这个楼有多高），而对于剩下
        的 dp[k-1][t-1] 层楼，我们一定能用 k-1 个鸡蛋在 t-1 步内求解。因此这种情况下，
        我们总共可以求解无限高的楼层。可见，这是一种非常好的情况，但并不总是发生。

        如果鸡蛋没碎，我们首先排除了该层以下的 dp[k-1][t-1] 层楼，此时我们还有 k 个蛋
        和 t-1 步，那么我们去该层以上的楼层继续测得 dp[k][t-1] 层楼。因此这种情况下，
        我们总共可以求解 dp[k-1][t-1] + 1 + dp[k][t-1] 层楼。

        在所有 m 步中只要有一次出现了第一种情况，那么我们就可以求解无限高的楼层。但题目
        要求我们能保证一定能找到安全楼层，所以每次丢鸡蛋的情况应该按照最差情况来，即每次
        都是第二种情况。于是得到转状态转移方程: 
           dp[k][m] = dp[k-1][m-1] + dp[k][m-1] + 1 。这个方程可以压缩到一维，因为
        每个新的状态只和上一行和左一列有关。那么每一行从右往左更新，即 
            dp[i] += 1 + dp[i-1]。时间复杂度 O(K * log N)，空间复杂度 O(N)。
        可能会有人有疑问，如果最初选择不在 dp[k-1][t-1] + 1 层丢鸡蛋会怎么样呢？选择在
        更低的层或者更高的层丢鸡蛋会怎样呢？
        如果在更低的楼层丢鸡蛋也能保证找到安全楼层。那么得到的结果一定不是最小步数。因为
        这次丢鸡蛋没有充分的展现鸡蛋和移动次数的潜力，最终求解一定会有鸡蛋和步数剩余，
        即不是能探测的最大楼层了。
        如果在更高的楼层丢鸡蛋，假设是第 dp[k-1][t-1] + 2 层丢鸡蛋，如果这次鸡蛋碎了，
        剩下 k-1 个鸡蛋和 t-1 步只能保证验证 dp[k-1][t-1] 的楼层，这里还剩第 
        dp[k-1][t-1]+ 1 的楼层，不能保证最终一定能找到安全楼层了。
        用反证法就能得出每一步都应该在第 dp[k-1][t-1] + 1 层丢鸡蛋。
        
        """

        """
        Inversion and Generic Solution

        With the help of the iterative solution above, we see that it's easier to solve an inverse problem: 
        
        given m total drops, and k eggs, how high can we go?

        So with one egg and m drops, we can only test m floors.

        With two eggs and m drops:

        We drop one egg to test one floor.
        We add the number of floors we can test with m - 1 drops and 2 eggs (the egg did not break).
        And we add m - 1 floors we can test with the last egg (the egg broke).
        Thus, the formula is:

        dp[m] = 1 + dp[m - 1] + m - 1;
        ... which is in-line with the observation we made for the iterative solution above!

        This can be easily generalized for k eggs:

        dp[m][k] = 1 + dp[m - 1][k] + dp[m - 1][k - 1];
        
        """
        dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
        m = 0
        while dp[m][K] < N: 
            m += 1
            for j in range(1, K+1):
                dp[m][j] = dp[m - 1][j - 1] + dp[m - 1][j] + 1
        return m

if __name__ == "__main__":
    print(Solution().superEggDrop(3,14))