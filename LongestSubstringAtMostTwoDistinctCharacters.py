# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 20:09:53 2017

Given a string S, find the length of the longest substring T that contains at
most two distinct characters.

For example, Given S = “eceba”, T is "ece" which its length is 3.

@author: merli
"""

class Solution(object):
    def longestsubString(self, S):
        i, j, maxLen=0, -1, 0
        for k in range(1, len(S)):
            if S[k] == S[k-1]:
                continue
            if j >= 0 and S[j] != S[k]:
                maxLen = max(k-i, maxLen)
                i = j+1
            print i, j, k, maxLen
            j = k-1
            
        #print j, i, maxLen
        return max(len(S)-i, maxLen)



if __name__ == "__main__":
   # assert Solution().longestsubString("eceba") == 3
    assert Solution().longestsubString("abaac") == 4