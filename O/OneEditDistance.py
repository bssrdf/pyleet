'''
-Medium-

Given two strings s and t, determine if they are both one edit distance apart.

Note: 

There are 3 possiblities to satisify one edit distance apart:

Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t
Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:

Input: s = "1203", t = "1213"
Output: true
Explanation: We can replace '0' with '1' to get t.

'''

class Solution(object):
    def oneEditDistance(self, s, t):
        if abs(len(s)-len(t)) > 1:
            return False
        if len(s) < len(t): s, t = t, s
        m, n =  len(s), len(t)
        diff = m-n       
        if (diff == 1):
            for i in range(n):
                if (s[i] != t[i]):
                    return s[i+1:] == t[i:]
            return True
        else:
            cnt = 0
            for i in range(m):
                if s[i] != t[i]: cnt += 1
            return cnt == 1
        

if __name__ == "__main__":   
    print(Solution().oneEditDistance("ab",  "acb"))
    print(Solution().oneEditDistance("cab", "ade"))
    print(Solution().oneEditDistance("1203", "1213"))
