'''

Given two sentences words1, words2 (each represented as an array of strings), and a list of 
similar word pairs pairs, determine if two sentences are similar.

For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] 
are similar, if the similar word pairs are pairs = [["great", "good"], ["fine", "good"],
["acting","drama"], ["skills","talent"]].

Note that the similarity relation is transitive. For example, if "great" and "good" are 
similar, and "fine" and "good" are similar, then "great" and "fine" are similar.

Similarity is also symmetric. For example, "great" and "fine" being similar is the same 
as "fine" and "great" being similar.

Also, a word is always similar with itself. For example, the sentences words1 = ["great"], 
words2 = ["great"], pairs = [] are similar, even though there are no specified similar 
word pairs.

Finally, sentences can only be similar if they have the same number of words. So a sentence 
like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

Note:

The length of words1 and words2 will not exceed 1000.
The length of pairs will not exceed 2000.
The length of each pairs[i] will be 2.
The length of each words[i] and pairs[i][j] will be in the range [1, 20].

'''

from collections import defaultdict
from collections import deque
from UnionFindSet import UnionFindSet

class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        if len(words1) != len(words2):
            return False
        mapping = defaultdict(list)
        for p in pairs:
            mapping[p[0]].append(p[1])
            mapping[p[1]].append(p[0])
        for k in mapping:
            print(k, mapping[k])
        for w1,w2 in zip(words1, words2):
            visited = set()
            if not self.dfs(w1, w2, mapping, visited):
                return False
        return True

    def dfs(self, src, dst, mapping, visited):
        if src == dst:
            return True
        visited.add(src)
        for w in mapping[src]:
            if w in visited:
                continue
            if self.dfs(w, dst, mapping, visited):
                return True
        return False
    
    def areSentencesSimilarTwoBFS(self, words1, words2, pairs):
        if len(words1) != len(words2):
            return False
        mapping = defaultdict(list)
        for p in pairs:
            mapping[p[0]].append(p[1])
            mapping[p[1]].append(p[0])
        def bfs(src, dst):
            
            candidates = deque([src])
            visited = set([src])
            
            while candidates:
                candidate = candidates.popleft()
                if candidate == dst:
                    return True
                for synonym in mapping[candidate]:
                    if synonym not in visited:
                        candidates.append(synonym)
                        visited.add(synonym)
            return False
        for w1,w2 in zip(words1, words2):
            if not bfs(w1, w2):
                return False
        return True
    
    def areSentencesSimilarTwoUF(self, words1, words2, pairs):
        if len(words1) != len(words2):
            return False
        mapping = {}
        n = 1
        for w in words1+words2:
            if w not in mapping:               
               mapping[w] = n
               n += 1             
        
        for p in pairs:
            for w in p:
              if w not in mapping:
                 mapping[w] = n
                 n += 1
        
        uf = UnionFindSet(n=n)
        for p in pairs:
            uf.union(mapping[p[0]], mapping[p[1]])
        for w1, w2 in zip(words1, words2):
            if uf.find(mapping[w1]) != uf.find(mapping[w2]):
                return False
        return True   

    def areSentencesSimilarTwoUF2(self, words1, words2, pairs):
        if len(words1) != len(words2):
            return False        
        words = set()
        for p in pairs:
           words.add(p[0])
           words.add(p[1]) 
        uf = UnionFindSet(items=list(set(words1+words2)|words))
        for p in pairs:
            uf.union(p[0], p[1])
        for w1, w2 in zip(words1, words2):
            if uf.find(w1) != uf.find(w2):
                return False
        return True   
        

print(Solution().areSentencesSimilarTwoUF(["great", "acting", "skills"], 
#print(Solution().areSentencesSimilarTwoUF(["acting", "great","skills"], 
                ["fine", "drama", "talent"],
                [["great", "good"], ["fine", "good"],
                ["acting","drama"], ["skills","talent"]]))

s1 = ["7", "5", "4", "11", "13", "15", "19", "12", "0", "10"]
s2 = ["16", "1", "7", "3", "15", "10", "13", "2", "19", "8"]
pairs = [["6", "18"], ["8", "17"], ["1", "13"], ["0", "8"], ["9", "14"], ["11", "17"], ["11", "19"], ["13", "16"], ["0", "18"], ["3", "11"], ["1", "9"], ["2", "11"], ["2", "4"], ["0", "19"], ["8", "12"], ["8", "19"], ["16", "19"], ["1", "11"], ["2", "18"], ["0", "16"], ["7", "11"], ["6", "8"], ["9", "17"], ["8", "16"], ["3", "13"], ["7", "9"], ["7", "10"], ["3", "6"], ["15", "19"], ["1", "5"], ["2", "14"], ["1", "18"], ["8", "15"], ["14", "19"], ["3", "17"], ["6", "10"], ["5", "17"], ["10", "15"], ["1", "10"], ["4", "6"]]
print(Solution().areSentencesSimilarTwoUF(s1, s2, pairs))
print(Solution().areSentencesSimilarTwoUF2(s1, s2, pairs))
print(Solution().areSentencesSimilarTwoBFS(s1, s2, pairs))

