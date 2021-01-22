'''
-Medium-
*Greedy*

Two strings are considered close if you can attain one from the other using the 
following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another 
existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and 
false otherwise.

 

Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any 
number of operations.
Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
Example 4:

Input: word1 = "cabbba", word2 = "aabbss"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any 
amount of operations.
 

Constraints:

1 <= word1.length, word2.length <= 10^5
word1 and word2 contain only lowercase English letters.

'''

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        """
        1. Frequency of Char need's to be same there both of string as we can do 
        Transform every occurrence of one existing character into another existing 
        character
        2. All the unique char which there in String1 need's to there as well 
        In string2
        """
        w1, w2 = set(), set()
        c1, c2 = {}, {}
        for w in word1:
            w1.add(w)
            c1[w] = c1.get(w,0) + 1
        for w in word2:
            w2.add(w)
            c2[w] = c2.get(w,0) + 1
        return w1 == w2 and sorted(c1.values()) == sorted(c2.values())

if __name__ == "__main__":
    print(Solution().closeStrings("cabbba",  "abbccc"))
    print(Solution().closeStrings("cabbba",  "aabbss"))