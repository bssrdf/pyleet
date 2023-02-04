'''
-Medium-

*BFS*

*DFS*

*Memoization*

Given a string s and a set of n substrings. You are supposed to remove every instance of 
those n substrings from s so that s is of the minimum length and output this minimum length.

样例
Example 1:

Input:
"ccdaabcdbb"
["ab","cd"]
Output:
2
Explanation: 
ccdaabcdbb -> ccdacdbb -> cacdbb -> cabb -> cb (length = 2)
Example 2:

Input:
"abcabd"
["ab","abcd"]
Output:
0
Explanation: 
abcabd -> abcd -> "" (length = 0)

'''
import re

from collections import deque

def findall(p, s):
    '''Yields all the positions of
    the pattern p in the string s.'''
    i = s.find(p)
    while i != -1:
        yield i
        i = s.find(p, i+1)

class Solution:
    """
    @param s: a string
    @param dict: a set of n substrings
    @return: the minimum length
    """
    def minLengthDFS(self, s, dict):
        # write your code here
        memo = {}
        def dfs(str):
            if not str: return 0
            if str in memo: return memo[str]
            n = len(str)
            for pat in dict:
                for i in findall(pat, str):
                    news = str[:i]+str[i+len(pat):]
                    n = min(n, dfs(news))
            memo[str] = n
            return memo[str]
        return dfs(s)

    def minLength(self, s, dict):
        # write your code here
        q = deque([s])
        res = len(s)
        memo = set([s])
        while q:
            cur = q.popleft()
            res = min(res, len(cur))
            for pat in dict:
                for i in findall(pat, cur):
                    news = cur[:i]+cur[i+len(pat):]
                    if news not in memo and len(news) < res:
                        memo.add(news)
                        q.append(news)
        return res
                

if __name__ == "__main__":
    print(Solution().minLengthDFS("ccdaabcdbb", ["ab","cd"]))
    print(Solution().minLengthDFS("abcabd", ["ab","abcd"]))
    print(Solution().minLength("ccdaabcdbb", ["ab","cd"]))
    print(Solution().minLength("abcabd", ["ab","abcd"]))
    s  = "wyewyruyiuysfhkjahjreiwoauifhjsajfhauwueihfjaskfjhaeuiwaeadjsakhkjhwaeiuwadhsajkhfkjafjiwueuwe"
    dic = ["fh","jh","yu","ab","bc","cd","sa","fjaskfjha","aeu","fjak","fjhaeuiwae","aeuiw","eu","iuif","yau","sfo","hkw","askadjs","jahjrei"]
    print(Solution().minLengthDFS(s, dic))
    print(Solution().minLength(s, dic))
    
    
