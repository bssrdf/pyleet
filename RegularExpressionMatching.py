'''
-Hard-

Given an input string (s) and a pattern (p), implement regular expression matching 
with support for '.' and '*' where: 

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by 
repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it 
matches "aab".
Example 5:

Input: s = "mississippi", p = "mis*is*p*."
Output: false
 

Constraints:

0 <= s.length <= 20
0 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous 
valid character to match.

'''


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        """
        我们也可以用 DP 来解，定义一个二维的 DP 数组，其中 dp[i][j] 表示 s[0,i) 和 p[0,j) 
        是否 match，然后有下面三种情况(下面部分摘自这个帖子)：

        1.  P[i][j] = P[i - 1][j - 1], if p[j - 1] != '*' && (s[i - 1] == p[j - 1] || p[j - 1] == '.');
        2.  P[i][j] = P[i][j - 2], if p[j - 1] == '*' and the pattern repeats for 0 times;
        3.  P[i][j] = P[i - 1][j] && (s[i - 1] == p[j - 2] || p[j - 2] == '.'), if p[j - 1] 
            == '*' and the pattern repeats for at least 1 times.

        Here are some conditions to figure out, then the logic can be very straightforward.

        1, If p.charAt(j) == s.charAt(i) :  dp[i][j] = dp[i-1][j-1];
        2, If p.charAt(j) == '.' :          dp[i][j] = dp[i-1][j-1];
        3, If p.charAt(j) == '*': 
        here are two sub conditions:
               1   if p.charAt(j-1) != s.charAt(i) : dp[i][j] = dp[i][j-2]  //in this case, 
                                                                a* only counts as empty
               2   if p.charAt(j-1) == s.charAt(i) or p.charAt(j-1) == '.':
                        dp[i][j] = dp[i-1][j]    //in this case, a* counts as multiple a 
                     or dp[i][j] = dp[i][j-1]   // in this case, a* counts as single a
                     or dp[i][j] = dp[i][j-2]   // in this case, a* counts as empty
        https://leetcode.com/problems/regular-expression-matching/discuss/191830/Java-DP-solution-beats-100-with-explanation

        s='aab', p='c*a*b'

              c * a * b 
            0 1 2 3 4 5
          0 y n y n y n
        a 1 n n n y y n
        a 2 n n n n y n
        b 3 n n n n n y
        """

        m, n = len(s), len(p)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True        
        for j in range(1, n+1):
            if p[j-1] == '*' and dp[0][j-2]:
                dp[0][j] = True
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]  
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or ((s[i - 1] == p[j - 2]  
                                                or p[j - 2] == '.') 
                                                and dp[i-1][j])
        for i in range(m+1):
            print(dp[i])               
        return dp[m][n]
        
if __name__ == "__main__":
    #print(Solution().isMatch("aab", "c*a*b"))
    '''
          c * a *  
        0 1 2 3 4 
      0 y n y n y 
    a 1 n n n y y 
    a 2 n n n n y 
    a 3 n n n n y
    a 4 n n n n y
    '''
    print(Solution().isMatch("aaaa", "c*a*"))
    '''
          c * a *  
        0 1 2 3 4 
      0 y n y n y 
    b 1 n n n n n 
    a 2 n n n n n 
    a 3 n n n n n
    a 4 n n n n n
    '''
    print(Solution().isMatch("baaa", "c*a*"))
    #print(Solution().isMatch("aaa","ab*a*c*a"))
    #print(Solution().isMatch("","b*c*"))