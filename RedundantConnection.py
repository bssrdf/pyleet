from UF import UF


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        uf = UF(len(edges))
        res = None
        for e in edges:
            n1, n2 = e[0], e[1]
            if uf.connected(n1, n2):
                res = e[:]
            else:
                uf.union(n1, n2)
        return res


print(Solution().findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))
print(Solution().findRedundantConnection([[1,2], [1,3], [2,3]]))