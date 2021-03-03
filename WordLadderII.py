'''
-Hard-

*BFS*
*Bidirectional BFS*

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a 
sequence of words such that:

The first word in the sequence is beginWord.
The last word in the sequence is endWord.
Only one letter is different between each adjacent pair of words in the sequence.
Every word in the sequence is in wordList.
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest 
transformation sequences from beginWord to endWord, or an empty list if no such sequence exists.
 
Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the strings in wordList are unique.

'''
import collections
import string

class Solution(object):
 
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: List[str]
        :rtype: List[List[int]]
        """ 
        
        def construct_paths(source, dest, tree):
            if source == dest: 
                return [[source]]
            #return [[source] + path for succ in tree[source]
             #                       for path in construct_paths(succ, dest, tree)]
            allpaths=[]    
            for succ in tree[source]:
                for path in construct_paths(succ, dest, tree):
                    allpaths.append([source] + path)
            return allpaths
                

        def add_path(tree, word, neigh, is_forw):
            if is_forw: tree[word]  += neigh,
            else:       tree[neigh] += word,

        def bfs_level(this_lev, oth_lev, tree, is_forw, words_set):
            if not this_lev: return False
            if len(this_lev) > len(oth_lev):
                # bidirectional BFS: alternate direction when one direction has
                # more nodes                
                return bfs_level(oth_lev, this_lev, tree, not is_forw, words_set)
            for word in (this_lev | oth_lev):
                words_set.discard(word)
            next_lev, done = set(), False
            while this_lev:
                word = this_lev.pop()
                for c in string.ascii_lowercase:
                    for index in range(len(word)):
                        neigh = word[:index] + c + word[index+1:]
                        if neigh in oth_lev:
                            done = True
                            add_path(tree, word, neigh, is_forw)                
                        if not done and neigh in words_set:
                            next_lev.add(neigh)
                            add_path(tree, word, neigh, is_forw)
            return done or bfs_level(next_lev, oth_lev, tree, is_forw, words_set)
                            
        #tree, path, paths = collections.defaultdict(list), [begin], []
        word_set = set(wordList)
        if endWord not in wordList: return []
        tree = collections.defaultdict(list)
        is_found = bfs_level(set([beginWord]), set([endWord]), tree, True, word_set)
        #print(tree)
        # note: after bidirectional BFS meets in the middle, tree contains only
        # shortest paths; the longer ones have not yet been explored.        
        return construct_paths(beginWord, endWord, tree)
        


if __name__ == "__main__":
    assert Solution().findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == [
        ["hit", "hot", "dot", "dog", "cog"],
        ["hit", "hot", "lot", "log", "cog"]
    ]