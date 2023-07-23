'''

-Hard-
*DFS*
*Bitmask*

You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is represented by a 0-indexed array parent of size n, where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.

You are also given a string s of length n, where s[i] is the character assigned to the edge between i and parent[i]. s[0] can be ignored.

Return the number of pairs of nodes (u, v) such that u < v and the characters assigned to edges on the path from u to v can be rearranged to form a palindrome.

A string is a palindrome when it reads the same backwards as forwards.

 

Example 1:



Input: parent = [-1,0,0,1,1,2], s = "acaabc"
Output: 8
Explanation: The valid pairs are:
- All the pairs (0,1), (0,2), (1,3), (1,4) and (2,5) result in one character which is always a palindrome.
- The pair (2,3) result in the string "aca" which is a palindrome.
- The pair (1,5) result in the string "cac" which is a palindrome.
- The pair (3,5) result in the string "acac" which can be rearranged into the palindrome "acca".
Example 2:

Input: parent = [-1,0,0,0,0], s = "aaaaa"
Output: 10
Explanation: Any pair of nodes (u,v) where u < v is valid.
 

Constraints:

n == parent.length == s.length
1 <= n <= 105
0 <= parent[i] <= n - 1 for all i >= 1
parent[0] == -1
parent represents a valid tree.
s consists of only lowercase English letters.


'''

from typing import List
from collections import defaultdict, Counter
class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        #wrong
        n = len(s)
        G = defaultdict(list)
        cnt = Counter()
        mask = [0]*n
        for i,p in enumerate(parent):
            if p >= 0: 
               G[p].append(i)
        def dfs(u, parity):
            if u > 0:
                mask[u] = parity ^ (1 << (ord(s[u])- ord('a')))
            # cnt[mask[u]] += 1
            for v in G[u]:
                dfs(v, mask[u])
        dfs(0, 0)
        for i in range(n):
            print(i, f'{mask[i]:26b}')
        ans = 0
        cnt[0] = 1
        for u in range(1, n):
            t = cnt[mask[u]]
            for i in range(26):
                if (1 << i) & mask[u] > 0:
                    t += cnt[mask[u]^(1<<i)] 
            print(u, ans, t, ans+t)
            ans += t
            cnt[mask[u]] += 1
        return ans        
    
    def countPalindromePaths2(self, parent: List[int], s: str) -> int:
        # the idea is still LCA
        # For each letter, its frequency on u-v path == (frequency on root->u path) + 
        # (frequency on root->v path) - 2 * (frequency on root -> LCA(u, v) path)
        # Note, if we only consider the parity (or just consider % 2), 
        # the 2 * (frequency on root -> LCA(u, v) path) part doesnt matter 
        # (since it's always even), so our interested part is 
        # just (frequency on root->u path) + (frequency on root->v path), 
        # both parts can be just calculated in a simple DFS.
        n = len(s)
        G = defaultdict(list)
        cnt = Counter()
        for i,p in enumerate(parent):
            if p >= 0: 
               G[p].append(i)
        def dfs(u, parity):
            ret = 0
            if u :
                parity ^= 1 << (ord(s[u]) - ord('a'))
            i = 1 << 25
            while i: 
                # if parity ^ i in cnt:
                ret += cnt[parity ^ i] # case where only one char has parity 1 
                i >>= 1
            ret += cnt[parity] # case where no char has parity 1
            cnt[parity] += 1
            for v in G[u]:
                ret += dfs(v, parity)
            return ret
        return dfs(0, 0)
        

if __name__ == "__main__":
    # print(Solution().countPalindromePaths(parent = [-1,0,0,1,1,2], s = "acaabc"))
    # print(Solution().countPalindromePaths(parent = [-1,0,0,0,0], s = "aaaaa"))
    print(Solution().countPalindromePaths(parent = [-1,5,0,5,5,2], s = "xsbcqq"))
    print(Solution().countPalindromePaths2(parent = [-1,5,0,5,5,2], s = "xsbcqq"))