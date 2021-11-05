'''
-Medium-
*DP*

Imagine you have a special keyboard with the following keys:

Key 1: (A): Print one 'A' on screen.

Key 2: (Ctrl-A): Select the whole screen.

Key 3: (Ctrl-C): Copy selection to buffer.

Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.

Now, you can only press the keyboard for N times (with the above four keys), 
find out the maximum numbers of 'A' you can print on screen.

Example 1:
Input: N = 3
Output: 3
Explanation:
We can at most get 3 A's on screen by pressing following key sequence:
A, A, A
Example 2:
Input: N = 7
Output: 9
Explanation:
We can at most get 9 A's on screen by pressing following key sequence:
A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
Note:
1 <= N <= 50
Answers will be in the range of 32-bit signed integer.


'''

class Solution:
    """
    @param N: an integer
    @return: return an integer
    """
    def maxA(self, N):
        # write your code here
        res = N
        # number of printing A is between [1, N-3],
        # the number of pasting is N-2-i,
        # plus the printed part, it is N-1-i
        for i in range(1,  N - 2):
            res = max(res, self.maxA(i) * (N - 1 - i))
        return res

    def maxADP(self, N):
        # This problem can also be done with DP. We use a one-dimensional 
        # array dp, where dp[i] represents the maximum number of A that 
        # can be printed when the total number of steps is i, initialized 
        # to N+1, and then we decide how to find the DP formula.

        #For dp[i], the method is actually the same as the above method. 
        # It is still necessary to traverse all the number of printed A, and 
        # then multiply by the number of pasting times plus 1 to update dp[i].

        dp = [0]*(N+1)
        for i in range(1, N+1):
            dp[i] = dp[i - 1] + 1
            for j in range(i - 3, 0, -1):
                dp[i] = max(dp[i], dp[j] * (i - j - 1))
        return dp[N]

if __name__ == "__main__":
    print(Solution().maxA(3))
    print(Solution().maxADP(3))
