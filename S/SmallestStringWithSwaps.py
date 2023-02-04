'''

-Medium-

You are given a string s, and an array of pairs of indices in the string 
pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.

 

Example 1:

Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"
Example 2:

Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"
Example 3:

Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination: 
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"
 

Constraints:

1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s only contains lower case English letters.



'''
from typing import List
from collections import deque, defaultdict

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        graph = defaultdict(list)
        n = len(s)
        si = {i:v for i,v in enumerate(s)}
        for u,v in pairs:
            graph[u].append(v)
            graph[v].append(u)
        connected = []
        visited = [False]*n 
        def dfs(u, path):
            visited[u] = True
            path.append(u)
            for v in graph[u]:
                if not visited[v]:
                    dfs(v, path) 
        for i in range(n):
            if not visited[i]:
                path = []
                dfs(i, path)
                connected.append(path)
        res = ['']*n
        for con in connected:
            t = sorted([si[c] for c in con])
            for c,d in zip(sorted(con), t):
               res[c] = d 
        return ''.join(res)


if __name__ == "__main__":
    print(Solution().smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2]]))
    print(Solution().smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2],[0,2]]))


