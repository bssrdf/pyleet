'''
-Hard-
*DP*

We can scramble a string s to get a string t using the following algorithm:

If the length of the string is 1, stop.
If the length of the string is > 1, do the following:
Split the string into two non-empty substrings at a random index, i.e., if 
the string is s, divide it to x and y where s = x + y.
Randomly decide to swap the two substrings or to keep them in the same order. 
i.e., after this step, s may become s = x + y or s = y + x.
Apply step 1 recursively on each of the two substrings x and y.
Given two strings s1 and s2 of the same length, return true if s2 is a 
scrambled string of s1, otherwise, return false.

 

Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true
Explanation: One possible scenario applied on s1 is:
"great" --> "gr/eat" // divide at random index.
"gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and keep them in order.
"gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both substrings. divide at ranom index each of them.
"g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring and to keep the second substring in the same order.
"r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide "at" to "a/t".
"r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings in the same order.
The algorithm stops now and the result string is "rgeat" which is s2.
As there is one possible scenario that led s1 to be scrambled to s2, we return true.
Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false
Example 3:

Input: s1 = "a", s2 = "a"
Output: true
 

Constraints:

s1.length == s2.length
1 <= s1.length <= 30
s1 and s2 consist of lower-case English letters.

'''
from functools import lru_cache
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2: return True
        if len(s1) != len(s2): return False
        n = len(s1)
        @lru_cache(None)
        def helper(idx1, idx2, l):
            '''
            简单的说，就是 s1 和 s2 是 scramble 的话，那么必然存在一个在 s1 上的
            长度 l1，将 s1 分成 s11 和 s12 两段，同样有 s21 和 s22，那么要么 s11 
            和 s21 是 scramble 的并且 s12 和 s22 是 scramble 的；要么 s11 和 s22 
            是 scramble 的并且 s12 和 s21 是 scramble 的。
            '''
            if l == 0: return True
            if l == 1: return s1[idx1] == s2[idx2] # base case
            for k in range(1, l): # split at k: 
                    # s1[idx1:idx1+k] and s2[idx2:idx2+k] are scramble
                    # and 
                    # s1[idx1+k:idx1+l] and s2[idx2+k:idx2+l] are scramble              
                if ((helper(idx1, idx2, k) and helper(idx1 + k, idx2 + k, l - k)) or
                    # s1[idx1:idx1+k] and s2[idx2+l-k:idx2+l] are scramble
                    # and 
                    # s1[idx1+k:idx1+l] and s2[idx2+k:idx2+l] are scramble              
                    (helper(idx1, idx2 + l - k, k) and helper(idx1 + k, idx2, l - k))): 
                    #print(idx1, idx2, k, l)
                    return True
            return False
        return helper(0,0,n)


if __name__ == "__main__":
    #print(Solution().isScramble("abcde", "caebd"))
    print(Solution().isScramble("great", "rgeat"))