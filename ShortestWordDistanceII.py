# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 23:56:39 2017

@author: merli
"""

import sys
from bisect import bisect_left

from collections import defaultdict
class Solution:
    
    def __init__(self, words):
        self.words = words
        self.wordInd = defaultdict(list)
        for i,w in enumerate(self.words):
            self.wordInd[w].append(i)
        print self.wordInd
        
    def shortestDistance(self, word1, word2):
        """
        :type words: list[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        index1 = self.wordInd[word1]
        index2 = self.wordInd[word2]
        i,j,dist=0,0,sys.maxint
        while i < len(index1) and j < len(index2):
            dist = min(dist, abs(index1[i]-index2[j]))
            if index1[i] < index2[j]:
                i += 1
            else:
                j += 1
        return dist
        
        

if __name__ == "__main__":
    words = ["practice", "makes", "perfect", "coding", "makes"]
    print Solution(words).shortestDistance("practice", "coding")
    #Solution(words)