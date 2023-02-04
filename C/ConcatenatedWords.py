'''
-Hard-

Given an array of strings words (without duplicates), return all the concatenated words in the given 
list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words 
in the given array.

 

Example 1:

Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Example 2:

Input: words = ["cat","dog","catdog"]
Output: ["catdog"]
 

Constraints:

1 <= words.length <= 10^4
0 <= words[i].length <= 1000
words[i] consists of only lowercase English letters.
0 <= sum(words[i].length) <= 6 * 10^5

'''

class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words.sort(key=len)
        wordset = set()
        res = []
        def dfs(s, wset):
            if not wset: return False
            dp = {}
            def helper(s):
                if not s: return True
                if s in dp: return dp[s]
                for i in range(len(s)):
                    if s[0:i+1] in wset:
                        if helper(s[i+1:]):
                            dp[s] = True                       
                            return dp[s]
                dp[s] = False
                return dp[s]
            return helper(s)     
        for word in words: 
            #wordset.remove(word)           
            if dfs(word, wordset): res.append(word)
            wordset.add(word)
        return res

    def findAllConcatenatedWordsInADictTLE(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        d = set(words)
        
        def dfs(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                
                if prefix in d and suffix in d:
                    return True
                if prefix in d and dfs(suffix):
                    return True
                if suffix in d and dfs(prefix):
                    return True
            
            return False
        
        res = []
        for word in words:
            if dfs(word):
                res.append(word)
        
        return res

    def findAllConcatenatedWordsInADictFast(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words_set = set(words)
        self.output = []
        self.memo = {}
        def check(word, words_set):
            if word in self.memo:
                return self.memo[word]
            
            for i in range(1, len(word)):
                x, y = word[:i],  word[i:]
                if x in words_set and y in words_set:
                    self.memo[word] = True
                    return True
                if x in words_set and check(y, words_set):
                    self.memo[word] = True
                    return True
                if y in words_set and check(x, words_set):
                    self.memo[word] = True
                    return True
            self.memo[word] = False
            return False
        
        for word in words:
            if check(word, words_set):
                self.output.append(word)
        return self.output
        




        
if __name__=="__main__":
    print(Solution().findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
    print(Solution().findAllConcatenatedWordsInADictFast(["cats","catsdogcats","cat","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))