'''
-Hard-


You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted 
at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is represented 
by a 0-indexed array parent of size n, where parent[i] is the parent of node i. Since 
node 0 is the root, parent[0] == -1.

You are also given a string s of length n, where s[i] is the character assigned to node i.

Return the length of the longest path in the tree such that no pair of adjacent nodes 
on the path have the same character assigned to them.

 

Example 1:


Input: parent = [-1,0,0,1,1,2], s = "abacbe"
Output: 3
Explanation: The longest path where each two adjacent nodes have different characters in the tree is the path: 0 -> 1 -> 3. The length of this path is 3, so 3 is returned.
It can be proven that there is no longer path that satisfies the conditions. 
Example 2:


Input: parent = [-1,0,0,0], s = "aabc"
Output: 3
Explanation: The longest path where each two adjacent nodes have different characters is the path: 2 -> 0 -> 3. The length of this path is 3, so 3 is returned.
 

Constraints:

n == parent.length == s.length
1 <= n <= 105
0 <= parent[i] <= n - 1 for all i >= 1
parent[0] == -1
parent represents a valid tree.
s consists of only lowercase English letters.

'''
from typing import List
from collections import defaultdict
from heapq import nlargest 
class Solution:
    def longestPath2(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        for i,v in enumerate(parent):
            graph[v].append(i)
        ans = [1]
        def dfs(u):
            # ret = 1
            l1, l2 = 0, 0
            c1, c2 = -1, -1
            if not graph[u]: 
                return 1

            for v in graph[u]:
                l = dfs(v)
                if s[u] != s[v]:
                    if l >= l1:
                        l1, l2 = l, l1
                        c1, c2 = v, c1
                    elif l >= l2:
                        l2 = l
                        c2 = v
                else:
                    if l >= l1:
                        l1 = l
            if c1 != -1 and c2 != -1:
                ans[0] = max(ans[0], l1+l2+1)
                return l1 + 1
            elif c1 != -1:     
                ans[0] = max(ans[0], l1+1)
                return l1 + 1
            ans[0] = max(ans[0], l1)
            return l1     
        dfs(0)
        return ans[0]
    
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        for i,v in enumerate(parent):
            graph[v].append(i)
        ans = [1]
        def dfs(u):
            # ret = 1
            candi = [0, 0]
            for v in graph[u]:
                l = dfs(v)
                if s[u] != s[v]:
                    candi.append(l)
            candi = nlargest(2,candi) 
            ans[0] = max(ans[0], candi[0]+candi[1]+1)
            return max(candi)+1     
        dfs(0)
        return ans[0]
        



        
    
if __name__ == "__main__":
    print(Solution().longestPath(parent = [-1,0,0,1,1,2], s = "abacbe"))
    print(Solution().longestPath(parent = [-1,0,0,0], s = "aabc"))
    print(Solution().longestPath(parent = [-1,0,1], s = "aab"))
    par = [-1,137,65,60,73,138,81,17,45,163,145,99,29,162,19,20,132,132,13,60,21,18,155,65,13,163,125,102,96,60,50,101,100,86,162,42,162,94,21,56,45,56,13,23,101,76,57,89,4,161,16,139,29,60,44,127,19,68,71,55,13,36,148,129,75,41,107,91,52,42,93,85,125,89,132,13,141,21,152,21,79,160,130,103,46,65,71,33,129,0,19,148,65,125,41,38,104,115,130,164,138,108,65,31,13,60,29,116,26,58,118,10,138,14,28,91,60,47,2,149,99,28,154,71,96,60,106,79,129,83,42,102,34,41,55,31,154,26,34,127,42,133,113,125,113,13,54,132,13,56,13,42,102,135,130,75,25,80,159,39,29,41,89,85,19]
    s = "ajunvefrdrpgxltugqqrwisyfwwtldxjgaxsbbkhvuqeoigqssefoyngykgtthpzvsxgxrqedntvsjcpdnupvqtroxmbpsdwoswxfarnixkvcimzgvrevxnxtkkovwxcjmtgqrrsqyshxbfxptuvqrytctujnzzydhpal"
    print(Solution().longestPath(par, s))