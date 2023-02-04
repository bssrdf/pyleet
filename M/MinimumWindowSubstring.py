'''
-Hard-

*Sliding Window*
*Two Pointers*

Given a string S and a string T, find the minimum window in S which will
 contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
'''

from collections import defaultdict
import collections
import sys

class Solution(object):

    def minWindowFrameWork(self, s, t):
        '''
        use the sliding window framework
        ''' 
        need   = defaultdict(int)
        window = defaultdict(int)        
        for c in t: need[c] += 1

        left, right = 0,  0
        valid = 0
        # 记录最小覆盖子串的起始索引及长度
        start, lth =  0, sys.maxsize
        while right < len(s):
            # c 是将移入窗口的字符
            c = s[right]
            # 右移窗口
            right += 1
            # 进行窗口内数据的一系列更新
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1 
            # 判断左侧窗口是否要收缩
            while valid == len(need):
                # 在这里更新最小覆盖子串
                if right - left < lth:
                    start = left
                    lth = right - left
                # d 是将移出窗口的字符
                d = s[left]
                # 左移窗口
                left += 1 
                # 进行窗口内数据的一系列更新
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        #返回最小覆盖子串
        return "" if lth == sys.maxsize \
              else s[start:start+lth]

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """        
        start = end = 0
        char_need = defaultdict(int)    # the count of char needed by current window, negative means current window has it but not needs it
        #char_need = {}
        count_need = len(t)             # count of chars not in current window but in t
        min_length = len(s)+1
        min_start = 0
        #print('length s :', len(s))
        for i in t:           
            char_need[i] += 1      # current window needs all char in t
        while end < len(s):
            if char_need[s[end]] > 0:
                count_need -= 1
            char_need[s[end]] -= 1 # current window contains s[end] now, 
                                  # so does not need it any more;
                                  # char_need[s[end]] could become negative
            end += 1
            print(end, s[end-1], count_need, char_need)
            # shrink the window only when all chars in T are still present in
            # the window: dictated by count_need=0
            while count_need == 0:
                if min_length > end - start:
                    min_length = end - start
                    min_start = start
                #if s[start] in char_need:
                char_need[s[start]] += 1    # current window does not contain s[start] any more
                if char_need[s[start]] > 0: # when some count in char_need is positive, it means there is char in t but not current window
                    count_need += 1
                start += 1
            print(start, end, min_start, min_length)
        return "" if min_length == len(s)+1 else s[min_start:min_start + min_length]
        


    def minWindowAC(self, s, t):
        """
        The current window is s[i:j] and the result window is s[I:J]. In 
        need[c] I store how many times I need character c (can be negative) 
        and missing tells how many characters are still missing. In the loop, 
        first add the new character to the window. Then, if nothing is missing, 
        remove as much as possible from the window start and then update the 
        result.
        """
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]
                

if __name__ == "__main__":
   #assert Solution().minWindow("ADOBECODEBANC", "ABC") == "BANC"
   assert Solution().minWindowFrameWork("ADOBECODEBANC", "ABC") == "BANC"
   #print(Solution().minWindowAC("ADOBECODEBANC", "ABCC"))