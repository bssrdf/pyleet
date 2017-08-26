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
        # Use sliding window: maintain two pointers i, j
        for k in range(1, len(S)):
            if S[k] == S[k-1]:
                continue
            if j >= 0 and S[j] != S[k]:
                # max length is always max(k-i)
                maxLen = max(k-i, maxLen)
                i = j+1            
            j = k-1
            print i, j, k, maxLen
        #print j, i, maxLen
        return max(len(S)-i, maxLen)

    def longestsubStringMap(self, S):
        maxLen = 0
        hmap={}        
        i = 0
        for k in range(len(S)):
            if S[k] in hmap:
                hmap[S[k]] += 1
            else:
                hmap[S[k]] = 1
            if len(hmap) > 2:
                maxLen = max(maxLen, k-i)
                while len(hmap) > 2:
                    count = hmap[S[i]]
                    if count > 1:
                        hmap[S[i]] -= 1
                    else:
                        del hmap[S[i]]
                    i += 1
            print i, k, maxLen, len(hmap)
        maxLen = max(maxLen, len(S)-i)
        return maxLen
                    


if __name__ == "__main__":
   # assert Solution().longestsubString("eceba") == 3
    #assert Solution().longestsubString("abaac") == 4
    #assert Solution().longestsubString("abcdaaaaac") == 6
    #assert Solution().longestsubString("cbaaaaaac") == 7
    #assert Solution().longestsubStringMap("cbaaaaaac") == 7
    assert Solution().longestsubStringMap("cbaaaaaa") == 7