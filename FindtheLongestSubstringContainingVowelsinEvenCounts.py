'''
-Medium-

Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

 

Example 1:

Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
Example 2:

Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.
Example 3:

Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.
 

Constraints:

1 <= s.length <= 5 x 10^5
s contains only lowercase English letters.



'''


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # solution similar to 1542. Find Longest Awesome Substring
        mask, res = 0, 0
        vowels = {c:i for i,c in enumerate('aeiou')}
        bitall = (1<<len(vowels))-1
        dp = [-1] + [len(s)] * bitall
        # dp[0] = -1
        for i in range(len(s)):
            if s[i] in vowels:
                mask ^= 1 << vowels[s[i]]
            # print(f'{mask:05b}')    
            res = max(res, i - dp[mask])
            print(res, f'{mask:05b}', i, s[i])
            dp[mask] = min(dp[mask], i)
        return res

if __name__ == "__main__":
    print(Solution().findTheLongestSubstring(s = "eleetminicoworoep"))    
    print(Solution().findTheLongestSubstring(s = "leetcodeisgreat"))    
    print(Solution().findTheLongestSubstring(s = "bcbcbc"))    