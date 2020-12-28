"""
Premium Question
Given a list of words and two words word1 and word2, return the shortest distance 
between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in 
the list.


"""
import sys
from bisect import bisect_left

class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: list[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        distance=len(words)
        idx1=idx2=-1
        for i,w in enumerate(words):
            if w==word1:
                idx1=i
            if w==word2:
                idx2 = i                
            if idx2 != -1 and idx1 != -1:
                distance = min(distance, abs(idx1-idx2))
        return distance
        
    def shortestDistanceEqual(self, words, word1, word2):
        """
        :type words: list[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        distance=len(words)
        idx1=idx2=-1
        for i,w in enumerate(words):
            if word1 == word2:
                if word1 == w:
                    if idx1 > idx2:
                        idx2 = i
                    else:
                        idx1 = i
                #print i, idx1, idx2
            else:                    
                if w==word1:
                    idx1 = i
                if w==word2:
                    idx2 = i                
            if idx2 != -1 and idx1 != -1:
                distance = min(distance, abs(idx1-idx2))
        return distance

if __name__ == "__main__":
    words = ["practice", "makes", "perfect", "coding", "makes", "study", "makes"]
    #print Solution().shortestDistance(words, "practice", "coding")
    #print Solution().shortestDistance(words, "makes", "coding")
    print(Solution().shortestDistanceEqual(words, "makes", "makes"))