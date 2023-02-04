'''

-Hard-
$$$
*DP*

Given a string s, encode the string such that its encoded length is the shortest.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. k should be a positive integer.

If an encoding process does not make the string shorter, then do not encode it. If there are several solutions, return any of them.

 

Example 1:

Input: s = "aaa"
Output: "aaa"
Explanation: There is no way to encode it such that it is shorter than the input string, so we do not encode it.
Example 2:

Input: s = "aaaaa"
Output: "5[a]"
Explanation: "5[a]" is shorter than "aaaaa" by 1 character.

Example 3:

Input: s = "aaaaaaaaaa"
Output: "10[a]"
Explanation: "a9[a]" or "9[a]a" are also valid solutions, both of them have the same length = 5, which is the same as "10[a]".
 

Example 4:

Input: s = "aabcaabcd"
Output: "2[aabc]d" 


Example 5:

Input: s = "abbbabbbcabbbabbbc"
Output: "2[2[abbb]c]" 

Constraints:

1 <= s.length <= 150
s consists of only lowercase English letters.


'''


class Solution:
 
   def encode(self, s: str) -> str:
        n = len(s)
        # dp[i][j] := shortest encoded string of s[i..j]
        dp = [['' for _ in range(n)] for _ in range(n)]
        def enc(s, i, j):
            if dp[i][j]:
                return dp[i][j]
            cur = s[i:j+1]
            dp[i][j] = cur
            if len(dp[i][j]) < 5: return dp[i][j]
            # try all possible partitions
            for k in range(i, j):
                l = enc(s, i, k)
                r = enc(s, k+1, j)
                if len(l) + len(r) < len(dp[i][j]):
                    dp[i][j] = l + r
            # try to compress the string
            for k in range(i, j+1):
                pattern = s[i:k+1]
                if len(cur) % len(pattern) == 0 and cur.replace(pattern, '') == '':
                    candidate = str(len(cur) // len(pattern)) + '[' + enc(s, i ,k) + ']'
                    if len(candidate) < len(dp[i][j]):
                        dp[i][j] = candidate 
            return dp[i][j]
        return enc(s, 0, n-1)
                



       
if __name__ == "__main__":
    print(Solution().encode(s = "aaa"))
    print(Solution().encode(s = "aaaaaaaaaa"))
    print(Solution().encode(s = "aabcaabcd"))
    print(Solution().encode(s = "abbbabbbcabbbabbbc"))

