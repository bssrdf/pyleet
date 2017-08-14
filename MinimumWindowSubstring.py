'''
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

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        MAX_INT = 2147483647
        start = end = 0
        char_need = defaultdict(int)    # the count of char needed by current window, negative means current window has it but not needs it
        count_need = len(t)             # count of chars not in current window but in t
        min_length = MAX_INT
        min_start = 0
        print 'length s :', len(s)
        for i in t:
            char_need[i] += 1           # current window needs all char in t
        while end < len(s):
            if char_need[s[end]] > 0:
                count_need -= 1
            char_need[s[end]] -= 1      # current window contains s[end] now, so does not need it any more
            end += 1
            print end, count_need, char_need
            while count_need == 0:
                if min_length > end - start:
                    min_length = end - start
                    min_start = start
                char_need[s[start]] += 1    # current window does not contain s[start] any more
                if char_need[s[start]] > 0: # when some count in char_need is positive, it means there is char in t but not current window
                    count_need += 1
                start += 1
        return "" if min_length == MAX_INT else s[min_start:min_start + min_length]
        


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
   assert Solution().minWindow("ADOBECODEBANC", "ABC") == "BANC"
   print Solution().minWindowAC("ADOBECODEBANC", "ABCC") 