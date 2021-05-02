'''
-Hard-

*Trie*

Design a special dictionary which has some words and allows you to search the words in it by a 
prefix and a suffix.

Implement the WordFilter class:

WordFilter(string[] words) Initializes the object with the words in the dictionary.
f(string prefix, string suffix) Returns the index of the word in the dictionary which has the 
prefix prefix and the suffix suffix. If there is more than one valid index, return the largest 
of them. If there is no such word in the dictionary, return -1.
 

Example 1:

Input
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
Output
[null, 0]

Explanation
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".
 

Constraints:

1 <= words.length <= 15000
1 <= words[i].length <= 10
1 <= prefix.length, suffix.length <= 10
words[i], prefix and suffix consist of lower-case English letters only.
At most 15000 calls will be made to the function f.

'''
from collections import defaultdict

class Node(defaultdict):
    def __init__(self):
        super().__init__(Node)
        self.index = -1

class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.root = Node()
        for i,word in enumerate(words):
            longw = word + "#" + word
            for j in range(len(word)):                  
                cur = self.root
                cur.index = i
                for c in longw[j:]:
                    cur = cur[c]
                    cur.index = i

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        word = suffix+'#'+prefix
        cur = self.root
        for c in word:
            if c not in cur: return -1
            cur = cur[c]
        return cur.index



        

if __name__ == "__main__":
# Your WordFilter object will be instantiated and called as such:
    wordFilter = WordFilter(["apple"])
    print(wordFilter.f("a", "e"))  # return 0, because the word at index 0 has prefix = "a" and suffix = 'e".
    ["WordFilter","f","f","f","f","f","f","f","f","f","f"]
    words = ["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa",
            "cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"]
    wordFilter = WordFilter(words)
    print(wordFilter.f("bccbacbcba","a"))
    print(wordFilter.f("ab","abcaccbcaa"))
    #["a","aa"],["cabaaba","abaaaa"],["cacc","accbbcbab"],["ccbcab","bac"],["bac","cba"],["ac","accabaccaa"],["bcbb","aa"],["ccbca","cbcababac"]