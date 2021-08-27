'''
-Medium-

Given an array of strings strs, return the length of the longest uncommon 
subsequence between them. If the longest uncommon subsequence does not exist, 
return -1.

An uncommon subsequence between an array of strings is a string that is a 
subsequence of one string but not the others.

A subsequence of a string s is a string that can be obtained after 
deleting any number of characters from s.

For example, "abc" is a subsequence of "aebdc" because you can delete the 
underlined characters in "aebdc" to get "abc". Other subsequences of 
"aebdc" include "aebdc", "aeb", and "" (empty string).
 

Example 1:

Input: strs = ["aba","cdc","eae"]
Output: 3
Example 2:

Input: strs = ["aaa","aaa","aa"]
Output: -1
 

Constraints:

1 <= strs.length <= 50
1 <= strs[i].length <= 10
strs[i] consists of lowercase English letters.

'''

class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def subseq(w1, w2):
            #True iff word1 is a subsequence of word2.
            i = 0
            for c in w2:
                if i < len(w1) and w1[i] == c:
                    i += 1
            return i == len(w1)
            
        strs.sort(key = len, reverse = True)
        duplicates = set()
        S = set()
        for s in strs:
            if s in S: duplicates.add(s)
            S.add(s) 

        for i, word1 in enumerate(strs):
            if word1 not in duplicates:
                if i == 0: return len(word1)
                for j, word2 in enumerate(strs[:i]):
                    if subseq(word1, word2): break 
                    if j == i-1: 
                        return len(word1)
        return -1

if __name__ == "__main__":
    print(Solution().findLUSlength(["aba","cdc","eae"]))
    print(Solution().findLUSlength(["aaa", "aaa", "aa"]))
    print(Solution().findLUSlength(["aabbcc", "aabbcc","bc","bcc","aabbccc"]))
