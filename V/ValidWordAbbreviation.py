'''
-Easy-

Given a non-empty string s and an abbreviation abbr, return whether the string matches 
with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Notice that only the above abbreviations are valid abbreviations of the string "word". 
Any other string is not a valid abbreviation of "word".

Note:
Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

Example 1:

Given s = "internationalization", abbr = "i12iz4n":

Return true.
Example 2:

Given s = "apple", abbr = "a2e":

Return false.
Similar Questions
Minimum Unique Word Abbreviation Hard
Word Abbreviation Hard

'''

class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        if len(abbr) > len(word): return False
        i, j = 0, 0
        while i < len(abbr): 
            if abbr[i].isalpha():
                if abbr[i] == word[j]:
                    i += 1
                    j += 1
                    continue
                return False
            num = 0
            while i < len(abbr) and abbr[i].isdigit():
                num = 10*num + int(abbr[i])
                i += 1
            j += num
            if j > len(word): return False
        return j == len(word)



if __name__=="__main__":
    print(Solution().validWordAbbreviation("internationalization", abbr = "i12iz4n"))
    print(Solution().validWordAbbreviation("apple", abbr = "a2e"))