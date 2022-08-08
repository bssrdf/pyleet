'''
-Medium-


You are given a string s consisting of lowercase letters and an integer k. We call a string t ideal if the following conditions are satisfied:

t is a subsequence of the string s.
The absolute difference in the alphabet order of every two adjacent letters in t is less than or equal to k.
Return the length of the longest ideal string.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

Note that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of 'a' and 'z' is 25, not 1.

 

Example 1:

Input: s = "acfgbd", k = 2
Output: 4
Explanation: The longest ideal string is "acbd". The length of this string is 4, so 4 is returned.
Note that "acfgbd" is not ideal because 'c' and 'f' have a difference of 3 in alphabet order.
Example 2:

Input: s = "abcd", k = 3
Output: 4
Explanation: The longest ideal string is "abcd". The length of this string is 4, so 4 is returned.
 

Constraints:

1 <= s.length <= 105
0 <= k <= 25
s consists of lowercase English letters.



'''


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[0]*26 for _ in range(n+1)]
        dp[1][ord(s[0]) - ord('a')] = 1 
        for i in range(2, n+1):
            c = ord(s[i-1]) - ord('a')
            for j in range(26):
                if abs(c - j) <= k:
                    dp[i][c] = max(dp[i][c], dp[i-1][j]+1)
                if j != c: 
                    dp[i][j] = dp[i-1][j]
        return max(dp[n])
    
    def longestIdealString2(self, s: str, k: int) -> int:
        n = len(s)
        dp0, dp1 = [0]*26, [0]*26
        dp0[ord(s[0]) - ord('a')] = 1 
        for i in range(1, n):
            c = ord(s[i]) - ord('a')
            for j in range(26):
                if abs(c - j) <= k:
                    dp1[c] = max(dp1[c], dp0[j]+1)
                if j != c: 
                    dp1[j] = dp0[j]
            dp0, dp1 = dp1, dp0
        return max(dp0)
    
    def longestIdealString3(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0]*26
        dp[ord(s[0]) - ord('a')] = 1 
        for i in range(1, n):
            c = ord(s[i]) - ord('a')
            mi = 0
            for j in range(max(c-k,0), min(c+k+1, 26)):
                mi = max(mi, dp[j])
            dp[c] = mi + 1
        return max(dp)

    
    def longestIdealString4(self, s: str, k: int) -> int:
        # fastest
        n = len(s)
        dp = [0]*26
        dp[ord(s[0]) - ord('a')] = 1 
        for i in range(1, n):
            c = ord(s[i]) - ord('a')
            # using python's built-in max function to find maximum 
            # is much faster than fining it mannually with a for-loop
            dp[c] = max(dp[max(c-k,0):min(c+k+1, 26)]) + 1
        return max(dp)

if __name__ == "__main__":
    print(Solution().longestIdealString(s = "acfgbd", k = 2))
    print(Solution().longestIdealString(s = "abcd", k = 3))
    print(Solution().longestIdealString(s = "pvjcci", k = 4))
    print(Solution().longestIdealString(s = "lkpkxcigcs", k = 6))


    print(Solution().longestIdealString2(s = "acfgbd", k = 2))
    print(Solution().longestIdealString2(s = "abcd", k = 3))
    print(Solution().longestIdealString2(s = "pvjcci", k = 4))
    print(Solution().longestIdealString2(s = "lkpkxcigcs", k = 6))


    print(Solution().longestIdealString3(s = "acfgbd", k = 2))
    print(Solution().longestIdealString3(s = "abcd", k = 3))
    print(Solution().longestIdealString3(s = "pvjcci", k = 4))
    print(Solution().longestIdealString3(s = "lkpkxcigcs", k = 6))
        