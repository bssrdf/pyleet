'''
-Hard
*DP*
A message containing letters from A-Z is being encoded to numbers using the 
following mapping way:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Beyond that, now the encoded string can also contain the character '*', which 
can be treated as one of the numbers from 1 to 9.

Given the encoded message containing digits and the character '*', return the 
total number of ways to decode it.

Also, since the answer may be very large, you should return the output mod 
10^9 + 7.

Example 1:
Input: "*"
Output: 9
Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", 
"E", "F", "G", "H", "I".

Example 2:
Input: "1*"
Output: 9 + 9 = 18

Note:
The length of the input string will fit in range [1, 105].
The input string will only contain the character '*' and digits '0' - '9'.

'''

import string

class Solution(object):
    def numDecodingsDP(self, s):
        n = len(s)
        if not s:
            return 0            
        dp = [0]*(n+1)
        dp[0] = 1 # this is a hack, so dp can work
                  # with cases like "26" 
        if s[0] == '0': return 0
        dp[1] = 9 if s[0] == '*' else 1
        for i in range(2, n+1):
            first = s[i-1:i]
            second = s[i-2:i-1] 
            if first == '*':
                dp[i] += 9*dp[i-1]
            elif first > '0':
                dp[i] += dp[i-1]

            if second == '*':
                if first == '*':
                    dp[i] += 15*dp[i-2]
                elif first <= '6':
                    dp[i] += 2*dp[i-2]
                else:
                    dp[i] += dp[i-2]
            elif second == '1' or second == '2':
                if first == '*':
                    if second == '1':
                        dp[i] += 9*dp[i-2]
                    else:
                        dp[i] += 6*dp[i-2]
                elif second+first <= "26":
                    dp[i] += dp[i-2] 
            dp[i] %= 10**9+7       
        return dp[n]        

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        Let's keep track of:

        e0 = current number of ways we could decode, ending on any number;
        e1 = current number of ways we could decode, ending on an open 1;
        e2 = current number of ways we could decode, ending on an open 2;
        (Here, an "open 1" means a 1 that may later be used as the first digit 
        of a 2 digit number, because it has not been used in a previous 2 digit 
        number.)

        With the right idea of what to keep track of, our dp proceeds 
        straightforwardly.

        Say we see some character c. We want to calculate f0, f1, f2, the 
        corresponding versions of e0, e1, e2 after parsing character c.

        If c == '*', then the number of ways to finish in total is: we could put
         * as a single digit number (9*e0), or we could pair * as a 2 digit 
         number 1* in 9*e1 ways, or we could pair * as a 2 digit number 2* in 6*e2 ways. 
         The number of ways to finish with an open 1 (or 2) is just e0.

        If c != '*', then the number of ways to finish in total is: we could put 
        c as a single digit if it is not zero ((c>'0')*e0), or we could pair c 
        with our open 1, or we could pair c with our open 2 if it is 6 or 
        less ((c<='6')*e2). The number of ways to finish with an open 1 (or 2) 
        is e0 iff c == '1' (or c == '2').

        '''
        MOD = 10**9 + 7
        e0, e1, e2 = 1, 0, 0
        for c in s:
            if c == '*':
                f0 = 9*e0 + 9*e1 + 6*e2
                f1 = e0
                f2 = e0
            else:
                f0 = (c > '0') * e0 + e1 + (c <= '6') * e2
                f1 = (c == '1') * e0
                f2 = (c == '2') * e0
            e0, e1, e2 = f0 % MOD, f1, f2
        return e0
        
import sys
if __name__ == "__main__":
    print(Solution().numDecodingsDP("3*"))