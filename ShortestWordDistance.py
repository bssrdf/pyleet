"""
Premium Question
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
        distance=sys.maxint
        idx1=idx2=-1
        for i,w in enumerate(words):
            if w==word1:
                idx1=i
                if idx2 != -1:
                    distance = min(distance, abs(idx1-idx2))
            if w==word2:
                idx2 = i
                if idx1 != -1:
                    distance = min(distance, abs(idx2-idx1))
        return distance

if __name__ == "__main__":
    words = ["practice", "makes", "perfect", "coding", "makes"]
    print Solution().shortestDistance(words, "practice", "coding")

