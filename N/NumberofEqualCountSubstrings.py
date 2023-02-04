'''
-Medium-
$$$

You are given a 0-indexed string s consisting of only lowercase English letters, and an integer count. A substring of s is said to be an equal count substring if, for each unique letter in the substring, it appears exactly count times in the substring.

Return the number of equal count substrings in s.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: s = "aaabcbbcc", count = 3
Output: 3
Explanation:
The substring that starts at index 0 and ends at index 2 is "aaa".
The letter 'a' in the substring appears exactly 3 times.
The substring that starts at index 3 and ends at index 8 is "bcbbcc".
The letters 'b' and 'c' in the substring appear exactly 3 times.
The substring that starts at index 0 and ends at index 8 is "aaabcbbcc".
The letters 'a', 'b', and 'c' in the substring appear exactly 3 times.
Example 2:

Input: s = "abcd", count = 2
Output: 0
Explanation:
The number of times each letter appears in s is less than count.
Therefore, no substrings in s are equal count substrings, so return 0.
Example 3:

Input: s = "a", count = 5
Output: 0
Explanation:
The number of times each letter appears in s is less than count.
Therefore, no substrings in s are equal count substrings, so return 0
 

Constraints:

1 <= s.length <= 3 * 104
1 <= count <= 3 * 104
s consists only of lowercase English letters.


'''
from collections import Counter

class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        n = len(s)
        ans, l, r = 0, 0, 0
        cnt = [0]*26
        while r < n:
            cnt[ord(s[r])-ord('a')] += 1
            r += 1
            while any(i > count for i in cnt):
                cnt[ord(s[l])-ord('a')] -= 1
                l += 1
            if all(i == count for i in cnt if i > 0):
                ans += 1
        while l < n:
            cnt[ord(s[l])-ord('a')] -= 1
            # print(l, s[l], ans, cnt)
            l += 1
            t = [i == count for i in cnt if i > 0]
            if t and all(t):
                ans += 1
        return ans 

    def equalCountSubstrings2(self, s: str, count: int) -> int:
        n = len(s)
        if count > n:
            return 0
        counter = [[0] * 26 for _ in range(n + 1)]

        def check(i, j):
            c1 = counter[i]
            c2 = counter[j + 1]
            for k in range(26):
                if c2[k] == 0 or c1[k] == c2[k]:
                    continue
                if c2[k] - c1[k] != count:
                    return False
            return True

        ans = 0
        for i, c in enumerate(s):
            idx = ord(c) - ord('a')
            for j in range(26):
                counter[i + 1][j] = counter[i][j]
            counter[i + 1][idx] = counter[i][idx] + 1
            l = 0
            for _ in range(26):
                l += count
                j = i - l + 1
                if j < 0:
                    break
                ans += check(j, i)
        return ans

    def equalCountSubstrings3(self, s: str, count: int) -> int:
        # Sliding window
        maxUnique = len(set(s))
        ans = 0

        for unique in range(1, maxUnique + 1):
            windowSize = unique * count
            lettersCount = Counter()
            uniqueCount = 0
            for i, c in enumerate(s):
                lettersCount[c] += 1
                if lettersCount[c] == count:
                    uniqueCount += 1
                if i >= windowSize:
                    lettersCount[s[i - windowSize]] -= 1
                    if lettersCount[s[i - windowSize]] == count - 1:
                        uniqueCount -= 1
                ans += uniqueCount == unique

        return ans



                  


if __name__ == "__main__":
    print(Solution().equalCountSubstrings(s = "aaabcbbcc", count = 3))
    print(Solution().equalCountSubstrings2(s = "aaabcbbcc", count = 3))
    print(Solution().equalCountSubstrings(s = "aaabcdbbcc", count = 3))
    print(Solution().equalCountSubstrings2(s = "aaabcdbbcc", count = 3))
    print(Solution().equalCountSubstrings(s = "abcd", count = 2))
    print(Solution().equalCountSubstrings(s = "a", count = 5))