'''
-Hard-

There are n items each belonging to zero or one of m groups where group[i] is the group 
that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group. 
The items and the groups are zero indexed. A group can have no item belonging to it.

Return a sorted list of the items such that:

The items that belong to the same group are next to each other in the sorted list.
There are some relations between these items where beforeItems[i] is a list containing 
all the items that should come before the i-th item in the sorted array (to the left 
of the i-th item).
Return any solution if there is more than one solution and return an empty list if there 
is no solution.

 

Example 1:



Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
Output: [6,3,4,1,5,2,0,7]
Example 2:

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
Output: []
Explanation: This is the same as example 1 except that 4 needs to be before 6 in the sorted list.
 

Constraints:

1 <= m <= n <= 3 * 10^4
group.length == beforeItems.length == n
-1 <= group[i] <= m - 1
0 <= beforeItems[i].length <= n - 1
0 <= beforeItems[i][j] <= n - 1
i != beforeItems[i][j]
beforeItems[i] does not contain duplicates elements.

'''
from collections import defaultdict
from collections import deque
class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        """
        :type n: int
        :type m: int
        :type group: List[int]
        :type beforeItems: List[List[int]]
        :rtype: List[int]
        """
        gm = defaultdict(set)        
        graph = defaultdict(set)        
        groups = set()
        for i,g in enumerate(group):
            gm[g].add(i)
            groups.add(g)
        l = m        
        extras = set()
        if -1 in gm:
            for node in gm[-1]:
                for b in beforeItems[node]:
                    if b not in gm[-1]:
                        if l == m: l = m+1
                        extras.add(node)
                        break
        if l == m+1:
            groups.add(m)
            for e in extras:
                gm[-1].remove(e)
                gm[m].add(e)
                group[e] = m    
        m = l
        for g in groups:
            for v in gm[g]:
                for u in beforeItems[v]:
                    if u not in gm[g]:
                        graph[group[u]].add(g)
        #print(gm, m)
        if -1 not in gm:
            start = 0
            indegrees = [0]*(m)
        else:
            start = -1
            indegrees = [0]*(m+1)
        for i in range(start,m):        
            for c in graph[i]:
                indegrees[c] += 1
        res, tmp = [], []         
        q = deque()
        for i in range(start,m):
            if indegrees[i] == 0: q.append(i)
        #print(indegrees)
        while q:
            node = q.popleft()
            tmp.append(node)
            for c in graph[node]:
                indegrees[c] -= 1
                if indegrees[c] == 0:
                    #graph[node].remove(c)
                    q.append(c)
        #print(indegrees)
        for i in range(start,m):
            if indegrees[i] != 0: return []
        def toposort(i):
            gs = defaultdict(set)        
            for node in gm[i]:
                for b in beforeItems[node]:
                    if b in gm[i]:
                       gs[b].add(node)
            ind = {node:0 for node in gm[i]}
            for node in gm[i]:
                for c in gs[node]:
                   ind[c] += 1
            ans = []
            q = deque()
            for i in ind:
                if ind[i] == 0: q.append(i)
            while q:
                node = q.popleft()
                ans.append(node)
                for c in gs[node]:
                    ind[c] -= 1
                    if ind[c] == 0:
                        #graph[node].remove(c)
                        q.append(c)
            for i in ind:
                if ind[i] != 0: return []
            return ans
        #print(tmp)
        for i in tmp:
            if i in gm:
                ret = toposort(i)
                #print(i, ret)
                if not ret: return []
                res += ret
        return res
    
    def sortItemsClean(self, n, m, group, beforeItems):
        """
        :type n: int
        :type m: int
        :type group: List[int]
        :type beforeItems: List[List[int]]
        :rtype: List[int]
        """
        # This problem can be broken down into two level topological sorting
        # 1) sort at group level
        # 2) sort within each group at each item level 
        gm = defaultdict(set)        
        graph = defaultdict(set)        
        for i,g in enumerate(group):
            gm[g].add(i)
        extras = set()
        if -1 in gm:
            for node in gm[-1]:
                for b in beforeItems[node]:
                    if b not in gm[-1]:
                        extras.add(node)
                        break
        if extras:
            for e in extras:
                gm[-1].remove(e)
                gm[m].add(e)
                group[e] = m    
            m += 1            
        def toposort1(gs, nodes):            
            ind = {node:0 for node in nodes}
            for node in nodes:
                for c in gs[node]:
                   ind[c] += 1
            ans, size = [], 0
            q = deque()
            for i in ind:
                if ind[i] == 0: 
                    size += 1
                    q.append(i)
            while q:
                node = q.popleft()
                ans.append(node)
                for c in gs[node]:
                    ind[c] -= 1
                    if ind[c] == 0:
                        size += 1
                        q.append(c)
            if size != len(nodes): return []
            return ans
        for g in gm:
            for v in gm[g]:
                for u in beforeItems[v]:
                    if u not in gm[g]:
                        graph[group[u]].add(g)
        tmp = toposort1(graph, set(gm.keys()))
        if not tmp: return []
        res = []
        for i in tmp:
            if i in gm:
                gs = defaultdict(set)        
                for node in gm[i]:
                    for b in beforeItems[node]:
                        if b in gm[i]:
                            gs[b].add(node)
                ret = toposort1(gs, gm[i])
                if not ret: return []
                res += ret
        return res

    
if __name__ == "__main__":
    print(Solution().sortItems(n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]))
    print(Solution().sortItems(n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]))
    print(Solution().sortItems(5,5,[2,0,-1,3,0],[[2,1,3],[2,4],[],[],[]]))
    print(Solution().sortItems(3,1,[-1,0,-1],[[],[0],[1]]))
    print(Solution().sortItems(5,3,[0,0,2,1,0],[[3],[],[],[],[1,3,2]]))