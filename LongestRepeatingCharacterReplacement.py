'''
-Medium-

*Two Pointers*
*Sliding Window*

Given a string s that consists of only uppercase English letters, you can 
perform at most k operations on that string.

In one operation, you can choose any character of the string and change it 
to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters 
you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 10^4.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
 

Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

'''

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        chars = [0]*26
        n = len(s)
        left, right = 0, 0        
        maxCnt = 0
        res = 0
        while right < n:            
            chars[ord(s[right])-ord('A')] += 1
            maxCnt = max(maxCnt, chars[ord(s[right])-ord('A')])
            # the bigger maxCnt is, the bigger right-left+1 (given k) will be          
            # once we get a window with maxCnt, we don't want it to get smaller 
            # so we don't recompute maxCnt because s[left]'s counts decreased
            while right-left+1 - maxCnt > k:
                chars[ord(s[left])-ord('A')] -= 1                     
                left += 1
            res = max(res, right-left+1)   
            right += 1
        return res

if __name__ == "__main__":
    print(Solution().characterReplacement("AABABBA", 1))