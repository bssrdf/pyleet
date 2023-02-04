'''

-Medium-


In combinatorial mathematics, a derangement is a permutation of the elements of a set, such that no element appears in its original position.

There's originally an array consisting of n integers from 1 to n in ascending order, you need to find the number of derangement it can generate.

Also, since the answer may be very large, you should return the output mod 10^9 + 7.

n is in the range of [1, 10^6][1,10 
6
 ].

样例
Example 1:

Input: 3
Output: 2
Explanation: 
  The original array is [1,2,3]. 
  The two derangements are [2,3,1] and [3,1,2].
Example 2:

Input: 2
Output: 1

'''

class Solution:
    """
    @param n: an array consisting of n integers from 1 to n
    @return: the number of derangement it can generate
    """
    def findDerangement(self, n):
        # Write your code here
        if n <= 3: return n - 1
        MODULO = 1000000007
        dp = [0]*n
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n):
            dp[i] = (dp[i - 2] + dp[i - 1]) * i % MODULO
        return dp[n - 1]
    
    def findDerangementO1Space(self, n):
        # Write your code here
        #Let f(n) be the number of derangement that can be generated using n integers. 
        # Obviously, f(1) = 0 and f(2) = 1. For n > 2, how to calculate f(n)?

        #Use dynamic programming, where f(n) can be obtained using f(n - 1) and f(n - 2). 
        # If there are n numbers, then the greatest number n can be placed in any 
        # position from 1 to n - 1. Suppose number n is placed in position m 
        # where 1 <= m < n, then number m must be in a position that is not 
        # its original position. If number m is in position n, then the situation 
        # becomes a derangement of n - 2 remaining numbers, so the number of 
        # derangement is f(n - 2). If number m is not in position n, then for 
        # each number from 1 to n - 1, there is exactly one position that the 
        # number can’t be in. For number m, the one position it can’t be in is 
        # position n. For other numbers like number k where k != m and k < n, 
        # the one position it can’t be in is position k. So the number of derangement 
        # is f(n - 1). In conclusion, if there are n numbers and number n is 
        # placed in position m where 1 <= m < n, then the number of derangement 
        # is f(n - 2) + f(n - 1). Since there are n - 1 possible values for m, 
        # the number of derangement in total is f(n) = (f(n - 2) + f(n - 1)) * (n - 1).

        #For each m such that 1 <= m <= n, after f(m) is calculated, do the 
        # modulo operation. Finally, return f(n).

        # 设定状态: f[i] 表示含i个元素的排列能生成的错乱的数量

        # 状态转移方程: f[i] = (i - 1) * (f[i-1] + f[i-2])

        # 边界: f[1] = 0, f[2] = 1

        # 对于 f[n] 的计算, 假定把 n 放到了第 k 个位置:

        # 这时如果把 k 放到了第 n 个位置, 那么剩下的 n-2 个元素的错乱即为 f[n-2]
        # 如果把 k 放到了其他位置, 也就是说 k 不能放到 n, 与 n-1 个元素的错乱中 "k不能放到k" 
        # 是等价的, 也就是说, 这时是 f[n-1]
        # k一共有 n-1 个选择, 故 f[n] = (i - 1) * (f[n-1] + f[n-2])
        if n <= 3: return n - 1
        MODULO = 1000000007
        dp0 = 0
        dp1 = 1
        for i in range(2, n):
            dp = (dp0 + dp1) * i % MODULO
            dp0, dp1 = dp1, dp
        return dp1


if __name__ == "__main__":
    print(Solution().findDerangement(3))
    print(Solution().findDerangement(10))
    print(Solution().findDerangementO1Space(10))