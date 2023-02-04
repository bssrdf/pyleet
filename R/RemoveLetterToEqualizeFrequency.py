'''

-Easy-

You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and remove the letter at that index from word so that the frequency of every letter present in word is equal.

Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.

Note:

The frequency of a letter x is the number of times it occurs in the string.
You must remove exactly one letter and cannot chose to do nothing.
 

Example 1:

Input: word = "abcc"
Output: true
Explanation: Select index 3 and delete it: word becomes "abc" and each character has a frequency of 1.
Example 2:

Input: word = "aazz"
Output: false
Explanation: We must delete a character, so either the frequency of "a" is 1 and the frequency of "z" is 2, or vice versa. It is impossible to make all present letters have equal frequency.
 

Constraints:

2 <= word.length <= 100
word consists of lowercase English letters only.

'''
from collections import defaultdict, Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        cnt = Counter(word)
        m = defaultdict(list)
        for c in cnt:
            m[cnt[c]].append(c)
        if len(cnt) == 1: return True
        if len(m) == 1 and list(m.keys())[0] == 1:
            return True
        if len(m) == 2:
            val = []
            for c in m:
                val.append((c, len(m[c])))
            val.sort()    
            if val[1][0] - val[0][0] == 1 and (val[1][1] == 1 or val[0][1] == 1):
                return True
        return False
            