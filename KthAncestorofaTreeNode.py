'''

-Hard-

You are given a tree with n nodes numbered from 0 to n - 1 in the form of a parent array parent where 
parent[i] is the parent of ith node. The root of the tree is node 0. Find the kth ancestor of a given node.

The kth ancestor of a tree node is the kth node in the path from that node to the root node.

Implement the TreeAncestor class:

TreeAncestor(int n, int[] parent) Initializes the object with the number of nodes in the tree and the 
parent array.

int getKthAncestor(int node, int k) return the kth ancestor of the given node node. If there is no 
such ancestor, return -1.
 

Example 1:


Input
["TreeAncestor", "getKthAncestor", "getKthAncestor", "getKthAncestor"]
[[7, [-1, 0, 0, 1, 1, 2, 2]], [3, 1], [5, 2], [6, 3]]
Output
[null, 1, 0, -1]

Explanation
TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);
treeAncestor.getKthAncestor(3, 1); // returns 1 which is the parent of 3
treeAncestor.getKthAncestor(5, 2); // returns 0 which is the grandparent of 5
treeAncestor.getKthAncestor(6, 3); // returns -1 because there is no such ancestor
 

Constraints:

1 <= k <= n <= 5 * 10^4
parent.length == n
parent[0] == -1
0 <= parent[i] < n for all 0 < i < n
0 <= node < n
There will be at most 5 * 10^4 queries.

'''

from typing import List

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.N = 20
        self.P = [[-1]*len(parent) for _ in range(self.N)] 
        for i in range(n):
            self.P[0][i] = parent[i]
        for i in range(1, self.N):
            for node in range(n):
                nodep = self.P[i-1][node] # find node's 2^(i-1)-th parent 
                if nodep != -1:
                    self.P[i][node] = self.P[i-1][nodep] # node's 2^i-th parent is nodep's 2^(i-1)-th parent
        for i in range(4):
            print(self.P[i])
    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(self.N):
            if k & (1<<i):
                node = self.P[i][node]
                if node == -1: return -1
        return node
        

if __name__ == "__main__":

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
    treeAncestor = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
    print(treeAncestor.getKthAncestor(3, 1)) # returns 1 which is the parent of 3
    print(treeAncestor.getKthAncestor(5, 2)) #  returns 0 which is the grandparent of 5
    print(treeAncestor.getKthAncestor(6, 3)) # returns -1 because there is no such ancestor

    treeAncestor = TreeAncestor(14, [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 7, 8, 8])
    print(treeAncestor.getKthAncestor(3, 1)) # returns 1 which is the parent of 3
    print(treeAncestor.getKthAncestor(5, 2)) #  returns 0 which is the grandparent of 5
    print(treeAncestor.getKthAncestor(6, 3)) # returns -1 because there is no such ancestor
 
    print(treeAncestor.getKthAncestor(9, 3)) # returns -1 because there is no such ancestor