class UnionFindSet:
    def __init__(self, items=None, n=None):
        if items is None:
            items = list(range(n))
        self._nums = len(items)
        self._parents = {}
        self._ranks = {}
        for t in items:
            self._parents.setdefault(t, t)            
            self._ranks[t] = 1
          
    def find(self, u):
        #self._parents.setdefault(u, u)       
        while u != self._parents[u]:
            self._parents[u] = self._parents[self._parents[u]]
            u = self._parents[u]
        return u

    def connected(self, p,  q):
        rootP = self.find(p)
        rootQ = self.find(q)
        #处于同一棵树上的节点，相互连通
        return rootP == rootQ

    def print(self):
        print(self._parents) 

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
    #uf = UnionFindSet(items=range(10))
    uf = UnionFindSet(n=10)
    uf.union(1, 5)
    uf.union(2, 7)
    uf.union(4, 2)
    uf.union(5, 8)
    print(uf.count())
    #uf.print()
    print(uf.connected(1,8))
    uf = UnionFindSet(items=['6', '7', '10'])
    #uf = UnionFindSet(n=10)
    uf.union('6', '7')
    print(uf.count())
    s1 = ["7", "5", "4", "11", "13", "15", "19", "12", "0", "10"]
    s2 = ["16", "1", "7", "3", "15", "10", "13", "2", "19", "8"]
    uf = UnionFindSet(items=list(set(s1+s2)))
    pairs = [["6", "18"], ["8", "17"], ["1", "13"], ["0", "8"], ["9", "14"], ["11", "17"], ["11", "19"], ["13", "16"], ["0", "18"], ["3", "11"], ["1", "9"], ["2", "11"], ["2", "4"], ["0", "19"], ["8", "12"], ["8", "19"], ["16", "19"], ["1", "11"], ["2", "18"], ["0", "16"], ["7", "11"], ["6", "8"], ["9", "17"], ["8", "16"], ["3", "13"], ["7", "9"], ["7", "10"], ["3", "6"], ["15", "19"], ["1", "5"], ["2", "14"], ["1", "18"], ["8", "15"], ["14", "19"], ["3", "17"], ["6", "10"], ["5", "17"], ["10", "15"], ["1", "10"], ["4", "6"]]
    for p in pairs:
        print(p[0], p[1])        
        uf.union(p[0], p[1])

    