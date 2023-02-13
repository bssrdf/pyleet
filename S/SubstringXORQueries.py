'''

-Medium-
*Robin Karp*
*Rolling Hash*
*Hash Table*

You are given a binary string s, and a 2D integer array queries where queries[i] = [firsti, secondi].

For the ith query, find the shortest substring of s whose decimal value, val, yields secondi when bitwise XORed with firsti. In other words, val ^ firsti == secondi.

The answer to the ith query is the endpoints (0-indexed) of the substring [lefti, righti] or [-1, -1] if no such substring exists. If there are multiple answers, choose the one with the minimum lefti.

Return an array ans where ans[i] = [lefti, righti] is the answer to the ith query.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: s = "101101", queries = [[0,5],[1,2]]
Output: [[0,2],[2,3]]
Explanation: For the first query the substring in range [0,2] is "101" which has a decimal value of 5, and 5 ^ 0 = 5, hence the answer to the first query is [0,2]. In the second query, the substring in range [2,3] is "11", and has a decimal value of 3, and 3 ^ 1 = 2. So, [2,3] is returned for the second query. 

Example 2:

Input: s = "0101", queries = [[12,8]]
Output: [[-1,-1]]
Explanation: In this example there is no substring that answers the query, hence [-1,-1] is returned.
Example 3:

Input: s = "1", queries = [[4,5]]
Output: [[0,0]]
Explanation: For this example, the substring in range [0,0] has a decimal value of 1, and 1 ^ 4 = 5. So, the answer is [0,0].
 

Constraints:

1 <= s.length <= 104
s[i] is either '0' or '1'.
1 <= queries.length <= 105
0 <= firsti, secondi <= 109




'''

from typing import List
from collections import defaultdict

class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        n, m = len(queries), len(s)
        mp = defaultdict(list)
        ans = [[-1, -1] for _ in range(n)]
        for i,(a, b) in enumerate(queries):
            mp[b^a].append(i)
        for l in range(1, 31):
            q, t = 2**(l-1), 0    
            for i in range(m):
                if i >= l:
                    t = 2*(t - int(s[i-l])*q) + int(s[i])
                else:
                    t = t*2 + int(s[i]) 
                if i >= l-1 and t in mp:
                    for k in mp[t]:
                        ans[k] = [i-l+1, i]  
                    mp.pop(t)
                    if not mp: return ans    
        return ans        
    
    def substringXorQueries2(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        n, m = len(queries), len(s)
        mp = defaultdict(list)
        ans = [[-1, -1] for _ in range(n)]
        for i,(a, b) in enumerate(queries):
            mp[b^a].append(i)
        for l in range(1, 31):
            q, t = 2**(l-1), 0                
            for i in range(min(l, m)):
                t = t*2 + int(s[i]) 
            if t in mp:
                for k in mp[t]:
                    ans[k] = [i-l+1, i]  
                mp.pop(t)
            for i in range(l, m):
                t = 2*(t - int(s[i-l])*q) + int(s[i])
                if t in mp:
                    for k in mp[t]:
                        ans[k] = [i-l+1, i]  
                    mp.pop(t)
                    if not mp: return ans
        return ans        
        




if __name__ == '__main__':
    print(Solution().substringXorQueries(s = "101101", queries = [[0,5],[1,2]]))
    print(Solution().substringXorQueries(s = "0101", queries = [[12,8]]))
    print(Solution().substringXorQueries(s = "1", queries = [[4,5]]))
    print(Solution().substringXorQueries2(s = "101101", queries = [[0,5],[1,2]]))