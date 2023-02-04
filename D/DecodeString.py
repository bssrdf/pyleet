'''
-Medium-

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the 
square brackets is being repeated exactly k times. Note that k is guaranteed 
to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, 
square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any 
digits and that digits are only for those repeat numbers, k. For example, 
there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"

'''

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        def helper(s):
            i, n = 0, len(s)
            num = 0
            res = ''
            while i < n:
                if ord('0') <= ord(s[i]) <= ord('9'):
                    num = 10*num+ord(s[i])-ord('0')                
                elif ord('a') <= ord(s[i]) <= ord('z'):    
                    res += s[i]                         
                elif s[i] == '[':                    
                    j, cnt = i, 0
                    while i < n:
                        if s[i] == '[': cnt += 1
                        if s[i] == ']': cnt -= 1
                        if cnt == 0: break
                        i += 1
                    subs = helper(s[j+1:i])
                    res += subs*num
                    num = 0              
                i += 1                         
            return res
        return helper(s)

if __name__ == "__main__":
    print(Solution().decodeString("3[a]2[bc]"))
    print(Solution().decodeString("3[a2[c]]"))
    print(Solution().decodeString("abc3[cd]xyz"))
    print(Solution().decodeString("2[abc]3[cd]ef"))