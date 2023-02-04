'''
Given an array of strings strs, group the anagrams together. You can return the 
answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different 
word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.


'''

from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        memo = defaultdict(list)
        for s in strs:
            memo[tuple(sorted(s))].append(s)        
        return list(memo.values())


if __name__ == "__main__":    
    print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(Solution().groupAnagrams([""]))
    print(Solution().groupAnagrams(["a"]))