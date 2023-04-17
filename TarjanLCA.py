'''

Tarjan's offline Algorithm to find LCA of a set of node pairs.


'''

from typing import List


class Tarjan(object):

    def __init__(self, n, edges) -> None:
        self.n = n 
        self.G = [[] for _ in range(n)]
        for x, y in edges:
            self.G[x].append(y)
            self.G[y].append(x)  # 建树
        
    def LCA(self, queries) -> List[int]:
        color = [0] * self.n
        pa = list(range(self.n))
        def find(x:int) -> int:
            if x != pa[x]:
                pa[x] = find(pa[x])
            return pa[x]
        qs = [[] for _ in range(self.n)]
        ans = [-1]*len(queries)
        for i, (s, e) in enumerate(queries):
            qs[s].append((e,i))  # 路径端点分组
            if s != e:
                qs[e].append((s,i))
        def tarjan(x: int, fa: int) -> None:
            color[x] = 1  # 递归中
            for y in self.G[x]:
                if color[y] == 0:  # 未递归
                    tarjan(y, x)
                    pa[y] = x  # 相当于把 y 的子树节点全部 merge 到 x
            for y,i in qs[x]:
                # color[y] == 2 意味着 y 所在子树已经遍历完
                # 也就意味着 y 已经 merge 到它和 x 的 lca 上了
                if y == x or color[y] == 2:  # 从 y 向上到达 lca 然后拐弯向下到达 x
                    ans[i] = find(y)
            color[x] = 2  # 递归结束
        tarjan(0, -1)
        return ans



if __name__ == '__main__':
    n = 9
    edges = [[2,5],[3,4],[4,1],[1,7],[6,7],[7,0],[0,5],[5,8]]    
    queries = [[1,5],[2,7],[4,3],[1,8],[2,8],[4,3],[1,5],[1,4],[2,1],[6,0],[0,7],[8,6],[4,0],[7,5],[7,5],[6,0],[5,1],[1,1],[7,5],[1,7],[8,7],[2,3],[4,1],[3,5],[2,5],[3,7],[0,1],[5,8],[5,3],[5,2]]
    
    lca = Tarjan(n=n, edges=edges)
    sol = lca.LCA(queries=queries)
    for q,a in zip(queries, sol):
        print(q, a)


