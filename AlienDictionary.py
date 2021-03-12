'''

-Hard-

*Topological Sort*
*BFS*
*DFS*

There is a new alien language which uses the latin alphabet. However, the order among 
letters are unknown to you. You receive a list of non-empty words from the dictionary, 
where words are sorted lexicographically by the rules of this new language. Derive the 
order of letters in this language.

You may assume all letters are in lowercase.
The dictionary is invalid, if a is prefix of b and b is appear before a.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return the smallest in normal 
lexicographical order


Example 1:

Input：["wrt","wrf","er","ett","rftt"]
Output："wertf"
Explanation：
from "wrt"and"wrf" ,we can get 't'<'f'
from "wrt"and"er" ,we can get 'w'<'e'
from "er"and"ett" ,we can get 'r'<'t'
from "ett"and"rftt" ,we can get 'e'<'r'
So return "wertf"

Example 2:

Input：["z","x"]
Output："zx"
Explanation：
from "z" and "x"，we can get 'z' < 'x'
So return "zx"

'''

from collections import deque
from collections import defaultdict
class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # Write your code here
        all_chars = {c for w in words for c in w}
        graph = defaultdict(set)
        inDegree = [0] * 26
        q = deque()
        res = ''        
        for i in range(1, len(words)):
            first = words[i - 1]
            second = words[i]
            mn = min(len(first), len(second))
            j = 0
            while j < mn:                
                parent = first[j]
                child = second[j]
                if parent != child :
                    graph[parent].add(child)
                    inDegree[ord(child) - ord('a')] += 1
                    break
                j += 1
            if j == mn and len(first) > len(second): return ""
        
        for c in graph.keys():
            if inDegree[ord(c)-ord('a')] == 0:
                q.append(c)
        while q:
            c = q.popleft()
            res += c
            for ch in graph[c]:              
                    inDegree[ord(ch)-ord('a')] -= 1
                    if inDegree[ord(ch)-ord('a')] == 0:
                        q.append(ch)        
        if len(res) != len(graph): return ""
        if len(all_chars) > len(res):
            for c in all_chars:
                if c not in res:
                    t, insert = [], False
                    for ch in list(res):
                        if c < ch and not insert: 
                            t.append(c)
                            insert = True
                        t.append(ch)
                    if not insert: t.append(c)
                    res = ''.join(t) 
        return res
               
if __name__ == "__main__":
    print(Solution().alienOrder(["wrt","wrf","er","ett","rftt"]))
    print(Solution().alienOrder(["zy","zx"]))
    print(Solution().alienOrder(["abc","ab"]))
    