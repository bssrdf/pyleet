'''
-Medium-
$$$


You are given a 0-indexed string s consisting of only lowercase English letters. Return the number of substrings in s that begin and end with the same character.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: s = "abcba"
Output: 7
Explanation:
The substrings of length 1 that start and end with the same letter are: "a", "b", "c", "b", and "a".
The substring of length 3 that starts and ends with the same letter is: "bcb".
The substring of length 5 that starts and ends with the same letter is: "abcba".
Example 2:

Input: s = "abacad"
Output: 9
Explanation:
The substrings of length 1 that start and end with the same letter are: "a", "b", "a", "c", "a", and "d".
The substrings of length 3 that start and end with the same letter are: "aba" and "aca".
The substring of length 5 that starts and ends with the same letter is: "abaca".
Example 3:

Input: s = "a"
Output: 1
Explanation:
The substring of length 1 that starts and ends with the same letter is: "a".
 

Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters.



'''


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = [0]*26
        res = 0
        for c in s:
            i = ord(c) - ord('a')
            res += cnt[i] + 1
            cnt[i] += 1
        return res

    def numberOfSubstrings2(self, s: str) -> int:
        counter = [0] * 26
        ans = 0
        for c in s:
            i = ord(c) - ord('a')
            counter[i] += 1
            ans += counter[i] # number of new substrings ending at c is counter[i]
        return ans





if __name__ == "__main__":
    print(Solution().numberOfSubstrings(s = "abcba"))
    print(Solution().numberOfSubstrings(s = "abacad"))
    print(Solution().numberOfSubstrings(s = "a"))
    print(Solution().numberOfSubstrings(s = "aabbcaa"))
    print(Solution().numberOfSubstrings2(s = "aabbcaa"))