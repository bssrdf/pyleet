'''
-Medium-

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 3 dots in word for search queries.
At most 104 calls will be made to addWord and search.

'''

from collections import defaultdict

class Node(defaultdict):
    def __init__(self):
        super().__init__(Node)
        self.terminal = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for c in word:
            node = node[c]
        node.terminal = True
       

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
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
    

class TNode:
    def __init__(self, key = None):
        self.terminal = False
        self.c = key
        self.left = None
        self.mid = None
        self.right = None

class WordDictionary2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = None

    def addWord(self, word: str) -> None:
        self.root = self._addWord(self.root, word, 0)

    def _addWord(self, node, word, d) -> TNode:
        c = word[d]
        if not node: node = TNode(c)
        if c < node.c:
            node.left = self._addWord(node.left, word, d)
        elif c > node.c:
            node.right = self._addWord(node.right, word, d)
        elif d < len(word) - 1:
            node.mid = self._addWord(node.mid, word, d + 1)
        else:
            node.terminal = True
        return node


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self._search(self.root, word, 0)

    def _search(self, node, word, d) -> bool:
        if not node: return False
        c = word[d]
        if c == '.':
            if d == len(word) - 1: return node.terminal
            if self._search(node.mid, word, d + 1): return True
            if self._search(node.left, word, d): return True
            if self._search(node.right, word, d): return True
            return False
        else:
            if c < node.c: return self._search(node.left, word, d)
            elif c > node.c: return self._search(node.right, word, d)
            elif d < len(word)-1: return self._search(node.mid, word, d + 1)
            else: return node.terminal

wordDictionary = WordDictionary2()
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
print(wordDictionary.root.c)
print(wordDictionary.search("pad")) # return False
print(wordDictionary.search("bad")) # return True
print(wordDictionary.search(".ad")) # return True
print(wordDictionary.search("b..")) # return True