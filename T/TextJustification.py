'''
-Hard-

Given an array of words and a width maxWidth, format the text such that each 
line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words 
as you can in each line. Pad extra spaces ' ' when necessary so that each 
line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the 
number of spaces on a line do not divide evenly between words, the empty slots 
on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is 
inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], 
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", 
because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified becase it contains only one word.

Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to",
"explain","to","a","computer.","Art","is","everything","else","we","do"], 
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
 

Constraints:

1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth


'''

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        i = 0
        while i < len(words):
            j, lth = i, 0
            #首先要做的就是确定每一行能放下的单词数，这个不难，就是比较n个单词的长度和
            # 加上n - 1个空格的长度跟给定的长度L来比较即可，
            while j < len(words) and lth + len(words[j])+ j - i <= maxWidth:
                lth += len(words[j])
                j += 1
            out = ''
            #找到了一行能放下的单词个数，然后计算出这一行存在的空格的个数，
            # 是用给定的长度减去这一行所有单词的长度和
            space = maxWidth - lth
            for k in range(i, j):
                out += words[k]
                #得到了空格的个数之后，就要在每个单词后面插入这些空格，这里有两种情况，
                # 比如某一行有两个单词"to" 和 "a"，给定长度L为6，如果这行不是最后一行，
                # 那么应该输出"to   a"，如果是最后一行，则应该输出 "to a  "，所以这里
                # 需要分情况讨论，最后一行的处理方法和其他行之间略有不同。
                # 最后一个难点就是，如果一行有三个单词，这时候中间有两个空，
                # 如果空格数不是2的倍数，那么左边的空间里要比右边的空间里多加入一个空格，
                # 那么我们只需要用总的空格数除以空间个数，能除尽最好，说明能平均分配，
                # 除不尽的话就多加个空格放在左边的空间里，以此类推
                if space > 0:
                    tmp = 0
                    # if this is the last line
                    if j == len(words):
                        # if the last word, use all remaining spaces                        
                        if j - k == 1: tmp = space
                        # otherwise, just one space
                        else: tmp = 1
                    else: 
                        if j - k - 1 > 0:
                            if space % (j - k - 1) == 0: tmp = space // (j - k - 1)
                            else: tmp = space // (j - k - 1) + 1
                        else: tmp = space
                    out += ' '*tmp
                    space -= tmp
            res.append(out)
            i = j
        return res
        
if __name__ == "__main__":
    print(Solution().fullJustify(["This", "is", "an", "example", "of",
             "text", "justification."], 16))