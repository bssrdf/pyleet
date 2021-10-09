'''
-Medium-
*Sliding Window*

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all 
these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the 
characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", 
"bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1
 

Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.

'''

from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left, right = 0, 0
        m = {c:0 for c in 'abc'}
        ans = 0
        while right < len(s):
            c = s[right]
            right += 1
            m[c] += 1
            while all(m.values()):
                m[s[left]] -= 1
                left += 1
            ans += left # for every valid window [left-1, right] extend it 
                        # backwards till 0th index; all subs starting from 
                        # s[0], s[1], ... s[left-1] to s[right-1] are valid
            print(left, right, ans)
        return ans
        
if __name__ == "__main__":
    print(Solution().numberOfSubstrings("abcabc"))