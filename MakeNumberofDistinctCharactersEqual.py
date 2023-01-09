'''

-Medium-

You are given two 0-indexed strings word1 and word2.

A move consists of choosing two indices i and j such that 0 <= i < word1.length and 0 <= j < word2.length and swapping word1[i] with word2[j].

Return true if it is possible to get the number of distinct characters in word1 and word2 to be equal with exactly one move. Return false otherwise.

 

Example 1:

Input: word1 = "ac", word2 = "b"
Output: false
Explanation: Any pair of swaps would yield two distinct characters in the first string, and one in the second string.
Example 2:

Input: word1 = "abcc", word2 = "aab"
Output: true
Explanation: We swap index 2 of the first string with index 0 of the second string. The resulting strings are word1 = "abac" and word2 = "cab", which both have 3 distinct characters.
Example 3:

Input: word1 = "abcde", word2 = "fghij"
Output: true
Explanation: Both resulting strings will have 5 distinct characters, regardless of which indices we swap.
 

Constraints:

1 <= word1.length, word2.length <= 105
word1 and word2 consist of only lowercase English letters.




'''

from collections import Counter

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        cnt1, cnt2 = Counter(word1), Counter(word2)
        for a in cnt1:            
            for b in cnt2:
                cnt1c = Counter(cnt1)
                cnt1c[a] -= 1
                if cnt1c[a] == 0:
                    cnt1c.pop(a)
                cnt2c = Counter(cnt2)
                cnt2c[b] -= 1
                if cnt2c[b] == 0:
                    cnt2c.pop(b)
                cnt2c[a] += 1
                cnt1c[b] += 1
                if len(cnt1c) == len(cnt2c):
                    return True
        return False









print(Solution().isItPossible(word1 = "abcde", word2 = "fghij"))
print(Solution().isItPossible(word1 = "abcc", word2 = "aab"))
print(Solution().isItPossible(word1 = "ac", word2 = "b"))
print(Solution().isItPossible(word1 = "ab", word2 = "abcc"))
