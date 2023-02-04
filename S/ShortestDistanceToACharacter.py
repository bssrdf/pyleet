'''
-Easy-

*Two Passes*

Given a string S and a character C, return an array of integers representing 
the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.

'''

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        n = len(S)
        forward, backword = [-1] * n, [-1] * n
        pos = -1
        for i in range(n):
            if S[i] == C:
                pos = i
            if pos != -1:
                forward[i] = i-pos
        pos = -1
        for i in range(n-1, -1, -1):
            if S[i] == C:
                pos = i
            if pos != -1:
                backword[i] = pos-i
        return  [min(i,j) if i >= 0 and j >= 0 else max(i, j) 
                 for i, j in zip(forward, backword)]

if __name__ == "__main__":
    print(Solution().shortestToChar("loveleetcode", 'e'))
