'''
-Medium-
*Backtracking*
*Bit Manipulation*

A word's generalized abbreviation can be constructed by taking any number of non-overlapping 
substrings and replacing them with their respective lengths. For example, "abcde" can be 
abbreviated into "a3e" ("bcd" turned into "3"), "1bcd1" ("a" and "e" both turned into "1"), 
and "23" ("ab" turned into "2" and "cde" turned into "3").

Given a string word, return a list of all the possible generalized abbreviations of word. 
Return the answer in any order.

 

Example 1:

Input: word = "word"
Output: ["4","3d","2r1","2rd","1o2","1o1d","1or1","1ord","w3","w2d","w1r1","w1rd","wo2","wo1d","wor1","word"]
Example 2:

Input: word = "a"
Output: ["1","a"]
 

Constraints:

1 <= word.length <= 15
word consists of only lowercase English letters.

'''

class Solution:
    """
    @param word: the given word
    @return: the generalized abbreviations of a word
    """
    def generateAbbreviations(self, word):
        # Write your code here
        ans =  []
        # index为当前位置
        # temp为当前组成的缩略字符串
        # abb为当前缩略长度
        def backtrack(index, path, abb):
            if index == len(word): 
                # 如果存在缩略长度，将其加入temp
                if abb > 0: path += str(abb)
                ans.append(path)
                return 
            # 当前字符
            c = word[index]
            newPath = path
            # 不缩略当前字符
            # 如果存在缩略长度，将其加入temp
            if abb > 0: newPath += str(abb)
            # 将当前字符加入temp
            newPath += c
            # 不缩略当前字符继续递归
            backtrack(index+1, newPath, 0)
            # 缩略当前字符继续递归
            backtrack(index+1, path, abb+1)
           
        backtrack(0, '', 0)
        return ans

    def generateAbbreviationsBit(self, word):
        # Write your code here
        ans =  []
        def abbr(x):
            k, s = 0, ''
            for i in range(len(word)):
                if x & 1 == 0:
                    if k > 0:
                       s += str(k)
                       k = 0
                    s += word[i]
                else:
                    k += 1
                x >>= 1
            if k > 0: s += str(k)
            return s                   

        for i in range(1<<len(word)):
            ans.append(abbr(i))
        return ans



if __name__ == "__main__":
    print(Solution().generateAbbreviations("word"))
    print(Solution().generateAbbreviationsBit("word"))