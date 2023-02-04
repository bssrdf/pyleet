'''
-Hard-

*DP*

An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
Any student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it modulo 109 + 7.

 

Example 1:

Input: n = 2
Output: 8
Explanation: There are 8 records with length 2 that are eligible for an award:
"PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).
Example 2:

Input: n = 1
Output: 3
Example 3:

Input: n = 10101
Output: 183236316
 

Constraints:

1 <= n <= 105


'''



class Solution:
    def checkRecord(self, n: int) -> int:
        # wrong
        mod = 10**9 + 7
        hasA, lastL, lastLL = 1, 1, 0
        dp1 = 3
        for i in range(2, n+1):
            dp = 3 * dp1 - hasA - lastLL
            hasA = 2 * (dp1 - hasA)
            lastLL = lastL
            lastL = dp1 - lastL
            dp, dp1 = dp1, dp
        return dp1 % mod
    
    def checkRecord2(self, n: int) -> int:
        mod = 10**9 + 7
        PorL = [0]*(n + 1) #  ending with P or L, no A
        P =  [0]*(n + 1)  #  ending with P, no A
        PorL[0] = P[0] = 1
        PorL[1] = 2; P[1] = 1

        for i in range(2, n+1):
            P[i] = PorL[i - 1] # append P at i to the end of either P or L at i-1
            # ending with P or L at i includes 3 cases:
            # 1) ends with P at i: P[i]
            # 2) ends with L at i and P at i-1: P[i-1]
            # 3) ends with L at i and L at i-1 and P at i-2: P[i-2]
            PorL[i] = (P[i] + P[i - 1] + P[i - 2]) % mod
    
        res = PorL[n] # count without A
        for i in range(n): # inserting A into (n-1)-length strings
            s = (PorL[i] * PorL[n - i - 1]) % mod
            res = (res + s) % mod    
        return res
if __name__ == "__main__":
    print(Solution().checkRecord(n = 2))
    print(Solution().checkRecord(n = 3))
    print(Solution().checkRecord(n = 10101))
    print(Solution().checkRecord2(n = 10101))
