'''

-Hard-
*DP*
*TYVJ1071*
熊大妈的奶牛在小沐沐的熏陶下开始研究信息题目。小沐沐先让奶牛研究了最长上升子序列，再让他们研究了最长公共子序列，现在又让他们要研究最长公共上升子序列了。
小沐沐说，对于两个串A，B，如果它们都包含一段位置不一定连续的数字，且数字是严格递增的，那么称这一段数字是两个串的公共上升子串，而所有的公共上升子串中最长的就是最长公共上升子串了。
奶牛半懂不懂，小沐沐要你来告诉奶牛什么是最长公共上升子串。不过，只要告诉奶牛它的长度就可以了。

1<=N<=3000

'''



from typing import List

class Solution:
    def longestCommonIncreasingSubsequence(self, A, B) -> int:
        # 此题为LIS和LCS的结合，所以容易列出状态转移方程：
        # f[i][j]表示a中的前i 个 和 b 中以 b[j] 结尾的最大LCIS。
        # f[i][j]=f[i-1][j], a[i]!=b[j]
        # f[i][j]=max(f[i-1][k])+1, a[i]=b[j],0<=k<j,b[j]>b[k]
        n = len(A)
        A = [-1] + A
        B = [-1] + B
        dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(1, n+1):
            val = 0            
            if B[0] < A[i]: val = dp[i-1][0]
            for j in range(1, n+1):
                if A[i] != B[j]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = val + 1
                if B[j] < A[i]:
                    val = max(val, dp[i-1][j])
        return max(dp[n])     
    

    def longestCommonIncreasingSubsequence2(self, A, B) -> int:
        n = len(A)
        A = [-1] + A
        B = [-1] + B
        dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                if A[i] != B[j]:
                    dp[i][j] = dp[i-1][j]
                else:
                    for k in range(j):
                        if B[k] < A[i]: 
                           dp[i][j] = max(dp[i][j], dp[i-1][k]+1)
        return max(dp[n])     
    





if __name__ == "__main__":   
    print(Solution().longestCommonIncreasingSubsequence([2, 2, 1, 3], [2, 1, 2, 3]))
    print(Solution().longestCommonIncreasingSubsequence2([2, 2, 1, 3], [2, 1, 2, 3]))
    print(Solution().longestCommonIncreasingSubsequence([3, 4, 9, 1], [5, 3, 8, 9, 10, 2, 1])) 
    print(Solution().longestCommonIncreasingSubsequence2([3, 4, 9, 1], [5, 3, 8, 9, 10, 2, 1])) 

