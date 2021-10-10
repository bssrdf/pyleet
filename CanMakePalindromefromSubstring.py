'''
-Medium-
*Prefix Sum*

You are given a string s and array queries where queries[i] = [lefti, righti, ki]. 
We may rearrange the substring s[lefti...righti] for each query and then choose 
up to ki of them to replace with any lowercase English letter.

If the substring is possible to be a palindrome string after the operations 
above, the result of the query is true. Otherwise, the result is false.

Return a boolean array answer where answer[i] is the result of the ith query 
queries[i].

Note that each letter is counted individually for replacement, so if, 
for example s[lefti...righti] = "aaa", and ki = 2, we can only replace two 
of the letters. Also, note that no query modifies the initial string s.

 

Example :

Input: s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
Output: [true,false,false,true,true]
Explanation:
queries[0]: substring = "d", is palidrome.
queries[1]: substring = "bc", is not palidrome.
queries[2]: substring = "abcd", is not palidrome after replacing only 1 character.
queries[3]: substring = "abcd", could be changed to "abba" which is palidrome. Also this can be changed to "baab" first rearrange it "bacd" then replace "cd" with "ab".
queries[4]: substring = "abcda", could be changed to "abcba" which is palidrome.
Example 2:

Input: s = "lyb", queries = [[0,1,0],[2,2,1]]
Output: [false,true]
 

Constraints:

1 <= s.length, queries.length <= 10^5
0 <= lefti <= righti < s.length
0 <= ki <= s.length
s consists of lowercase English letters.


'''

from typing import List
from collections import Counter
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n, m = len(s), len(queries)
        res = [False]*m
        preSum1 = [[0]*n for _ in range(26)]
        preSum = [[0]*(n+1) for _ in range(26)]
        for i in range(n):
            idx = ord(s[i]) - ord('a')
            preSum1[idx][i] = 1 #cnt[idx]
        for j in range(26):    
            for i in range(1,n+1):
                preSum[j][i] = preSum[j][i-1] + preSum1[j][i-1] 
        for i in range(m):
            l, r, k = queries[i]
            if r == l: 
                res[i] = True
                continue
            odd = 0
            for j in range(26):
                cnt = preSum[j][r+1]-preSum[j][l] 
                if cnt % 2 == 1:
                    odd += 1
            res[i] = odd // 2 <= k
        return res
    
    def canMakePaliQueries2(self, s: str, queries: List[List[int]]) -> List[bool]:
        n, m = len(s), len(queries)
        N = 26
        a = ord('a')
        dp = [[0] * N]
        for i in range(1, len(s)+1):
            new = dp[i-1][:]
            j = ord(s[i-1]) - a
            new[j] += 1
            dp.append(new)
        res = [False]*m
        for i in range(m):
            l, r, k = queries[i]
            if r == l: 
                res[i] = True
                continue
            odd = 0
            for j in range(26):
                cnt = dp[r+1][j]-dp[l][j] 
                if cnt % 2 == 1:
                    odd += 1
            res[i] = odd // 2 <= k
        return res

    def canMakePaliQueries3(self, s: str, queries: List[List[int]]) -> List[bool]:
        N = 26
        a = ord('a')
        dp = [[0] * N]
        for i in range(1, len(s)+1):
            new = dp[i-1][:]
            j = ord(s[i-1]) - a
            new[j] += 1
            dp.append(new)
        print(len(dp), len(dp[0]))
        ans = []
        for l, r, k in queries:
            L = dp[l]
            R = dp[r+1]
            ans.append(sum((R[i] - L[i]) & 1 for i in range(N)) // 2 <= k)
        return ans
    
    def canMakePaliQueries4(self, s: str, queries: List[List[int]]) -> List[bool]:
        l, m = len(s), 0
        presum = [0] * (l+1)
        for i in range(l):
            m ^= (1 << (ord(s[i]) - ord('a')))
            presum[i+1] = m
  
        rst, mask = [], 0x3ffffff
        for st, end, k in queries:
            bi = (presum[end+1] ^ presum[st]) & mask
            rst.append(bin(bi).count('1')//2 <= k)
        return rst



if __name__ == "__main__":
    print(Solution().canMakePaliQueries(s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]))
    print(Solution().canMakePaliQueries2(s = "abcda", queries = [[3,3,0],
    [1,2,0],[0,3,1],[0,3,2],[0,4,1]]))
    print(Solution().canMakePaliQueries3(s = "abcda", queries = [[3,3,0],
    [1,2,0],[0,3,1],[0,3,2],[0,4,1]]))
