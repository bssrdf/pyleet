'''
-Easy-
In an alien language, surprisingly they also use english lowercase letters, 
but possibly in a different order. The order of the alphabet is some 
permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of 
the alphabet, return true if and only if the given words are sorted 
lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.

'''

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        m = {}
        for i,v in enumerate(order):
            m[v] = i
        for i in range(1,len(words)):
            w1 = words[i-1]
            w2 = words[i]
            j = 0
            for c1, c2 in zip(w1, w2):
               if m[c1] == m[c2]: j += 1
               elif m[c1] < m[c2]: break
               else: return False            
            #print(j, len(w1), len(w2))
            if j == len(w2) and len(w1) > len(w2):                
                return False
        return True

if __name__ == "__main__":
    print(Solution().isAlienSorted(["apple","app"],"abcdefghijklmnopqrstuvwxyz"))
    print(Solution().isAlienSorted(["kuvp","q"],"ngxlkthsjuoqcpavbfdermiywz"))
