'''
Given a string s, remove duplicate letters so that every letter appears once and 
only once. You must make sure your result is the smallest in lexicographical order 
among all possible results.

Note: This question is the same as 1081: 
https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.

*Greedy*

'''
from collections import defaultdict
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """        
        
        m = defaultdict(int)
        for c in s:
            m[c] += 1
        visited = [False]*26        
        res = '0'        
        for c in s:
            m[c] -= 1
            if visited[ord(c)-ord('a')]:
                continue
            while c < res[-1] and m[res[-1]] > 0:
                visited[ord(res[-1])-ord('a')] = False 
                res = res[:-1]            
            res += c            
            visited[ord(c)-ord('a')] = True        
        return res[1:]           
                

            


if __name__ == "__main__":   
    print(Solution().removeDuplicateLetters("bcabc"))
    print(Solution().removeDuplicateLetters("cbacdcbc"))