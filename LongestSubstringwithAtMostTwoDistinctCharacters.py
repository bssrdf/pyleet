# -*- coding: utf-8 -*-
"""
Created on Sun Aug 06 14:27:12 2017

Given a string S, find the length of the longest substring T that contains 
at most two distinct characters.

For example, Given S = “eceba”, T is "ece" which its length is 3.



@author: merli
"""
from collections import defaultdict

class Solution(object):

    def lengthOfLongestSubstringTwoDistinct(self, s):
        n = len(s)
        window = defaultdict(int)
        left, right = 0, 0
        res = 0 # 记录结果
        while right < n:
            c = s[right]
            right += 1
            # 进行窗口内数据的一系列更新
            window[c] += 1
            # 判断左侧窗口是否要收缩
            while len(window) > 2: 
                d = s[left]
                left += 1
                # 进行窗口内数据的一系列更新
                window[d] -= 1
                if window[d] == 0:
                    del window[d]
            # 在这里更新答案
            res = max(res, right-left)
        return res

if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstringTwoDistinct("eceba") == 3
    assert Solution().lengthOfLongestSubstringTwoDistinct("abaac") == 4
    assert Solution().lengthOfLongestSubstringTwoDistinct("abcdaaaaac") == 6
    assert Solution().lengthOfLongestSubstringTwoDistinct("cbaaaaaac") == 7
   
   
        
