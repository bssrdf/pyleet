'''
-Medium-

Design a data structure that is initialized with a list of different words. Provided a string, 
you should determine if you can change exactly one character in this string to match any word 
in the data structure.

Implement the MagicDictionary class:

MagicDictionary() Initializes the object.
void buildDict(String[] dictionary) Sets the data structure with an array of distinct strings dictionary.
bool search(String searchWord) Returns true if you can change exactly one character in 
searchWord to match any string in the data structure, otherwise returns false.
 

Example 1:

Input
["MagicDictionary", "buildDict", "search", "search", "search", "search"]
[[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
Output
[null, null, false, true, false, false]

Explanation
MagicDictionary magicDictionary = new MagicDictionary();
magicDictionary.buildDict(["hello", "leetcode"]);
magicDictionary.search("hello"); // return False
magicDictionary.search("hhllo"); // We can change the second 'h' to 'e' to match "hello" so we return True
magicDictionary.search("hell"); // return False
magicDictionary.search("leetcoded"); // return False
 

Constraints:

1 <= dictionary.length <= 100
1 <= dictionary[i].length <= 100
dictionary[i] consists of only lower-case English letters.
All the strings in dictionary are distinct.
1 <= searchWord.length <= 100
searchWord consists of only lower-case English letters.
buildDict will be called only once before search.
At most 100 calls will be made to search.


'''

from collections import defaultdict

class Node(defaultdict):
    def __init__(self):
        super().__init__(Node)
        self.terminal = False


class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()        

    def buildDict(self, dictionary):
        """
        :type dictionary: List[str]
        :rtype: None
        """
        for word in dictionary:
            cur = self.root
            for c in word:
                cur = cur[c]
            cur.terminal = True

    def search(self, searchWord):
        """
        :type searchWord: str
        :rtype: bool
        """
        def helper(cur, remain, word):
            if not word:
                return True if remain == 0 and cur.terminal else False
            for c in cur:
                if c == word[0]:
                    if helper(cur[c], remain, word[1:]):
                        return True
                elif remain == 1:
                    if helper(cur[c], 0, word[1:]):
                        return True
            return False
        return helper(self.root, 1, searchWord)

                

if __name__ == "__main__":
    '''
    magicDictionary = MagicDictionary()
    magicDictionary.buildDict(["hello", "leetcode"])
    print(magicDictionary.search("hello")) # return False
    print(magicDictionary.search("hhllo")) # We can change the second 'h' to 'e' to match "hello" so we return True
    print(magicDictionary.search("hell")) # return False
    print(magicDictionary.search("leetcoded")) # return False
    '''


    magicDictionary = MagicDictionary()
    magicDictionary.buildDict(["hello", "hallo", "leetcode"])
    print(magicDictionary.search("hello")) # return False
    print(magicDictionary.search("hhllo")) # We can change the second 'h' to 'e' to match "hello" so we return True
    print(magicDictionary.search("hell")) # return False
    print(magicDictionary.search("leetcoded")) # return False