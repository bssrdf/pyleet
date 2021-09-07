'''
-Easy-

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the 
length of last word in the string.

If the last word does not exist, return 0.

A word is defined as a character sequence consists of non-space characters only.

样例
Example 1:

Input: "Hello World"
Output: 5
Example 2:

Input: "Hello LintCode"
Output: 8

'''

class Solution:
    """
    @param s: A string
    @return: the length of last word
    """
    def lengthOfLastWord(self, s):
        # write your code here
        #return len(s.split()[-1]) if s else 0
        #res = 0
        count = 0
        for i in s[::-1]:
            if i == ' ' and count != 0:
                return count
            elif i != ' ':
                count += 1
        return count