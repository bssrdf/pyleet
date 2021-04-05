'''
-Hard-

*Two Pointers*
*Hash Table*

You are given a string s and an array of strings words of the same length. Return all starting 
indices of substring(s) in s that is a concatenation of each word in words exactly once, in 
any order, and without any intervening characters.

You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
 

Constraints:

1 <= s.length <= 10^4
s consists of lower-case English letters.
1 <= words.length <= 5000
1 <= words[i].length <= 30
words[i] consists of lower-case English letters.


'''

from collections import defaultdict

class Solution(object):
    def findSubstringWrong(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        m, n = {}, len(s)
        window = defaultdict(int)
        needed = 0
        width = len(words[0])
        for w in words:
            m[w] = m.setdefault(w, 0) + 1
        needed = len(m)
        left, right, start = 0, 0, 0
        cnt = 0
        res = []
        while right < n:
            w = s[right:right+width]
            right += 1
            if w in m:
                window[w] += 1 
                if window[w] == m[w]:
                   cnt += 1
                right += width-1
            while cnt == needed:
                while start <= right and s[start:start+width] not in m:
                    start += 1
                res.append(start)
                window[s[start:start+width]] -= 1
                if window[s[start:start+width]] == 0:
                    window.pop(s[start:start+width])
                cnt -= 1
                start += width
        return res

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        target = defaultdict(int)
        for word in words:
            target[word] += 1
        one_word = len(words[0])
        words_len = len(words)*one_word
        result = []
        for i in range(0,one_word): #窗口的起始位置
            left = i 
            right = i
            valid = 0
            window = defaultdict(int)
            while(right + one_word <=len(s)):#右边界可以继续移动的条件
                #新加入窗口的单词
                new_word = s[right:right+one_word]
                right += one_word
                if new_word in target:
                    window[new_word]+=1
                    if window[new_word] == target[new_word]:
                        valid += 1
                while(right-left == words_len): #左边界移动的条件
                    #判断一下
                    if(valid == len(target)):
                        result.append(left)
                    #左移
                    tmp_word = s[left:left+one_word]
                    left += one_word
                    if tmp_word in target:
                        if(window[tmp_word] == target[tmp_word]):
                            valid -= 1
                        window[tmp_word] -= 1
        return result



if __name__ == "__main__":
    print(Solution().findSubstring("barfoothefoobarman", ["foo","bar"]))