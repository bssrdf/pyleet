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
        """
        还是子串问题，我们仍用滑动窗口去解决。由于words中单词长度相等，那么设置左右指针移动时只移动一个
        单词的长度。需要注意的是，应当在“窗口滑动”之前遍历窗口的起始位置。比如每个单词的长度为3，如果左
        右指针的起始位置为0，那么每次只移动一个单词长度的话，能访问到的只有以0、3、6、9,...这几个索引字
        母开头的单词。左右指针的起始位置为1时，每次只移动一个单词长度，能访问到的只有以1、4、7、10,...
        这几个索引字母开头的单词。左右指针的起始位置为2时，能访问到的只有2,5,8,11,...这几个索引字母开头
        的单词。因此需要遍历[0,len(one_word))设置左右指针的起始位置，这样能够遍历到以各个位置开头的单词，
        确保没有遗漏。

        我们仍维护target来存储words中出现的各个单词的个数（需要凑齐的单词），window存储窗口中出现的words
        里单词的个数，valid存储window中满足target条件的单词个数。需要注意的是对于不同的窗口起始位置，
        window和valid要重新初始化。因为对于不同的窗口起始位置，window和valid将要存储新一轮的滑动结果。

        右边界移动的条件为：右指针+一个单词的长度<=字符串s的长度(这样当右指针+一个单词长度=字符串s的长度时，
        右指针继续右移一个单词的长度，右指针等于len(s)，就不能继续移动了)。左指针移动的条件为窗口内的字母
        个数等于words中的字母个数，此时判断窗口内子串是否是words中单词的串联，并移动左指针。
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
                    # left pointer moves
                    tmp_word = s[left:left+one_word]
                    left += one_word
                    if tmp_word in target:
                        if(window[tmp_word] == target[tmp_word]):
                            valid -= 1
                        window[tmp_word] -= 1
        return result



if __name__ == "__main__":
    print(Solution().findSubstring("barfoothefoobarman", ["foo","bar"]))