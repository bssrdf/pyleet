


class Solution(object):

    def id(self, c):
        return ord(c) - ord('a')

    def ch(self, x):
        return chr(x+ord('a'))

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return

        # 小树接到大树下面，较平衡
        if rootP < rootQ:
            self.parent[rootQ] = rootP
          
        else:
            self.parent[rootP] = rootQ
            
    
    # 返回节点 x 的根节点 
    def find(self, x):
        self.parent.setdefault(x,x)
        while self.parent[x] != x :
            # 进行路径压缩
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def smallestEquivalentString(self, A, B, S):
        #self.parent = [i for i in range(26)]
        self.parent = {}
        for a,b in zip(A, B):
            #print(self.id(a), self.id(b))
            #self.union(self.id(a), self.id(b))
            self.union(a, b)
        res = ''
        for s in S:
            res += self.find(s)
        return res

print(Solution().smallestEquivalentString("parker", "morris", "parser"))
print(Solution().smallestEquivalentString("leetcode", "programs", "sourcecode"))

