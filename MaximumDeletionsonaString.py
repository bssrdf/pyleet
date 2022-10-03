'''


'''
from functools import lru_cache

import sys
sys.setrecursionlimit(300000)

class Solution:
    def deleteString(self, s: str) -> int:
        if (len(set(s)) == 1): return len(s)
        @lru_cache(None)
        def dfs(s):
            ret = 1 
            for i in range(1,len(s)//2+1):
                if s[:i] == s[i:2*i]:
                    ret = max(ret, dfs(s[i:]) + 1)
            return ret 
        return dfs(s)
    
    def deleteString2(self, s: str) -> int:
        if (len(set(s)) == 1): return len(s)
        def partialMatchTable(P):
            n = len(P)
            pt = [0]*n 
            k = 0
            for q in range(1,n): # start matching at index 1, no need to match itself                
                while k > 0 and P[k] != P[q]: 
                    k = pt[k-1] # note the difference from CLRS text which has k = pt[k]
                if P[k] == P[q]:
                    k += 1
                pt[q] = k
            return pt
        @lru_cache(None)
        def dfs(s):
            ret = 1 
            pt = partialMatchTable(s)
            for i in range(1,len(s),2):
                if pt[i] == (i+1)//2:
                    ret = max(ret, dfs(s[pt[i]:]) + 1)
            return ret 
        return dfs(s)

    def deleteString3(self, s):
        # lcs[i][j] means the length of the longest common substring.
        # If lcs[i][j] = k,
        # then s.substring(i, i + k) == s.substring(j, j + k)
        # and s.substring(i, i + k + 1) != s.substring(j, j + k + 1).
        # This can be done in O(n^2).

        # dp[i] mean the the maximum number of operations to delete
        # the substring starting at s[i].

        # If lcs[i][j] >= j - i,
        # s.substring(i, j) == s.substring(j, j + j - i)
        # this means we can delete the prefix s.substring(i, j) from s.substring(i),
        # and it changes to s.substring(j).
        # And we update dp[i] = max(dp[i], dp[j] + 1)


        # Complexity
        # Time O(n^2)
        # Space O(n^2)
        n = len(s)
        if len(set(s)) == 1: return n
        lcs = [[0] * (n + 1) for i in range(n + 1)]
        dp = [1] * n
        for i in range(n-1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    lcs[i][j] = lcs[i + 1][j + 1] + 1
                if lcs[i][j] >= j - i:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[0]


if __name__ == "__main__":   
    # print(Solution().deleteString(s = "aaabaab"))
    # print(Solution().deleteString(s = "aaaaa"))
    # print(Solution().deleteString(s = "abcabcdabc"))
    print(Solution().deleteString2(s = "aaabaab"))
    print(Solution().deleteString2(s = "aaaaa"))
    print(Solution().deleteString2(s = "abcabcdabc"))
    print(Solution().deleteString2(s = "abaaa"))
    s = 'a'*2000
    # print(Solution().deleteString2(s = s))

    sol = Solution().deleteString2(s = s)
    print(sol)
    