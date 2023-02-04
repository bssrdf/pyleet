'''
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.

'''

from collections import defaultdict

class Node(defaultdict):
    def __init__(self):
        super().__init__(Node)
        self.terminal = False        


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        cur = self.root
        for c in word:    
            cur = cur[c]
        cur.terminal = True
        


        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return cur.terminal

        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))   # returns true
    print(trie.search("app"))     # returns false
    print(trie.startsWith("app")) # returns true
    trie.insert("app");   
    print(trie.search("app"))     # returns true



    