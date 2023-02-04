'''
-Medium-

On a 2D plane, we place n stones at some integer coordinate points. Each coordinate 
point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another 
stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of 
the ith stone, return the largest possible number of stones that can be removed.

 

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Explanation: One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.
Example 3:

Input: stones = [[0,0]]
Output: 0
Explanation: [0,0] is the only stone on the plane, so you cannot remove it.
 

Constraints:

1 <= stones.length <= 1000
0 <= xi, yi <= 10^4
No two stones are at the same coordinate point.

'''
import collections

class UnionFind:
    def __init__(self):
        self.parent = {}
    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    def union(self, u, v):
        self.parent.setdefault(u, u)
        self.parent.setdefault(v, v)
        pu, pv = self.find(u), self.find(v)
        if pu != pv: self.parent[pu] = pv
    def nConnected(self):
        groups = set()
        for i in self.parent.keys():
           groups.add(self.find(i))
        return len(groups) 
    '''
    def getGroups(self):
        groups = collections.defaultdict(list)
        for i in self.parent.keys():
            #print(i)
            groups[self.find(i)].append(i)
      #  print(groups)
        return groups
    '''


class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        '''
        m, n = 0, 0
        for st in stones:
            m = max(m, st[0])
            n = max(n, st[1])        
        m += 1; n += 1
        print('m=',m, 'n=',n)
        '''
        uf = UnionFind()            
        for r, c in stones:
            uf.union(r, ~c)  # Un
        return len(stones) - uf.nConnected()

    def removeStonesUF(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        m, n = 0, 0
        for st in stones:
            m = max(m, st[0])
            n = max(n, st[1])        
        m += 1; n += 1
        #def find(i):
        #    while roots[i] != i:
        #        roots[i] = roots[roots[i]]
        #        #print(i, roots)
        #    return roots[i]
        def find(i):
            if roots[i] != i:
                roots[i] = find(roots[i])
            return roots[i]

        
        roots = [-1]*(m+n)
        for r, c in stones:
            if roots[r] == -1: roots[r] = r            
            if roots[c+m] == -1: roots[c+m] = c+m
            p, q = find(r), find(c+m)
            if p != q:
                roots[p] = q 
            print(r,c,roots)
        st = set()
        for i in range(m+n):            
            st.add(find(i))
        #print(roots)
        return len(stones) - len(st)
        
        

if __name__ == "__main__":
    #print(Solution().removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))
    print(Solution().removeStonesUF([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))
    #print(Solution().removeStones([[0,0],[0,1],[1,1],[1,3],[2,1],[2,3]]))
   #print(Solution().removeStones([[0,0],[0,1],[1,1],[1,3],[2,2]]))
    #print(Solution().removeStonesUF([[0,0],[0,1],[1,1],[1,3],[2,2]]))