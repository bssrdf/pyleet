'''
-Medium-


Given a list of words and two words  word1  and  word2 , return the shortest distance 
between these two words in the list.

word1  and  word2  may be the same and they represent two individual words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: _word1_ = “makes”, _word2_ = “coding”
Output: 1



Input: _word1_ = "makes", _word2_ = "makes"
Output: 3
Note:
You may assume  word1  and  word2  are both in the list.


'''
class Solution:
    def shortestDistanceEqual(self, words, word1, word2):
        """
        :type words: list[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        distance = len(words)
        idx = -1
        for i,w in enumerate(words):
            if w == word1 or w == word2:
                if idx != -1 and (word1 == word2 or w != words[idx]):
                    distance = min(distance, i-idx)
                idx = i    
        return distance

if __name__ == "__main__":
    words = ["practice", "makes", "perfect", "coding", "makes", "study", "makes"]
    #print Solution().shortestDistance(words, "practice", "coding")
    #print Solution().shortestDistance(words, "makes", "coding")
    print(Solution().shortestDistanceEqual(words, "makes", "makes"))