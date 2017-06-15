# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 23:56:39 2017

@author: merli
"""

import sys
from bisect import bisect_left

class Solution:
    
    def __init__(self, words):
        self.words = words
        
    def shortestDistance(self, word1, word2):
        """
        :type words: list[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        

if __name__ == "__main__":
    words = ["practice", "makes", "perfect", "coding", "makes"]
    print Solution().shortestDistance(words, "practice", "coding")