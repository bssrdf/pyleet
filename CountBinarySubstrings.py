'''
-Easy-

Give a string s, count the number of non-empty (contiguous) substrings that have the same number 
of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: 
"0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of 
consecutive 1's and 0's.
Note:

s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.


'''

class Solution(object):
    def countBinarySubstringsTLE(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s) // 2
        res = 0
        for i in range(1, n+1):
            t = {'0'*i+'1'*i, '1'*i+'0'*i}
            l = 2 * i
            for j in range(0,len(s)-l+1):
                if s[j:j+l] in t: res += 1
           # print(t, res)
        return res

    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # consider consecutive groups of '1's and '0's
        # the number of valid substrings formed from the 2 groups is min(len(1's), len(0's))
        pre, cur, res = 0, 1, 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]: cur += 1 
            else:
                res += min(pre, cur)
                pre = cur
                cur = 1
        return res + min(pre, cur)


if __name__ == "__main__":
    print(Solution().countBinarySubstrings("00110011"))
    print(Solution().countBinarySubstrings("10101"))