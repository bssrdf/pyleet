'''
-Medium-


Given a string s, partition s such that every substring of the partition is a 
palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.

'''

class Solution(object):

    def partitionDP(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """        
        def isPalindrome(s): 
        # Run loop from 0 to len/2 
            return s == s[::-1]
        memo = {}        
        def helper(s):
            if not s:                
                return [[]]
            if s in memo:
                return memo[s]
            res = []
            for i in range(len(s)):
                if isPalindrome(s[:i+1]):
                    cur = [s[:i+1]]                    
                    pars = helper(s[i+1:]) 
                    for p in pars:
                       res.append(cur+p)
            memo[s] = res
            return memo[s]
        return helper(s)    
       

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """        
        def isPalindrome(s): 
        # Run loop from 0 to len/2 
            for i in range(len(s)//2): 
                if s[i] != s[len(s)-i-1]:
                    return False
            return True
        memo = {}
        res = []
        def helper(s,cur):
            if not s:
                res.append(cur[:]) 
                return
            #if s in memo:
            #    return memo[s]
            #res = []
            for i in range(len(s)):
                if isPalindrome(s[:i+1]):
                    cur.append(s[:i+1])
                    helper(s[i+1:], cur) 
                    cur.pop()
        helper(s, [])    
        return res           
                    

if __name__ == "__main__":
    print(Solution().partition("aab"))