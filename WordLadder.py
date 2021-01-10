# Time:  O(n * d), n is length of string, d is size of dictionary
# Space: O(d)
#
# Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:
# 
# Only one letter can be changed at a time
# Each intermediate word must exist in the dictionary
# For example,
# 
# Given:
# start = "hit"
# end = "cog"
# dict = ["hot","dot","dog","lot","log"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# 
# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
#
from collections import deque
# BFS
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, beginWord, endWord, wordList):

        wordLists = set(wordList)        
        queue = deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            #print word, length
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordLists:
                        wordLists.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0
        
    def ladderLengthPrep(self, beginWord, endWord, wordList):
        
        def construct_dict(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i+1:]
                    d[s] = d.get(s, []) + [word]
            return d
            
        def bfs_words(begin, end, dict_words):
            queue, visited = deque([(begin, 1)]), set()
            while queue:
                word, steps = queue.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == end:
                        return steps
                    for i in range(len(word)):
                        s = word[:i] + "_" + word[i+1:]
                        neigh_words = dict_words.get(s, [])
                        for neigh in neigh_words:
                            if neigh not in visited:
                                queue.append((neigh, steps + 1))
            return 0
        
        d = construct_dict(wordList | set([beginWord, endWord]))
        #print d
        return bfs_words(beginWord, endWord, d)
      

if __name__ == "__main__":
    print(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "lof", "cof"]))
    #print Solution().ladderLength("hit", "cog", set(["hot", "dot", "dog", "lot", "log", "cog"]))
    #print Solution().ladderLengthPrep("hit", "cog", set(["hot", "dot", "dog", "lot", "lof", "cof"]))
