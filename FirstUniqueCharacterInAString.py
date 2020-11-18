'''
Given a string, find the first non-repeating character in it and return its index. 
If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
 

Note: You may assume the string contains only lowercase English letters.

'''

import sys

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {}        
        mx = sys.maxsize
        res = mx
        for i,c in enumerate(s):            
            m[c] = mx if c in m else i                            
        for v in m.values():
            res = min(res, v)
        return -1 if res == mx else res
        


if __name__ == "__main__":
    print(Solution().firstUniqChar("leetcode"))
    print(Solution().firstUniqChar("loveleetcode"))