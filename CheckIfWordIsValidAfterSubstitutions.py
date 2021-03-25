'''
-Medium-

Given a string s, determine if it is valid.

A string s is valid if, starting with an empty string t = "", you can transform t into s after 
performing the following operation any number of times:

Insert string "abc" into any position in t. More formally, t becomes tleft + "abc" + tright, 
where t == tleft + tright. Note that tleft and tright may be empty.
Return true if s is a valid string, otherwise, return false.

 

Example 1:

Input: s = "aabcbc"
Output: true
Explanation:
"" -> "abc" -> "aabcbc"
Thus, "aabcbc" is valid.
Example 2:

Input: s = "abcabcababcc"
Output: true
Explanation:
"" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"
Thus, "abcabcababcc" is valid.
Example 3:

Input: s = "abccba"
Output: false
Explanation: It is impossible to get "abccba" using the operation.
Example 4:

Input: s = "cababc"
Output: false
Explanation: It is impossible to get "cababc" using the operation.
 

Constraints:

1 <= s.length <= 2 * 10^4
s consists of letters 'a', 'b', and 'c'


'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        S = list(s)    
        r = 'abc'
            
        while S:
            i = 0
            for j in range(len(S)):
                S[i] = S[j]
                i += 1
                if i > 2 and S[i-3] == r[0] and S[i-2] == r[1] and S[i-1] == r[2]:
                    i -= 3
            if i == len(S): return False
            S = S[:i]
        return True

if __name__ == "__main__":
    print(Solution().isValid("aabcbc"))