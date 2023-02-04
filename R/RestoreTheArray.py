'''
-Hard-

*DP*

*Reverse DP* (going backwards from the end of the array to the beginning)

A program was supposed to print an array of integers. The program forgot to print 
whitespaces and the array is printed as a string of digits s and all we know is 
that all integers in the array were in the range [1, k] and there are no leading 
zeros in the array.

Given the string s and the integer k, return the number of the possible arrays 
hat can be printed as s using the mentioned program. Since the answer may be 
very large, return it modulo 109 + 7.

 

Example 1:

Input: s = "1000", k = 10000
Output: 1
Explanation: The only possible array is [1000]
Example 2:

Input: s = "1000", k = 10
Output: 0
Explanation: There cannot be an array that was printed this way and has all integer >= 1 and <= 10.
Example 3:

Input: s = "1317", k = 2000
Output: 8
Explanation: Possible arrays are [1317],[131,7],[13,17],[1,317],[13,1,7],[1,31,7],[1,3,17],[1,3,1,7]
Example 4:

Input: s = "2020", k = 30
Output: 1
Explanation: The only possible array is [20,20]. [2020] is invalid because 2020 > 30. [2,020] is ivalid because 020 contains leading zeros.
Example 5:

Input: s = "1234567890", k = 90
Output: 34
 

Constraints:

1 <= s.length <= 10^5
s consists of only digits and does not contain leading zeros.
1 <= k <= 10^9


'''

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n, MOD = len(s), 10**9+7
        dp = [0]*(n+1) # dp[i]: the number of the possible arrays formed by s[i:]
        dp[n] = 1 # base case: there is exactly one way to construct an empty string
        for i in range(n-1, -1, -1):
            if s[i] == '0': continue # no leading zeros
            for j in range(i+1,n+1):
                num = int(s[i:j])
                if 1 <= num <= k:
                    dp[i] = (dp[i] + dp[j]) % MOD
                elif num >= 1:
                    break # once s[i:j] larger thank, no need to proceed with bigger j's
        return dp[0]

        
if __name__ == "__main__":
    print(Solution().numberOfArrays(s = "1234567890", k = 90))
    print(Solution().numberOfArrays(s = "1317", k = 2000))
    print(Solution().numberOfArrays(s = "1000", k = 10000))
    print(Solution().numberOfArrays(s = "2020", k = 30))