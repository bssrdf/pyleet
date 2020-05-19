class UF:
  
    def __init__(self, n):    
        self.nums = n   #记录连通分量个数
        self.parent = [i for i in range(n+1)] # 存储若干棵树
        self.size = [1] * (n+1) # 记录树的“重量”
        
    

    #将 p 和 q 连通 
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return

        # 小树接到大树下面，较平衡
        if self.size[rootP] > self.size[rootQ]:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
        else:
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
        
        self.nums -= 1
    

    # 判断 p 和 q 是否互相连通 
    def connected(self, p,  q):
        rootP = self.find(p)
        rootQ = self.find(q)
        #处于同一棵树上的节点，相互连通
        return rootP == rootQ
    

    # 返回节点 x 的根节点 
    def find(self, x):
        while self.parent[x] != x :
            # 进行路径压缩
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def count(self):
        return self.nums





