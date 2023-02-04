'''
$$$
-Medium-

A string S represents a list of words.

Each letter in the word has 1 or more options.  If there is one option, the 
letter is represented as is.  If there is more than one option, then curly 
braces delimit the options.  For example, "{a,b,c}" represents options 
["a", "b", "c"].

For example, "{a,b,c}d{e,f}" represents the list ["ade", "adf", "bde", 
"bdf", "cde", "cdf"].

Return all words that can be formed in this manner, in lexicographical order.

 

Example 1:

Input: "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]
Example 2:

Input: "abcd"
Output: ["abcd"]
 

Note:

1 <= S.length <= 50
There are no nested curly brackets.
All characters inside a pair of consecutive opening and ending 
curly brackets are different.

'''
class Solution(object):
    def expense(self, s):
        res = []
        def helper(s, path):
            if not s:
                res.append(path)
                return
            n = len(s)
            if s[0] == '{':
                i = 1
                while i < n:                      
                    if s[i] == '}': break
                    i += 1
                for c in sorted(s[1:i].split(',')):
                    helper(s[i+1:], path+c)
            else:
                helper(s[1:], path+s[0])
        helper(s, '')
        return res



if __name__ == "__main__":
    print(Solution().expense("{a,b}c{d,e}f"))
    print(Solution().expense("{a,b,c}d{e,f}"))
    print(Solution().expense("abcd"))