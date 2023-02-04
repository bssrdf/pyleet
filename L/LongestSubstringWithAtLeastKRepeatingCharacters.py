'''

-Medium-

*Divide and Conquer*
*Recursion*

Given a string s and an integer k, return the length of the longest substring 
of s such that the frequency of each character in this substring is greater 
than or equal to k.

 

Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times 
and 'b' is repeated 3 times.
 

Constraints:

1 <= s.length <= 10^4
s consists of only lowercase English letters.
1 <= k <= 105

'''
from collections import defaultdict 
    
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        """
        In each step, just find the infrequent elements (show less than k times) 
        as splits since any of these infrequent elements couldn’t be any part of 
        the substring we want.
        """
        if not s: return 0
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
        flag = True
        for i in range(26):
            if count[i] < k and count[i] > 0:
                flag = False
                break
        # return the length of string if this string is a valid string
        if flag: return len(s)
        res = 0
        start, cur = 0, 0
        # otherwise we use all the infrequent elements as splits
        while cur < len(s):
            if count[ord(s[cur]) - ord('a')] < k:
                res = max(res, self.longestSubstring(s[start:cur], k))
                start = cur + 1
            cur += 1
        # last segment
        res = max(res, self.longestSubstring(s[start:],k))
        return res

        '''   
        def longestSubstringHelper(s, k, start, end):
            count = [0] * 26
            for i in range(start, end):
                count[ord(s[i]) - ord('a')] += 1
            max_len = 0
            i = start
            while i < end:
                while i < end and count[ord(s[i]) - ord('a')] < k:
                    i += 1
                j = i
                while j < end and count[ord(s[j]) - ord('a')] >= k:
                    j += 1

                if i == start and j == end:
                    return end - start

                max_len = max(max_len, longestSubstringHelper(s, k, i, j))
                i = j
            return max_len

        return longestSubstringHelper(s, k, 0, len(s))
        '''
        

if __name__ == "__main__":
    print(Solution().longestSubstring("aaabb", 3))
    print(Solution().longestSubstring("aaabbcccc", 3))