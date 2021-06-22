'''
-Hard-
*DFS*

Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where 
each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
 

Constraints:

1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.


'''

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wd = set(wordDict)
        res = []
        def helper(words, sentence):
            if not words:
                res.append(sentence.lstrip())
                return 
            for i in range(len(words)):
                if words[:i+1] in wd:
                    helper(words[i+1:], sentence+' '+words[:i+1])
        helper(s, '')   
        return res
        
if __name__ == "__main__":
    #print(Solution().wordBreak("leetcode", ["leet", "code"]))
    #print(Solution().wordBreak("applepenapple", ["apple", "pen"]))
    print(Solution().wordBreak(s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]))
    print(Solution().wordBreak(s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]))
    print(Solution().wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]))
    #print(Solution().wordBreak("aaaaaaa",["aaaa","aaa"]))
