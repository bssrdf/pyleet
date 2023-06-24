'''

-Medium-
*Sliding Window*

You are given a string s consisting only of lowercase English letters. We call a substring special if it contains no character which has occurred at least twice (in other words, it does not contain a repeating character). Your task is to count the number of special substrings. For example, in the string "pop", the substring "po" is a special substring, however, "pop" is not special (since 'p' has occurred twice).

Return the number of special substrings.

A substring is a contiguous sequence of characters within a string. For example, "abc" is a substring of "abcd", but "acd" is not.

 

Example 1:

Input: s = "abcd"
Output: 10
Explanation: Since each character occurs once, every substring is a special substring. We have 4 substrings of length one, 3 of length two, 2 of length three, and 1 substring of length four. So overall there are 4 + 3 + 2 + 1 = 10 special substrings.
Example 2:

Input: s = "ooo"
Output: 3
Explanation: Any substring with a length of at least two contains a repeating character. So we have to count the number of substrings of length one, which is 3.
Example 3:

Input: s = "abab"
Output: 7
Explanation: Special substrings are as follows (sorted by their start positions):
Special substrings of length 1: "a", "b", "a", "b"
Special substrings of length 2: "ab", "ba", "ab"
And it can be shown that there are no special substrings with a length of at least three. So the answer would be 4 + 3 = 7.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters


'''

from collections import defaultdict, Counter

class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        cnt = [-1]*26
        n = len(s)
        ans = 0
        lastP = -1
        for i in range(n):
            idx = ord(s[i])-ord('a')
            if cnt[idx] != -1:
                lastP = max(lastP, cnt[idx])             
            ans += i-lastP
            # print(ans, i, s[i], lastP, cnt)
            cnt[idx] = i
        return ans
    
    def numberOfSpecialSubstrings2(self, s: str) -> int:
        cnt = Counter()
        ans = j = 0
        for i, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 1:
                cnt[s[j]] -= 1
                j += 1
            ans += i - j + 1
            # print(ans, i, c, j, cnt)
        return ans


from random import randint
import time
if __name__ == "__main__":
    # print(Solution().numberOfSpecialSubstrings(s = "abcd"))
    # print(Solution().numberOfSpecialSubstrings(s = "ooo"))
    # print(Solution().numberOfSpecialSubstrings(s = "abab"))
    print(Solution().numberOfSpecialSubstrings(s = 'bnwqahemqdzzsyzydke'))
    print(Solution().numberOfSpecialSubstrings2(s = 'bnwqahemqdzzsyzydke'))
    t1, t2 = 0.0, 0.0
    for k in range(1000):
        N = 10000
        s = ''
        for i in range(N):
            c = ord('a')+randint(0,25)
            s += chr(c)
        start = time.time()
        s1 = Solution().numberOfSpecialSubstrings(s = s) 
        end = time.time()
        t1 += (end-start)
        start = time.time()
        s2 = Solution().numberOfSpecialSubstrings2(s = s)
        end = time.time()
        t2 += (end-start)
        if s1 != s2:
            print(s) 
    print('time spent: {}, {}'.format(t1, t2))    