'''

-Medium-

Given a string S, we can transform every letter individually to be lowercase 
or uppercase to create another string.

Return a list of all possible strings we could create. You can return 
the output in any order.

 

Example 1:

Input: S = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: S = "3z4"
Output: ["3z4","3Z4"]
Example 3:

Input: S = "12345"
Output: ["12345"]
Example 4:

Input: S = "0"
Output: ["0"]
 

Constraints:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.

'''

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        def helper(s, cur):
            if not s:
                res.append(cur)
                return            
            i = 0
            while i < len(s) and s[i].isdigit():
                i += 1
            if i < len(s):   
                c = s[i]                        
                if c.islower():
                    a, b = c, c.upper()
                else:
                    a, b = c, c.lower()                
                helper(s[i+1:], cur+s[:i]+a)
                helper(s[i+1:], cur+s[:i]+b)
            else:
                helper(s[i:], cur+s[:i])

        helper(S, '')
        return res


if __name__ == "__main__":
    print(Solution().letterCasePermutation("a1b2"))
    print(Solution().letterCasePermutation("12345"))
    print(Solution().letterCasePermutation("0"))
    print(Solution().letterCasePermutation("3z4"))