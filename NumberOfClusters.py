'''
-Medium-

Given a 2-d array , elements only consist of the lowecase alphabets - a , b or c.
Find the number of clusters (same lowecase alphabets that connect 4-directionally - up , down ,left or right).

Example 1

a a a
b b b

Output : 2

Example 2

b b b c a a
b b b b b b

Output : 3

Example 3

a a a
c c b
a b a

Output : 6


'''

class Solution(object):

    def findNumOfClusters(self, grid):
        if not grid:
            return 0
        n,m = len(grid), len(grid[0])
        roots = [i*m+j for i in range(n) for j in range(m)]
        cnt = n*m
        dirs = [(-1,0), (0,-1), (1,0), (0,1)]
        for t in ['a','b','c']:
            for i in range(n):
                for j in range(m):                
                    if grid[i][j] == t:
                        idx = i*m+j
                        for r,c in dirs:
                            i1,j1=i+r,j+c
                            if i1<0 or i1>=n or j1<0 or j1>=m:
                                continue
                            if grid[i1][j1] == t:
                                idx1 = m*i1+j1
                                x,y = self.find(roots, idx),self.find(roots, idx1) 
                                if x != y:
                                    roots[x] = y
                                    cnt -= 1
        return cnt

    def find(self, roots, i):
        # this while loop is called "qiuck union";
        # it "recursively" decends to the root node represented by the
        # node whose roots value is untouched 'i'
        while roots[i] != i:
            # path compression; set every other node in path point to its grandparent
            roots[i] = roots[roots[i]] 
            i = roots[i]
        return i


if __name__ == "__main__":
    grid = ["bbbcaa",
            "bbbbbb"]
    print(Solution().findNumOfClusters(grid))
    grid = ["aaa",
            "ccb",
            "aba" ]
    print(Solution().findNumOfClusters(grid))