'''
Given a list of words, find words in that list that are made up of other words 
in the list. For example, if the list were ["race", "racecar", "car"],  
return ["racecar"].

'''

from collections import defaultdict

class Node(defaultdict):
    def __init__(self):
        super().__init__(Node)
        self.terminal = False

class Trie(object):

    def __init__(self, wl):        
        self.root = Node()
        for w in wl:
            self.add_word(w)

    def __contains__(self, word):
        node = self.root
        for c in word:
            node = node.get(c)
            if node is None:
                return False
        return node.terminal

    def add_word(self, word):
        node = self.root
        for c in word:
            node = node[c]
        node.terminal = True

    def is_combination(self, word):
        node= self.root
        for i,c in enumerate(word):
            node = node.get(c)
            if not node:
                break
            if node.terminal and word[i+1:] in self:
                return True
        return False

class Solution(object):

    def findCompoundWord(self, words):
        return [w for w in words if Trie(words).is_combination(w)]


if __name__ == "__main__":

    print(Solution().findCompoundWord(["race", "racecar", "car", "after", "thought", "afterthought"]))    
    

