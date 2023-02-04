'''
-Medium-
*Two Pointers*

Given a string S, find the length of the longest substring T that contains 
at most k distinct characters.

样例
Example 1:

Input: S = "eceba" and k = 3
Output: 4
Explanation: T = "eceb"
Example 2:

Input: S = "WORLD" and k = 4
Output: 4
Explanation: T = "WORL" or "ORLD"

'''

from collections import defaultdict
class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
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
            while len(window) > k: 
                d = s[left]
                left += 1
                # 进行窗口内数据的一系列更新
                window[d] -= 1
                if window[d] == 0:
                    del window[d]
            # 在这里更新答案
            res = max(res, right-left)
        return res
