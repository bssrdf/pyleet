'''

-Easy-

Given two string arrays word1 and word2, return true if the two arrays represent 
the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order 
forms the string.

 

Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
Example 3:

Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true
 

Constraints:

1 <= word1.length, word2.length <= 103
1 <= word1[i].length, word2[i].length <= 103
1 <= sum(word1[i].length), sum(word2[i].length) <= 103
word1[i] and word2[i] consist of lowercase letters.


'''

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        w1, w2, c1, c2 = 0, 0, 0, 0
        m1, m2 = len(word1), len(word2)
        while w1 < m1 and w2 < m2:            #while c1 < len(word1[w1]) and c2 < len(word2[w2]):
            if word1[w1][c1] != word2[w2][c2]:
                    return False
            if c1 == len(word1[w1])-1:
                w1 += 1
                c1 = 0
            else:
                c1 += 1
            if c2 == len(word2[w2])-1:
                w2 += 1
                c2 = 0
            else:
                c2 += 1    
        return w1 == m1 and w2 == m2

if __name__ == "__main__":
    print(Solution().arrayStringsAreEqual(["abc", "d", "defg"], word2 = ["abcddefg"]))
    print(Solution().arrayStringsAreEqual(["a", "cb"], ["ab", "c"]))