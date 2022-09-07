'''
-Medium-

A wonderful string is a string where at most one letter appears an odd number of times.

For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
Given a string word that consists of the first ten lowercase English letters ('a' through 'j'), return the number of wonderful non-empty substrings in word. If the same substring appears multiple times in word, then count each occurrence separately.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: word = "aba"
Output: 4
Explanation: The four wonderful substrings are underlined below:
- "aba" -> "a"
- "aba" -> "b"
- "aba" -> "a"
- "aba" -> "aba"
Example 2:

Input: word = "aabb"
Output: 9
Explanation: The nine wonderful substrings are underlined below:
- "aabb" -> "a"
- "aabb" -> "aa"
- "aabb" -> "aab"
- "aabb" -> "aabb"
- "aabb" -> "a"
- "aabb" -> "abb"
- "aabb" -> "b"
- "aabb" -> "bb"
- "aabb" -> "b"
Example 3:

Input: word = "he"
Output: 2
Explanation: The two wonderful substrings are underlined below:
- "he" -> "h"
- "he" -> "e"
 

Constraints:

1 <= word.length <= 105
word consists of lowercase English letters from 'a' to 'j'.


'''


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        mask, res = 0, 0
        n = ord(max(word)) - ord('a') + 1
        bitall = (1<<n)-1
        dp = {0:1}
        for i in range(len(word)):
            mask ^= 1 << (ord(word[i]) - 97)
            # print(bin(mask), s[i])
            for j in range(n+1):
                check_mask = bitall & (mask ^ (1 << j))
                # print(f'{mask:010b}', f'{check_mask:010b}', j, s[i])
                res += dp.get(check_mask, 0)
            dp[mask] = dp.get(mask, 0) + 1
        return res
    
    def wonderfulSubstrings2(self, word: str) -> int:
        # solution similar to 1542. Find Longest Awesome Substring
        # and 1371. Find the Longest Substring Containing Vowels in Even Counts
        mask, res = 0, 0
        n = ord(max(word)) - ord('a') + 1
        bitall = (1<<n)-1
        dp = [0]*(bitall+1)
        dp[0] = 1
        for i in range(len(word)):
            mask ^= 1 << (ord(word[i]) - 97)
            for j in range(n+1):
                check_mask = bitall & (mask ^ (1 << j))
                res += dp[check_mask]
            dp[mask] += 1
        return res

if __name__ == "__main__":
    print(Solution().wonderfulSubstrings(word = "aba"))
    print(Solution().wonderfulSubstrings(word = "aabb"))