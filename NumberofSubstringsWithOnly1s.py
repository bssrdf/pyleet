'''

-Medium-

Given a binary string s, return the number of substrings with all characters 1's. 
Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: s = "0110111"
Output: 9
Explanation: There are 9 substring in total with only 1's characters.
"1" -> 5 times.
"11" -> 3 times.
"111" -> 1 time.
Example 2:

Input: s = "101"
Output: 2
Explanation: Substring "1" is shown 2 times in s.
Example 3:

Input: s = "111111"
Output: 21
Explanation: Each substring contains only 1's characters.
Example 4:

Input: s = "000"
Output: 0
 

Constraints:

1 <= s.length <= 10^5
s[i] is either '0' or '1'.


'''

class Solution:
    def numSub(self, s: str) -> int:
        n, MOD = len(s), 10**9+7
        i, res = 0, 0 
        while i < n:
            while i < n and s[i] == '0':
                i += 1
            j = i
            while j < n and s[j] == '1':
                j += 1
            k = j - i
            if k > 0:
                res =(res + k*(k+1)//2) % MOD
            i = j
        return res
        

if __name__ == "__main__":
    print(Solution().numSub("0110111"))
    print(Solution().numSub("101"))
    print(Solution().numSub("000"))
    print(Solution().numSub("111111"))