'''
-Hard-

*Greedy*


Given a string s and an integer k, rearrange s such that the same characters 
are at least distance k from each other. If it is not possible to rearrange 
the string, return an empty string "".

 

Example 1:

Input: s = "aabbcc", k = 3
Output: "abcabc"
Explanation: The same letters are at least a distance of 3 from each other.
Example 2:

Input: s = "aaabc", k = 3
Output: ""
Explanation: It is not possible to rearrange the string.
Example 3:

Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least a distance of 2 from each other.
 

Constraints:

1 <= s.length <= 3 * 105
s consists of only lowercase English letters.
0 <= k <= s.length



'''

from collections import Counter
import string
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        n = len(s)
        ans = []
        count = Counter(s)
        valid = Counter()  # valid[i] := the leftmost index i can appear
        # return the letter that has most count and also valid
        def getBestLetter(index: int) -> chr:
            maxCount = -1
            bestLetter = '*'

            for c in string.ascii_lowercase:
                if count[c] > 0 and count[c] > maxCount and index >= valid[c]:
                    bestLetter = c
                    maxCount = count[c]

            return bestLetter
        for i in range(n):
            c = getBestLetter(i)
            if c == '*': return ''
            ans.append(c)
            count[c] -= 1
            valid[c] = i + k
        return ''.join(ans) 


if __name__ == "__main__":
    print(Solution().rearrangeString(s = "aabbcc", k = 3))
    print(Solution().rearrangeString(s = "aaadbbcc", k = 2))