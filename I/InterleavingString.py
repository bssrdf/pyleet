'''
-Medium-
*DP*
*BFS*


Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into 
non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

 

Example 1:


Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true
 

Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.
 

Follow up: Could you solve it using only O(s2.length) additional memory space?

'''

from collections import deque

class Solution(object):
    def isInterleaveDP(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n1, n2 = len(s1), len(s2)
        if n1 + n2 != len(s3): return False
        dp = [[False for _ in range(n2+1)] for _ in range(n1+1)]
        dp[0][0] = True # both s1 and s2 are ''
        for i in range(1,n1+1):
            dp[i][0] = dp[i - 1][0] and (s1[i - 1] == s3[i - 1]) # s2 is ''
        for j in range(1,n2+1):
            dp[0][j] = dp[0][j - 1] and (s2[j - 1] == s3[j - 1]) # s1 is ''
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or  \
                           (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return dp[n1][n2]

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n1, n2 = len(s1), len(s2)
        if n1 + n2 != len(s3): return False
        visited = [[False for _ in range(n2+1)] for _ in range(n1+1)]
        queue = deque([(0,0)])
        visited[0][0] = True
        while queue:
            i, j = queue.popleft()
            if i == n1 and j == n2: return True
            if i < n1 and s1[i] == s3[i+j] and not visited[i+1][j]:
                visited[i+1][j] = True
                queue.append((i+1, j))
            if j < n2 and s2[j] == s3[i+j] and not visited[i][j+1]:
                visited[i][j+1] = True
                queue.append((i, j+1))
        return False

        


if __name__ == "__main__":
    print(Solution().isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"))