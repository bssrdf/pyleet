'''

-Medium-

*DP*
*Stack*


You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

 

Example 1:

Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
Example 2:

Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.
 

Constraints:

1 <= s.length <= 105
s[i] is 'a' or 'b'​​.



'''



class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n+1)
        bcount = 0
        for i in range(1, n+1):
            if s[i-1] == 'a':
                # case 1: keep current a. ==> prev chars must be a...a
                # so need to remove all 'b' chars before i, which is bcount
                
                # case 2: remove current a ==> prev chars must be a...ab...b
                # so need to remove current a and whatever makes substring before 
                # current i valid which is dp[i];
                dp[i] = min(dp[i-1]+1, bcount)
            else:
                # since it is always valid to append 'b' if substring before current i is 
                # valid, so just copy whatever makes substring before i valid which is dp[i];
                dp[i] = dp[i-1]
                bcount += 1
        return dp[n]
    
    def minimumDeletions2(self, s: str) -> int:
        n = len(s)
        dp, dp0 = 0, 0
        bcount = 0
        for i in range(1, n+1):
            if s[i-1] == 'a':
                # case 1: keep current a. ==> prev chars must be a...a
                # so need to remove all 'b' chars before i, which is bcount
                
                # case 2: remove current a ==> prev chars must be a...ab...b
                # so need to remove current a and whatever makes substring before 
                # current i valid which is dp[i];
                dp = min(dp0+1, bcount)
            else:
                # since it is always valid to append 'b' if substring before current i is 
                # valid, so just copy whatever makes substring before i valid which is dp[i];
                dp = dp0
                bcount += 1
            dp, dp0 = dp0, dp            
        return dp0

    def minimumDeletions3(self, s: str) -> int:
        stack = []
        res = 0
        for c in s:
            if stack and c < stack[-1]:
                stack.pop()
                res += 1
            else:
                stack.append(c)
        return res

            


if __name__ == "__main__":
    print(Solution().minimumDeletions(s = "aababbab"))
        
