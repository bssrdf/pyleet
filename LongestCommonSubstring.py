'''

-Medium-
*DP*
*Suffix Tree*

Given two strings s and t, return the length of their longest common substring. If there 
is no common substring, return 0.


 

Example 1:

Input:  s = "xabxac", t = "abcabxabcd" 
Output: 4  
Explanation: The longest common substring is "abxa" and its length is 4.


Example 2:

Input: s = "xabxaabxa", t = "babxba" 
Output: 3  
Explanation: The longest common substring is "abx" and its length is 3.


Example 3:

Input: s = "pqrst", t = "uvwxyz" 
Output: 0  


Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.


'''

from SuffixTree import SuffixTree

class Solution(object):
    def longestCommonSubstring(self, s, t):
        m, n = len(s), len(t)
        dp = [[0]*(n+1) for _ in range(m+1)]
        ans = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                ans = max(ans, dp[i][j]) 
        return ans

    def longestCommonSubstring2(self, s, t):    
        suffix_tree = SuffixTree()
        suffix_tree.append_string(s)
        suffix_tree.append_string(t)
        lcs = suffix_tree.find_longest_common_substrings()
        return len(lcs[0])



if __name__ == "__main__":
    print(Solution().longestCommonSubstring(s = "xabxac", t = "abcabxabcd" ))
    print(Solution().longestCommonSubstring(s = "xabxaabxa", t = "babxba"  ))
    print(Solution().longestCommonSubstring(s = "pqrst", t = "uvwxyz"  ))
    print(Solution().longestCommonSubstring2(s = "xabxac", t = "abcabxabcd" ))
    print(Solution().longestCommonSubstring2(s = "xabxaabxa", t = "babxba"  ))
    print(Solution().longestCommonSubstring2(s = "pqrst", t = "uvwxyz"  ))
