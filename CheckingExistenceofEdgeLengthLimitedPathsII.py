'''

-Hard-

An undirected graph of n nodes is defined by edgeList, where 
edgeList[i] = [u_i, v_i, dis_i] denotes an edge between nodes u_i and v_i with 
distance dis_i. Note that there may be multiple edges between two nodes, 
and the graph may not be connected.

Implement the DistanceLimitedPathsExist class:

DistanceLimitedPathsExist(int n, int[][] edgeList) Initializes the class with an 
undirected graph.
boolean query(int p, int q, int limit) Returns true if there exists a path 
from p to q such that each edge on the path has a distance strictly less than limit, 
and otherwise false.
Example 1:

Image text

Input
["DistanceLimitedPathsExist", "query", "query", "query", "query"]
[[6, [[0, 2, 4], [0, 3, 2], [1, 2, 3], [2, 3, 1], [4, 5, 5]]], [2, 3, 2], [1, 3, 3], [2, 0, 3], [0, 5, 6]]
Output
[null, true, false, true, false]

Explanation
DistanceLimitedPathsExist distanceLimitedPathsExist = new DistanceLimitedPathsExist(6, [[0, 2, 4], [0, 3, 2], [1, 2, 3], [2, 3, 1], [4, 5, 5]]);
distanceLimitedPathsExist.query(2, 3, 2); // return true. There is an edge from 2 to 3 of distance 1, which is less than 2.
distanceLimitedPathsExist.query(1, 3, 3); // return false. There is no way to go from 1 to 3 with distances strictly less than 3.
distanceLimitedPathsExist.query(2, 0, 3); // return true. There is a way to go from 2 to 0 with distance < 3: travel from 2 to 3 to 0.
distanceLimitedPathsExist.query(0, 5, 6); // return false. There are no paths from 0 to 5.
Constraints:

2 <= n <= 10^4
0 <= edgeList.length <= 10^4
edgeList[i].length == 3
0 <= u_i, v_i, p, q <= n-1
u_i != v_i
p != q
1 <= dis_i, limit <= 10^9
At most 10^4 calls will be made to query.

解法
https://github.com/wisdompeak/LeetCode/tree/master/Union_Find/1724.Checking-Existence-of-Edge-Length-Limited-Paths-II

'''
import bisect

class DistanceLimitedPathsExist:
    def __init__(self, n, edgeList):
        self.snaps = [[] for _ in range(10000)]
        self.father = [0]*10000
        self.rank = [0]*10000
        self.dist = []
        self.changed = set()
        self.snapId = 0
        self.INT_MAX = 10**4+1
        for i in range(n):
            self.father[i] = i
            self.snaps[i].append((-1,i))
        edgeList.sort(key=lambda x: x[2])
        cur_dist = 0
        for e in edgeList:
            if cur_dist < e[2]:
                self.dist.append(cur_dist)
                cur_dist = e[2]
                for node in self.changed:
                    self.snaps[node].append((self.snapId, self.father[node]))
                self.changed.clear()
                self.snapId += 1
            self.union(e[0], e[1])

    def find(self, node):
        while self.father[node] != node:
            # 不做任何“路径压缩”, because要原原本本的保留每个节点的原始父节点（因为需要存储快照）
            # self.father[node] = sef.father[self.father[node]] 
            node = self.father[node]
        return node

    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if self.find(x) != self.find(y):
            if self.rank[x] < self.rank[y]:
                self.father[x] = y
                self.rank[y] = max(self.rank[y], self.rank[x]+1)
                self.changed.add(x)
            else:
                self.father[y] = x
                self.rank[x] = max(self.rank[x], self.rank[y]+1)
                self.changed.add(y)
    
    def findSnap(self, node, snap_id):
        idx = bisect.bisect_left(self.snaps[node], (snap_id, self.INT_MAX))        
        f = self.snaps[node][idx-1][1]
        # print('find', node, f, idx)
        if f == node: return f
        else:
            return self.findSnap(f, snap_id)        

    def query(self, p, q, limit):
        snap_id = bisect.bisect_left(self.dist, limit) - 1
        # print('pq', p, q, 
        #      snap_id, self.dist, self.snaps[p], self.snaps[q])

        return self.findSnap(p, snap_id) == self.findSnap(q, snap_id)


if __name__ == "__main__":
    distanceLimitedPathsExist = DistanceLimitedPathsExist(6, [[0, 2, 4], [0, 3, 2], [1, 2, 3], [2, 3, 1], [4, 5, 5]])
    print(distanceLimitedPathsExist.query(2, 3, 2)) # return true. There is an edge from 2 to 3 of distance 1, which is less than 2.
    print(distanceLimitedPathsExist.query(1, 3, 3)) # return false. There is no way to go from 1 to 3 with distances strictly less than 3.
    print(distanceLimitedPathsExist.query(2, 0, 3)) # return true. There is a way to go from 2 to 0 with distance < 3: travel from 2 to 3 to 0.
    print(distanceLimitedPathsExist.query(0, 5, 6)) # return false. There are no paths from 0 to 5.

