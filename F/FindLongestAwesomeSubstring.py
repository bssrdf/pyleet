'''


-Hard-

*Bit Manipulation*
*Hash Table*

You are given a string s. An awesome substring is a non-empty substring of s such that we can make any number of swaps in order to make it a palindrome.

Return the length of the maximum length awesome substring of s.

 

Example 1:

Input: s = "3242415"
Output: 5
Explanation: "24241" is the longest awesome substring, we can form the palindrome "24142" with some swaps.
Example 2:

Input: s = "12345678"
Output: 1
Example 3:

Input: s = "213123"
Output: 6
Explanation: "213123" is the longest awesome substring, we can form the palindrome "231132" with some swaps.
 

Constraints:

1 <= s.length <= 105
s consists only of digits.


'''



class Solution:
    def longestAwesome(self, s: str) -> int:
        # solution similar to 1371. Find the Longest Substring Containing Vowels in Even Counts
        mask, res = 0, 0
        bitall = (1<<10)-1
        dp = [-1] + [len(s)] * bitall
        # dp[0] = -1
        for i in range(len(s)):
            mask ^= 1 << (ord(s[i]) - ord('0'))
            # print(bin(mask), s[i])
            for j in range(11):
                check_mask = bitall & (mask ^ (1 << j))
                print(f'{mask:010b}', f'{check_mask:010b}', j, s[i])
                res = max(res, i - dp[check_mask])
            dp[mask] = min(dp[mask], i)
        return res


if __name__ == "__main__":
    print(Solution().longestAwesome(s = "3242415"))
  