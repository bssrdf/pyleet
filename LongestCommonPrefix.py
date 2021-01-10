'''
-Easy-

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.

'''

class Solution(object):

    def longestCommonPrefixMV(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res, c = '', ''
        n = len(strs)
        sz = zip(*strs)
        for c in sz:
            print(c)
        for i in range(200):
            prefix = set()
            for j in range(n):
                if i < len(strs[j]):
                    c = strs[j][i]                   
                    prefix.add(c)
                else:
                    return res
            if len(prefix) > 1:
                return res
            res += c 
        return res


if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))
    print(Solution().longestCommonPrefix(["dog","racecar","car"]))