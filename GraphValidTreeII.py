'''
-Medium-

Please design a data structure which can do the following operations:

void addEdge(int a, int b):add an edge between node aa and node bb. It is guaranteed that there isn't self-loop or multi-edge.
bool isValidTree(): Check whether these edges make up a valid tree.
样例
Example 1

Input:
addEdge(1, 2)
isValidTree()
addEdge(1, 3)
isValidTree()
addEdge(1, 5)
isValidTree()
addEdge(3, 5)
isValidTree()
Output: ["true","true","true","false"]



'''

class Solution:
    def __init__(self):
        self.edgeNum = 0
        self.vertexNum = 0
        self.tag = 1
        self.f = {}

    def Find(self,x):
        while x != self.f[x]:
            self.f[x] = self.f[self.f[x]]
            x = self.f[x]
        return x



    def Union(self, x, y):
        fx = self.Find(x)
        fy = self.Find(y)
        if fx != fy:
            self.f[fx] = fy
        else:
            self.tag = 0

    def addEdge(self, a, b):
        if a not in self.f:
            self.f[a] = a
            self.vertexNum += 1
        if b not in self.f:
            self.f[b] = b
            self.vertexNum += 1
        self.edgeNum += 1
        self.Union(a, b)

        # write your code here

    """
    @return: check whether these edges make up a valid tree
    """

    def isValidTree(self):
        # write your code here
        if self.edgeNum + 1 == self.vertexNum and self.tag == 1:
            return True
        else:
            return False

   

if __name__ == "__main__":
    sol = Solution()
    sol.addEdge(1, 2)
    print(sol.isValidTree())
    sol.addEdge(1, 3)
    print(sol.isValidTree())
    sol.addEdge(1, 5)
    print(sol.isValidTree())
    sol.addEdge(3, 5)
    print(sol.isValidTree())
