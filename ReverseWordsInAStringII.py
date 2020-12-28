'''
-Medium-

*String*

Given an input string , reverse the string word by word. 

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Note: 

A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.

Follow up: Could you do it in-place without allocating extra space?

'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: List[str]
        """
        n = len(s)
        l, r = 0, n-1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        l, r = 0, 0
        for i in range(n):
            if s[i] == ' ':
                r = i-1
                while l < r:
                    s[l], s[r] = s[r], s[l]
                    l += 1
                    r -= 1
                l = i+1
        r = n-1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1        
        return s 

if __name__ == "__main__":
    print(Solution().reverseWords(["t","h","e"," ","s","k","y"," ","i",
                                        "s"," ","b","l","u","e"]))
