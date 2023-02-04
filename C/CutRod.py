'''
CLRS Dynamic Programming introduction
'''

import sys

class Solution(object):
    def cutRod(self, L, n):
        """
        :type L: List[int]
        :type n: int
        :rtype:  int
        """
        r = [-sys.maxint]*(n+1)
        s = [-sys.maxint]*(n+1)
        q = self.helper(L, n, r, s)
        return q,s

    def helper(self, L, n, r, s):
        if r[n] >= 0:
            return r[n]
        if n == 0:
            q = 0
        else:
            q = -sys.maxint
            for i in range(1,n+1):
                #q = max(q, L[i-1]+self.helper(L, n-i, r, s))
                w = L[i-1]+self.helper(L, n-i, r, s)
                if q < w:
                    q = w
                    s[n] = i
        r[n] = q
        return q


if __name__ == "__main__":
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    n = 7
    q,s = Solution().cutRod(p, n)
    print q
    while n > 0:
        print s[n]
        n = n - s[n]

