'''
Given two words (beginWord and endWord), and a dictionary's word list, find all 
shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
All words have the same length.
All words contain only lowercase alphabetic characters.
'''
import collections
import string

class Solution(object):
 
    def findLadders(self, begin, end, words_list):   
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """ 
        
        """
        DFS to reproduce the paths
        typical recursive call         
        """
        def construct_paths(source, dest, tree):
            if source == dest: 
                return [[source]]
            return [[source] + path for succ in tree[source]
                                    for path in construct_paths(succ, dest, tree)]

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
        tree = collections.defaultdict(list)
        is_found = bfs_level(set([begin]), set([end]), tree, True, words_list)
        #print tree
        # note: after bidirectional BFS meets in the middle, tree contains only
        # shortest paths; the longer ones have not yet been explored.        
        return construct_paths(begin, end, tree)
        


if __name__ == "__main__":
    assert Solution().findLadders("hit", "cog", {"hot", "dot", "dog", "lot", "log"}) == [
        ["hit", "hot", "dot", "dog", "cog"],
        ["hit", "hot", "lot", "log", "cog"]
    ]