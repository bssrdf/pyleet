'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

'''
import string

class Solution(object):

    def numDecodingsDP(self, s):
        #'''
        n = len(s)
        if not s:
            return 0
        dp = [0]*(n+1)
        dp[0] = 1 # this is a hack, so dp can work
                  # with cases like "26" 
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(2, n+1):
            first = s[i-1:i]
            second = s[i-2:i] 
            if '1' <= first <= '9' and '10' <= second <= '26':
                dp[i] = dp[i-1] + dp[i-2] 
            elif '1' <= first <= '9':
                dp[i] = dp[i-1] 
            elif '10' <= second <= '26':
                dp[i] = dp[i-2]             
            
        #print(dp)
        return dp[n]        






    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = { str(b):a for a,b in zip(string.ascii_uppercase,range(1,27)) }        
        dp = {}
        def dfs(s):           
            if not s:               
                return 1
            else:
                if s in dp:
                    return dp[s]
                res = 0
                for k in range(1, 3):
                    if len(s) < k:
                        break
                    if s[0:k] not in mapping:
                        continue                     
                    res += dfs(s[k:])       
                dp[s] = res   
                return res         
        return dfs(s)
        
import sys
if __name__ == "__main__":
    #print(Solution().numDecodings("9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"))    
    #print(Solution().numDecodingsDP("9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"))    
    #print(Solution().numDecodingsDP("0371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"))    
    #print(Solution().numDecodingsDP("0371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"))    
    print(Solution().numDecodingsDP(sys.argv[1]))

