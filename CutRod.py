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
        return self.helper(L, n, r)

    def helper(self, L, n, r):
        if r[n] >= 0:
            return r[n]
        if n == 0:
            q = 0
        else:
            q = -sys.maxint
            for i in range(1,n+1):
                q = max(q, L[i-1]+self.helper(L, n-i, r))
        r[n] = q
        return q


if __name__ == "__main__":
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    print Solution().cutRod(p, 10)
