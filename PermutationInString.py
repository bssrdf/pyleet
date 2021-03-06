'''
-Medium-

*Sliding Window*



Given two strings s1 and s2, write a function to return true if s2 contains 
the permutation of s1. In other words, one of the first string's permutations 
is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Constraints:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

'''
from collections import defaultdict

class Solution(object):

    def checkInclusionFramework(self, s1, s2):
        '''
        use the sliding window framework
        ''' 
        need   = defaultdict(int)
        window = defaultdict(int)        
        for c in s1: need[c] += 1
        left, right = 0,  0
        valid = 0
        while right < len(s2):
            # c 是将移入窗口的字符
            c = s2[right]
            # 右移窗口
            right += 1
            # 进行窗口内数据的一系列更新
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1 
            # 判断左侧窗口是否要收缩
            while right-left >= len(s1): 
                if valid == len(need):
                   return True
                d = s2[left]
                # 左移窗口
                left += 1 
                # 进行窗口内数据的一系列更新
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1        
        return False

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        start = end = 0
        char_need = defaultdict(int)    # the count of char needed by current window, negative means current window has it but not needs it        
        count_need = len(s1)             # count of chars not in current window but in t               
        
        for i in s1:           
            char_need[i] += 1           # current window needs all char in t
           
        while end < len(s2):
            if char_need[s2[end]] > 0:
                count_need -= 1
            char_need[s2[end]] -= 1 # current window contains s[end] now, 
                                  # so does not need it any more;
                                  # char_need[s[end]] could become negative
            end += 1
            #print(end, s[end-1], count_need, char_need)
            # shrink the window only when all chars in T are still present in
            # the window: dictated by count_need=0
            while count_need == 0:
                if end-start == len(s1):
                    return True                
                char_need[s2[start]] += 1    # current window does not contain s[start] any more
                if char_need[s2[start]] > 0: # when some count in char_need is positive, it means there is char in t but not current window
                    count_need += 1
                start += 1
            #print(start, end, min_start, min_length)
        return False


if __name__ == "__main__":
   print(Solution().checkInclusion("ab", "eidbaooo"))
   print(Solution().checkInclusion("ab", "eidboaoo"))
   print(Solution().checkInclusionFramework("ab", "eidbaooo"))
   print(Solution().checkInclusionFramework("ab", "eidboaoo"))