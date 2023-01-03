'''
-Medium-

You are given two strings s and t consisting of only lowercase English letters.

Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

 

Example 1:

Input: s = "coaching", t = "coding"
Output: 4
Explanation: Append the characters "ding" to the end of s so that s = "coachingding".
Now, t is a subsequence of s ("coachingding").
It can be shown that appending any 3 characters to the end of s will never make t a subsequence.
Example 2:

Input: s = "abcde", t = "a"
Output: 0
Explanation: t is already a subsequence of s ("abcde").
Example 3:

Input: s = "z", t = "abcde"
Output: 5
Explanation: Append the characters "abcde" to the end of s so that s = "zabcde".
Now, t is a subsequence of s ("zabcde").
It can be shown that appending any 4 characters to the end of s will never make t a subsequence.
 

Constraints:

1 <= s.length, t.length <= 105
s and t consist only of lowercase English letters.



'''


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0
        for i in range(len(s)):
            if s[i] == t[j]:
                j += 1
                if j == len(t):
                   return 0
            i += 1
        return len(t) - j 


if __name__=="__main__":
    print(Solution().appendCharacters(s = "coaching", t = "coding"))
    print(Solution().appendCharacters(s = "abcde", t = "a"))
    print(Solution().appendCharacters(s = "z", t = "abcde"))
        