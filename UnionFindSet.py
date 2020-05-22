class UnionFindSet:
    def __init__(self, items):
        self._nums = len(items)
        self._parents = {}
        self._ranks = {}
        for t in items:
            self.find(t)
            self._ranks[t] = 1
        
    def find(self, u):
        self._parents.setdefault(u, u)       
        while u != self._parents[u]:
            self._parents[u] = self._parents[self._parents[u]]
            u = self._parents[u]
        return u

    def connected(self, p,  q):
        rootP = self.find(p)
        rootQ = self.find(q)
        #处于同一棵树上的节点，相互连通
        return rootP == rootQ


    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv: return False
        
        if self._ranks[pu] < self._ranks[pv]:
            self._parents[pu] = pv
            self._ranks[pv] += self._ranks[pu]
        else:
            self._parents[pv] = pu
            self._ranks[pu] += self._ranks[pv]
        

        self._nums -= 1
        return True

    def count(self):
        return self._nums



if __name__ == "__main__":
    uf = UnionFindSet(range(10))
    uf.union(1, 5)
    uf.union(2, 7)
    uf.union(4, 2)
    uf.union(5, 8)
    print(uf.count())
    print(uf.connected(1,8))