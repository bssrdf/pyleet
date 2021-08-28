'''
-Medium-
*Union Find*
*BFS*
Given a list of pairs of equivalent words synonyms and a sentence text, 
Return all possible synonymous sentences sorted lexicographically.
 

Example 1:

Input:
synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]],
text = "I am happy today but was sad yesterday"
Output:
["I am cheerful today but was sad yesterday",
"I am cheerful today but was sorrow yesterday",
"I am happy today but was sad yesterday",
"I am happy today but was sorrow yesterday",
"I am joy today but was sad yesterday",
"I am joy today but was sorrow yesterday"]
Example 2:

Input: synonyms = [["happy","joy"],["cheerful","glad"]], text = "I am happy today but was sad yesterday"
Output: ["I am happy today but was sad yesterday","I am joy today but was sad yesterday"]
Example 3:

Input: synonyms = [["a","b"],["c","d"],["e","f"]], text = "a c e"
Output: ["a c e","a c f","a d e","a d f","b c e","b c f","b d e","b d f"]
Example 4:

Input: synonyms = [["a","QrbCl"]], text = "d QrbCl ya ya NjZQ"
Output: ["d QrbCl ya ya NjZQ","d a ya ya NjZQ"]
 

Constraints:

0 <= synonyms.length <= 10
synonyms[i].length == 2
synonyms[i][0] != synonyms[i][1]
All words consist of at most 10 English letters only.
text is a single space separated sentence of at most 10 words.
Hints
Find all synonymous groups of words.
Use union-find data structure.
By backtracking, generate all possible statements.

'''

from collections import defaultdict, deque

class UnionFind(object):
    """
    groups: word to group mapping
    """
    
    def __init__(self, pairs = None):
        self.groups = {}
        '''
        for w1,w2 in pairs:
            self.groups[w1] = w1
            self.groups[w2] = w2

        for w1,w2 in pairs:
            self.union(w1, w2)
        '''

    def find(self, word):
        """
        Return the group of the given word
        Add the word if the word does not already exist
        """
        if word not in self.groups:
            self.groups[word] = word
        return self.groups[word]
        #if word == self.groups[word]:
        #    return word
        #return self.find(self.groups[word])

    def union(self, word1, word2):
        """
        Union the 2 groups and keep the lexicographically smallest group
        """
        group1, group2 = self.find(word1), self.find(word2) # O(1)
        
        if group1 == group2: # already in the same group
            return
        
        if group1 > group2: # let group1 be the lexicographically smaller group
            group1, group2 = group2, group1
    
        for word in self.groups: # worst case O(# words in group) which is less than O(N)
            if self.groups[word] == group2:
                self.groups[word] = group1

class Solution(object):
    def generateSentences(self, synonyms, text):
        """
        :type synonyms: List[List[str]], N pairs
        :type text: str, M words
        :rtype: List[str]
        """
        #return self.generateSentencesBFS(synonyms, text)
        return self.generateSentencesUnionFind(synonyms, text)

        
    def generateSentencesBFS(self, synonyms, text):
        graph = defaultdict(list)
        for w1, w2 in synonyms:
            graph[w1].append(w2)
            graph[w2].append(w1)
            
        words = text.split(' ')
        res = [[]]
        
        def bfs(word):
            res = []
            
            candidates = deque([word])
            visited = set([word])
            
            while candidates:
                candidate = candidates.popleft()
                res.append(candidate)
                for synonym in graph[candidate]:
                    if synonym not in visited:
                        candidates.append(synonym)
                        visited.add(synonym)
            return res

        for word in words:
            candidates = sorted(bfs(word))
            res = [r + [candidate] for r in res for candidate in candidates]
            
        return [" ".join(sentence) for sentence in res]   
    
    def generateSentencesUnionFind(self, synonyms, text):
        uf = UnionFind()
        
        # overall this is probably O(NlogN) instead of O(N^2)
        for w1, w2 in synonyms: # O(N)
            uf.union(w1, w2)
        
        words = text.split(" ")
        res = []
        
        def backtrack(idx, sentence):
            if idx == len(words): # we've reached the end
                res.append(" ".join(sentence))
            else:
                word = words[idx]
                group = uf.groups.get(word) # O(1)
                
                if group:
                    candidates = sorted(word for word in uf.groups if uf.groups[word] == group) # O(N)
                    for candidate in candidates:
                        backtrack(idx + 1, sentence + [candidate])
                else:
                    backtrack(idx + 1,  sentence + [word])
                        
        backtrack(0, [])
        return res

if __name__ == "__main__":
    synonyms = [["happy","joy"],["cheerful","glad"]]
    text = "I am happy today but was sad yesterday"
    print(Solution().generateSentences(synonyms, text))
    synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]]
    text = "I am happy today but was sad yesterday"
    print(Solution().generateSentences(synonyms, text))
