'''
-Medium-

Given a rows x cols screen and a sentence represented by a list of non-empty words, 
find how many times the given sentence can be fitted on the screen.

Note:

A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won't exceed 100.
Length of each word is greater than 0 and won't exceed 10.
1 ≤ rows, cols ≤ 20,000.
Example 1:

Input:
rows = 2, cols = 8, sentence = ["hello", "world"]
Output:
1


Explanation:
hello---
world---


The character '-' signifies an empty space on the screen.


Example 2:

Input:
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]
Output:
2


Explanation:
a-bcd-
e-a---
bcd-e-


The character '-' signifies an empty space on the screen.


Example 3:

Input:
rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]
Output:
1


Explanation:
I-had
apple
pie-I
had--


The character '-' signifies an empty space on the screen.

'''

class Solution(object):
    def wordsTyping(self, rows, cols, sentence):
        all = ""
        for word in sentence: all += word + " "
        res, idx, n, size = 0,  0,  len(sentence),  len(all)
        for i in range(rows):
            colsRemaining = cols
            while colsRemaining > 0:
                if len(sentence[idx]) <= colsRemaining:
                    colsRemaining -= len(sentence[idx])
                    if colsRemaining > 0: colsRemaining -= 1
                    idx += 1
                    # 如果idx此时超过单词个数的范围了，说明一整句可以放下，
                    if idx >= n: 
                        # 那么就有可能出现宽度远大于句子长度的情况，
                        # 所以我们加上之前放好的一句之外，
                        # 还要加上colsRemaining/len的个数，
                        res += 1 + colsRemaining // size
                        # 然后colsRemaining%len是剩余的位置，
                        colsRemaining %= size
                        # 此时idx重置为0
                        idx = 0
                else:
                    break
        return res


if __name__ == "__main__":
    print(Solution().wordsTyping(3, 6, ["a", "bcd", "e"]))