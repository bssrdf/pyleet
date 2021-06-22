'''
-Medium-
*Trie*

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string 
containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.

'''

from collections import defaultdict

class Node(defaultdict):
    def __init__(self):
        super().__init__(Node)
        self.terminal = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.root
        for c in word:
            node = node[c]
        node.terminal = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        node = self.root        
        def dfs(root, word):
            if not word:
                return root.terminal                   
            c = word[0] 
            if c == '.':      
                if len(root) == 0:
                    return False                              
                for k in root:
                    if dfs(root[k], word[1:]):   
                       return True
                return False                
            else:
                node = root.get(c)                    
                if node is None:
                    return False                    
                return dfs(node, word[1:])

        return dfs(node, word)

if __name__ == "__main__":
    obj = WordDictionary()
    obj.addWord("bad")
    obj.addWord("dad")
    obj.addWord("mad")
    print(obj.search("pad"))
    print(obj.search("bad"))
    print(obj.search(".ad"))
    print(obj.search("b.."))

    obj = WordDictionary()
    obj.addWord("a")
    obj.addWord("a")    
    print(obj.search("."))
    print(obj.search("a"))
    print(obj.search("aa"))
    print(obj.search("a"))
    print(obj.search(".a"))
    print(obj.search("a."))

    obj = WordDictionary()
    obj.addWord("at")
    obj.addWord("and")    
    obj.addWord("an")
    obj.addWord("add")    
    print(obj.search("a"))
    print(obj.search(".at"))
    obj.addWord("bat") 
    print(obj.search(".at"))



