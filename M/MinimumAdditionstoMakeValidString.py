'''

-Medium-
*Recursion*
*Memoization*
*DP*

Given a string word to which you can insert letters "a", "b" or "c" anywhere and any number of times, return the minimum number of letters that must be inserted so that word becomes valid.

A string is called valid if it can be formed by concatenating the string "abc" several times.

 

Example 1:

Input: word = "b"
Output: 2
Explanation: Insert the letter "a" right before "b", and the letter "c" right next to "a" to obtain the valid string "abc".
Example 2:

Input: word = "aaa"
Output: 6
Explanation: Insert letters "b" and "c" next to each "a" to obtain the valid string "abcabcabc".
Example 3:

Input: word = "abc"
Output: 0
Explanation: word is already valid. No modifications are needed. 
 

Constraints:

1 <= word.length <= 50
word consists of letters "a", "b" and "c" only. 

'''

from functools import lru_cache
class Solution:
    def addMinimum(self, word: str) -> int:
        @lru_cache(None)
        def helper(s):
            if not s: return 0
            if len(s) == 1: return 2
            if len(s) == 2: 
                if s == 'ab' or s == 'bc' or s == 'ac': return 1
                else: return 4 
            if len(s) == 3:
                if s == 'abc': return 0
                return min(helper(s[:2])+helper(s[2:]), 
                           helper(s[:1])+helper(s[1:]))
            return min(helper(s[:3])+helper(s[3:]),
                       helper(s[:2])+helper(s[2:]),
                       helper(s[:1])+helper(s[1:]))
        return helper(word)     
    
    def addMinimum2(self, word: str) -> int:
        k, prev = 0, 'z'
        for c in word:
            k += c <= prev
            prev = c
        return k * 3 - len(word)

                

        

if __name__ == '__main__':
    print(Solution().addMinimum(word = "aaa"))
    print(Solution().addMinimum(word = "abc"))
    print(Solution().addMinimum(word = "b"))
    print(Solution().addMinimum(word = "baacbab"))
