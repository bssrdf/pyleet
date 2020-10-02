'''

Given a non-empty string s and a dictionary wordDict containing 
a list of non-empty words, determine if s can be segmented into a 
space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the 
segmentation.

You may assume the dictionary does not contain duplicate words.

Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as 
"leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented 
as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false


'''



class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wd = set(wordDict)
        dp = {}
        def helper(words):
            if not words:
                return True
            if words in dp:
                return dp[words]
            for i in range(len(words)):
                if words[0:i+1] in wd:
                    if helper(words[i+1:]):
                        dp[words] = True                       
                        return dp[words]
            dp[words] = False
            return dp[words]
        return helper(s)       


if __name__ == "__main__":
    #print(Solution().wordBreak("leetcode", ["leet", "code"]))
    #print(Solution().wordBreak("applepenapple", ["apple", "pen"]))
    #print(Solution().wordBreak("catsandog", ["cats", "dog", 
    #                           "sand", "and", "cat"]))
    print(Solution().wordBreak("aaaaaaa",["aaaa","aaa"]))
