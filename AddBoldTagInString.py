'''
$$$
-Medium-
*String*

Given a string s and a list of strings dict, you need to add a closed pair of 
bold tag and to wrap the substrings in s that exist in dict. If two such 
substrings overlap, you need to wrap them together by only one pair of closed 
bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need 
to combine them.

Example 1:

Input: 
s = "abcxyz123"
dict = ["abc","123"]
Output:
"abcxyz123"
 

Example 2:

Input: 
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"aaabbcc"
 

Constraints:

The given dict won't contain duplicates, and its length won't exceed 100.
All the strings in input have length in range [1, 1000].

'''

class Solution:

    def addBoldTag(self, s, dic):
        n = len(s)
        res = ''
        bold = set()
        '''
        the idea is a brute force string matching 
        '''
        for word in dic:
            wl = len(word)
            for i in range(n-wl+1):
                if s[i] == word[0] and s[i:i+wl] == word:
                    for j in range(i, i+wl): bold.add(j)        
        for i in range(n):
            if i in bold and i-1 not in bold: res += '<b>'
            res += s[i]
            if i in bold and i+1 not in bold: res += '</b>'
        return res



if __name__ == "__main__": 
    print(Solution().addBoldTag("abcxyz123", ["abc","123"]))
    print(Solution().addBoldTag("aaabbcc", ["aaa","aab","bc"]))