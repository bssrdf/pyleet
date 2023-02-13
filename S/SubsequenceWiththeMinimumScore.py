'''

-Hard-

*DP*
*Greedy*
*Two Pointers*

You are given two strings s and t.

You are allowed to remove any number of characters from the string t.

The score string is 0 if no characters are removed from the string t, otherwise:

Let left be the minimum index among all removed characters.
Let right be the maximum index among all removed characters.
Then the score of the string is right - left + 1.

Return the minimum possible score to make t a subsequence of s.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abacaba", t = "bzaa"
Output: 1
Explanation: In this example, we remove the character "z" at index 1 (0-indexed).
The string t becomes "baa" which is a subsequence of the string "abacaba" and the score is 1 - 1 + 1 = 1.
It can be proven that 1 is the minimum score that we can achieve.
Example 2:

Input: s = "cde", t = "xyz"
Output: 3
Explanation: In this example, we remove characters "x", "y" and "z" at indices 0, 1, and 2 (0-indexed).
The string t becomes "" which is a subsequence of the string "cde" and the score is 2 - 0 + 1 = 3.
It can be proven that 3 is the minimum score that we can achieve.
 

Constraints:

1 <= s.length, t.length <= 105
s and t consist of only lowercase English letters.



'''



class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        def isSubseqence(s1, s2):
            i, j = 0, 0
            for i in range(len(s1)):
                if s1[i] == s2[j]:
                    j += 1
                if j == len(s2): return True
            return False

        print(isSubseqence(s, t))
        return 0        
    
    def minimumScore2(self, s: str, t: str) -> int:
        '''
        More explanation on this problem:
        We want to minimize the difference between the last index we delete k and 
        the first one we delete j. There is no harm in deleting extra indices in-between, 
        so we can opt to delete all if we so choose since we only want t to be a 
        subsequence of s.
        '''
        m, n = len(s), len(t)
        i, k = m-1, n-1
        dp = [-1]*n # dp has size of len(t)
        while i >= 0 and k >= 0:
            if s[i] == t[k]:
                dp[k] = i # dp[k] is the index i where suffix s[i:] contains t[k:] as subsequence
                          # dp[k] == -1 if t[k:] is NOT a subsequence of any suffix of s
                k -= 1
            i -= 1
        ans = k + 1
        i, j = 0, 0
        print(dp, k)
        while i < m and j < n and ans > 0:
            if s[i] == t[j]: # if we find a match between prefix s[:i] and t[:j]
                # we need to find the longest suffix s[dp[k]:] matching t[k:]   
                # and the first k where dp[k] > i is the longest one 
                while k < n and dp[k] <= i:
                    k += 1
                j += 1
                ans = min(ans, k - j)
            i += 1
        return ans  


            



if __name__ == '__main__':
    # print(Solution().minimumScore(s = "abacaba", t = "bzaa"))
    # print(Solution().minimumScore(s = "abacaba", t = "baa"))
    # print(Solution().minimumScore2(s = "abacaba", t = "bzaa"))
    print(Solution().minimumScore2(s = "abaaaba", t = "aababab"))