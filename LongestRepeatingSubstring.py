'''

-Medium-


Given a string S, find out the length of the longest repeating substring(s). Return 0 if no 
repeating substring exists.

Example 1:

Input: “abcd”

Output: 0

Explanation: There is no repeating substring.

Example 2:

Input: “abbaba”

Output: 2

Explanation: The longest repeating substrings are “ab” and “ba”, each of which occurs twice.

Example 3:

Input: “aabcaabdaab”

Output: 3

Explanation: The longest repeating substring is “aab”, which occurs 3 times.

Example 4:

Input: “aaaaa”

Output: 4

Explanation: The longest repeating substring is “aaaa”, which occurs twice.

Note:

The string S consists of only lowercase English letters from 'a' - 'z'.
1 <= S.length <= 1500


'''
from collections import defaultdict

class Node(object):
    def __init__(self):        
        self.children = [None]*26       


class Solution(object):
    def longestRepeatingSubstring(self, s):
        n, m = len(s), set()
        #for i in range(n):
        #    m.add(s[:i+1])
        res = 0
        for i in range(n):
            for j in range(i,n):
                if s[i:j+1] in m:
                    res = max(res, j+1-i)
                else:
                    m.add(s[i:j+1])
        return res

    def longestRepeatingSubstring2(self, s):

        n, m = len(s), set()
        #for i in range(n):
        #    m.add(s[:i+1])
        root = Node()
        res = 0
        for i in range(n):
            cur = root
            for j in range(i,n):
                idx = ord(s[j])-ord('a')
                if cur.children[idx]:
                    res = max(res, j+1-i)
                else:
                    cur.children[idx] = Node()
                cur = cur.children[idx]
        return res

    def longestRepeatingSubstringDP(self, S: str) -> int:
        ans = 0
        for i in range(1, len(S)):
            if ans >= len(S)-i: 
                break 
                
            tmp = 0
            for x, y in zip(S[i:],S[:-i]):
                if x == y:
                    tmp += 1 
                    ans = max(ans, tmp)
                else:
                    tmp = 0 
            
        return ans
    
    def longestRepeatingSubstringDP2(self, S: str) -> int:

        # 我们先定义dp[i][j]为分别以第i个字符和第j个字符结尾的substring有相同共同后缀的最大长度。
        # 因此，我们也要求i>j。
        # 我们注意到，当S[i] != S[j], 那么dp[i][j] = 0， 否则dp[i][j] = dp[i-1][j-1] + 1。
        # 这就是我们的状态转移方程。

        # dp[i][j] = dp[i-1][j-1] + 1 ----------- S[i] == S[j]
        # dp[i][j] = 0                ----------- S[i] != S[j]

        # 我们更新dp[i][j]的最大值，就可以得到最后的答案。
        ans, n = 0, len(S)
        dp = [[0]*(n+1) for _ in range(n+1)] 
        for i in range(1, n+1):
            for j in range(1, i):
                if S[i-1] == S[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = 0 
        for i in range(n+1):
           print(dp[i])
        return ans

import random
if __name__ == "__main__":
    print(Solution().longestRepeatingSubstring("abbaba"))
    print(Solution().longestRepeatingSubstring("aaaaa"))
    print(Solution().longestRepeatingSubstring("aabcaabdaab"))
    print(Solution().longestRepeatingSubstringDP("abbaba"))
    print(Solution().longestRepeatingSubstringDP("aaaaa"))
    print(Solution().longestRepeatingSubstringDP("aabcaabdaab"))
    print(Solution().longestRepeatingSubstringDP2("aabcaabdaab"))
    s = ''
    for i in range(1500):
        s += chr(random.randint(0,25)+ord('a'))
    #print(Solution().longestRepeatingSubstringDP(s))
    #print(Solution().longestRepeatingSubstringDP2(s))
    #print(Solution().longestRepeatingSubstring2(s))
    #print(Solution().longestRepeatingSubstring(s))
    
    
