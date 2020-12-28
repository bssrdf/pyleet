'''

-Medium-

*DP*
*Knapsack*

You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at 
most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

 

Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", 
"0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than 
the maximum of 3.
Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.
 

Constraints:

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] consists only of digits '0' and '1'.
1 <= m, n <= 100

'''

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """

        '''
        这题就是0-1背包的变种
        我们需要建立一个二维的DP数组，其中dp[i][j]表示有i个0和j个1时能组成的最多
        字符串的个数，而对于当前遍历到的字符串，我们统计出其中0和1的个数为zeros
        和ones，然后dp[i - zeros][j - ones]表示当前的i和j减去zeros和ones之前
        能拼成字符串的个数，那么加上当前的zeros和ones就是当前dp[i][j]可以达到
        的个数，我们跟其原有数值对比取较大值即可，所以递推式如下：

           dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1);

        '''
        def count(s):
            zos, ons = 0, 0 
            for c in s:
                if c == '1': ons +=1
                else: zos += 1
            return (zos, ons)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for s in strs:
            zeros, ones = count(s)
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones]+1)
        return dp[m][n]
        







if __name__ == "__main__":
    print(Solution().findMaxForm(["10","0001","111001","1","0"],  5, 3))
    print(Solution().findMaxForm(["10","0","1"], 1, 1))