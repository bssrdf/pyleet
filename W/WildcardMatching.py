'''

-Hard-

*DP*
*Greedy*

Given an input string (s) and a pattern (p), implement wildcard pattern matching 
with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input: s = "adceb", p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches 
the substring "dce".
Example 5:

Input: s = "acdcb", p = "a*c?b"
Output: false
 

Constraints:

0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.

'''

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        """
        这道题通配符外卡匹配问题还是小有难度的，有特殊字符 ‘*’ 和 ‘?’，其中 ‘?’ 能代替任何字符，
        ‘*’ 能代替任何字符串，注意跟另一道 Regular Expression Matching 正则匹配的题目区分开来。
        两道题的星号的作用是不同的，注意对比区分一下。这道题最大的难点，就是对于星号的处理，可以
        匹配任意字符串，简直像开了挂一样，就是说在星号对应位置之前，不管你s中有任何字符串，我大星
        号都能匹配你，主角光环啊。但即便叼如斯的星号，也有其处理不了的问题，那就是一旦p中有s中不
        存在的字符，那么一定无法匹配，因为星号只能增加字符，不能消除字符，再有就是星号一旦确定了
        要匹配的字符串，对于星号位置后面的匹配情况也就鞭长莫及了。所以p串中星号的位置很重要，用 
        jStar 来表示，还有星号匹配到s串中的位置，使用 iStart 来表示，这里 iStar 和 jStar 均初
        始化为 -1，表示默认情况下是没有星号的。然后再用两个变量i和j分别指向当前s串和p串中遍历到
        的位置。

        开始进行匹配，若i小于s串的长度，进行 while 循环。若当前两个字符相等，或着p中的字符是问号，
        则i和j分别加1。若 p[j] 是星号，要记录星号的位置，jStar 赋为j，此时j再自增1，iStar 赋为i。
        若当前 p[j] 不是星号，并且不能跟 p[i] 匹配上，此时就要靠星号了，若之前星号没出现过，那么
        就直接跪，比如 s = "aa" 和 p = "c*"，此时 s[0] 和 p[0] 无法匹配，虽然 p[1] 是星号，但
        还是跪。如果星号之前出现过，可以强行续一波命，比如 s = "aa" 和 p = "*c"，当发现 s[1] 和 
        p[1] 无法匹配时，但是好在之前 p[0] 出现了星号，把 s[1] 交给 p[0] 的星号去匹配。至于如何
        知道之前有没有星号，这时就能看出 iStar 的作用了，因为其初始化为 -1，而遇到星号时，其就会
        被更新为i，只要检测 iStar 的值，就能知道是否可以使用星号续命。虽然成功续了命，匹配完了s中
        的所有字符，但是之后还要检查p串，此时没匹配完的p串里只能剩星号，不能有其他的字符，将连续的
        星号过滤掉，如果j不等于p的长度，则返回 false，

        """

        i, j, iStar, jStar = 0,  0, -1,  -1
        m, n = len(s), len(p)
        while i < m:
            if j < n and (s[i] == p[j] or p[j] == '?'):
                i += 1 
                j += 1
            elif j < n and p[j] == '*':
                iStar, jStar = i, j
                j += 1
            elif iStar >= 0: # now s[i] != p[j] and p[j] is not * or ?
                             # keep using prior * to match s[i] 
                i, j = iStar, jStar + 1
                iStar += 1
            else: return False
        while j < n and p[j] == '*': j += 1
        return j == n

    def isMatchDP(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        """
        对于这种玩字符串的题目，动态规划 Dynamic Programming 是一大神器，因为字符串跟其子串之间的
        关系十分密切，正好适合 DP 这种靠推导状态转移方程的特性。那么先来定义dp数组吧，使用一个二维 
        dp 数组，其中 dp[i][j] 表示 s中前i个字符组成的子串和p中前j个字符组成的子串是否能匹配。大
        小初始化为 (m+1) x (n+1)，加1的原因是要包含 dp[0][0] 的情况，因为若s和p都为空的话，也应
        该返回 true，所以也要初始化 dp[0][0] 为 true。还需要提前处理的一种情况是，当s为空，p为连
        续的星号时的情况。由于星号是可以代表空串的，所以只要s为空，那么连续的星号的位置都应该为true，
        所以先将连续星号的位置都赋为 true。然后就是推导一般的状态转移方程了，如何更新 dp[i][j]，
        首先处理比较 tricky 的情况，若p中第j个字符是星号，由于星号可以匹配空串，所以如果p中的前 
        j-1 个字符跟s中前i个字符匹配成功了（ dp[i][j-1] 为true）的话，则 dp[i][j] 也能为 true。
        或者若p中的前j个字符跟s中的前i-1个字符匹配成功了（ dp[i-1][j] 为true ）的话，则 dp[i][j] 
        也能为 true（因为星号可以匹配任意字符串，再多加一个任意字符也没问题）。若p中的第j个字符不是
        星号，对于一般情况，假设已经知道了s中前 i-1 个字符和p中前 j-1 个字符的匹配情况（即 
        dp[i-1][j-1] ），现在只需要匹配s中的第i个字符跟p中的第j个字符，若二者相等（s[i-1] == p[j-1]），
        或者p中的第j个字符是问号（ p[j-1] == '?' ），再与上 dp[i-1][j-1] 的值，就可以更新 
        dp[i][j] 了，
        """
        m, n = len(s), len(p)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True
        for i in range(1, n+1):
            if p[i - 1] == '*': dp[0][i] = dp[0][i - 1]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:
                    dp[i][j] = (s[i - 1] == p[j - 1] or p[j - 1] == '?') and dp[i - 1][j - 1]
        return dp[m][n]

if __name__ == "__main__":
    print(Solution().isMatch("adceb", "*a*b"))
    print(Solution().isMatchDP("adceb", "*a*b"))