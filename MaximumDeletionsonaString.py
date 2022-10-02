'''


'''
from functools import lru_cache

import sys
sys.setrecursionlimit(300000)

class Solution:
    def deleteString(self, s: str) -> int:
        @lru_cache(None)
        def dfs(s):
            ret = 1 
            for i in range(1,len(s)//2+1):
                if s[:i] == s[i:2*i]:
                    ret = max(ret, dfs(s[i:]) + 1)
            return ret 
        return dfs(s)
    
    def deleteString2(self, s: str) -> int:
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
    