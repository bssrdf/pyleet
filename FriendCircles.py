#import sys

#print(sys.path)

from UF import UF

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M[0])
        
        uf = UF(n)
        for i in range(n):
            for j in range(n):
                if i != j and M[i][j] == 1:
                    uf.union(i,j)
        return uf.count()


M=[[1,1,0],
   [1,1,0],
   [0,0,1]]
print(Solution().findCircleNum(M))


