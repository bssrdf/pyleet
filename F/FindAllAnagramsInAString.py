'''
-Medium-

*Sliding Window*

Given a string s and a non-empty string p, find all the start indices of p's 
anagrams in s.

Strings consists of lowercase English letters only and the length of both 
strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

'''
from collections import defaultdict

class Solution(object):

    def findAnagramsFramework(self, s, p):
        '''
        :type s: str
        :type p: str
        :rtype: List[int]

        use the sliding window framework
        ''' 
        need   = defaultdict(int)
        window = defaultdict(int)        
        for c in p: need[c] += 1
        left, right = 0,  0
        valid = 0
        res = []
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
            while right-left >= len(p): 
                # 当窗口符合条件时，把起始索引加入 res
                if valid == len(need):
                    res.append(left)                    
                d = s[left]
                # 左移窗口
                left += 1 
                # 进行窗口内数据的一系列更新
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1        
        return res

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        start = end = 0
        char_need = defaultdict(int)    # the count of char needed by current window, negative means current window has it but not needs it        
        count_need = len(p)             # count of chars not in current window but in t               
        res = []
        for i in p:           
            char_need[i] += 1           # current window needs all char in t
           
        while end < len(s):
            if char_need[s[end]] > 0:
                count_need -= 1
            char_need[s[end]] -= 1 # current window contains s[end] now, 
                                  # so does not need it any more;
                                  # char_need[s[end]] could become negative
            end += 1
            #print(end, s[end-1], count_need, char_need)
            # shrink the window only when all chars in T are still present in
            # the window: dictated by count_need=0
            while count_need == 0:
                if end-start == len(p):
                    res.append(start)
                char_need[s[start]] += 1    # current window does not contain s[start] any more
                if char_need[s[start]] > 0: # when some count in char_need is positive, it means there is char in t but not current window
                    count_need += 1
                start += 1
            #print(start, end, min_start, min_length)
        return res

if __name__ == "__main__":
   print(Solution().findAnagrams("cbaebabacd","abc"))
   print(Solution().findAnagrams("abab","ab"))
   print(Solution().findAnagramsFramework("cbaebabacd","abc"))
   print(Solution().findAnagramsFramework("abab","ab"))