'''
-Easy-

Given a string s, the power of the string is the maximum length of a 
non-empty substring that contains only one unique character.

Return the power of the string.

 

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
Example 3:

Input: s = "triplepillooooow"
Output: 5
Example 4:

Input: s = "hooraaaaaaaaaaay"
Output: 11
Example 5:

Input: s = "tourist"
Output: 1

Constraints:

1 <= s.length <= 500
s contains only lowercase English letters.

'''

class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        left, right = 0, 1
        res = 1
        while right < n:
            if s[right] != s[right-1]:                
                res = max(res, right-left)
                left = right
            right += 1
        res = max(res, right-left)
        return res


        
if __name__ == "__main__":
    print(Solution().maxPower("leetcode"))
    print(Solution().maxPower("tourist"))
    print(Solution().maxPower("hooraaaaaaaaaaay"))