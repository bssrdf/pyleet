'''
-Medium-
*DP*

A binary string is monotone increasing if it consists of some number of 0's (possibly none), 
followed by some number of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

Return the minimum number of flips to make s monotone increasing.

 

Example 1:

Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
Example 2:

Input: s = "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.
Example 3:

Input: s = "00011000"
Output: 2
Explanation: We flip to get 00000000.
 

Constraints:

1 <= s.length <= 10^5
s[i] is either '0' or '1'.

'''

class Solution(object):
    def minFlipsMonoIncrWrong(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        one, zero = 0, n-1
        while one < n:
            if s[one] == '1': break
            one += 1
        while zero >= 0:
            if s[zero] == '0': break  
            zero -= 1
        print(one, zero)
        k, l = 0, 0
        i = one+1
        while i < n:
            if s[i] == '0': k += 1
            i += 1
        i = zero-1
        while i >= 0:
            if s[i] == '1': l += 1
            i -= 1
        print(k,l)
        return min(k,l)
    
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        n, res = len(s), 10**6
        cnt1, cnt0 = [0]*(n+1), [0]*(n+1)
        i, j = 1, n-1
        for j in range(n-1, -1, -1):
            cnt1[i] = cnt1[i-1] + (1 if s[i-1] == '1' else 0)
            cnt0[j] = cnt0[j+1] + (1 if s[j] == '0' else 0)
            i += 1
        #print(cnt1, cnt0)
        for i in range(n+1):
            # at any given i, 
            # cnt1[i] is the number of 1's in [0,i-1]
            # cnt0[i] is the number of 0's in [i,n]
            res = min(res, cnt0[i]+cnt1[i])
        return res

    def minFlipsMonoIncrO1Space(self, s):
        """
        :type s: str
        :rtype: int
        """
        n, res, cnt1 = len(s), 0, 0
        for i in range(n):
            if s[i] == '1': cnt1 += 1
            else: res += 1
            res = min(res, cnt1)
        return res



if __name__ == "__main__":
    print(Solution().minFlipsMonoIncr("00110"))
    print(Solution().minFlipsMonoIncr("010110"))
    print(Solution().minFlipsMonoIncr("00011000"))
    print(Solution().minFlipsMonoIncr("000000"))
    print(Solution().minFlipsMonoIncr("10011111110010111011"))
    print(Solution().minFlipsMonoIncrO1Space("00110"))
    print(Solution().minFlipsMonoIncrO1Space("010110"))
    print(Solution().minFlipsMonoIncrO1Space("00011000"))
    print(Solution().minFlipsMonoIncrO1Space("000000"))
    print(Solution().minFlipsMonoIncrO1Space("10011111110010111011"))