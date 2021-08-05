'''
-Hard-

Given an array of n distinct non-empty strings, you need to generate minimal possible 
abbreviations for every word following rules below.

Begin with the first character and then the number of characters abbreviated, which 
followed by the last character.
If there are any conflict, that is more than one words share the same abbreviation, a 
longer prefix is used instead of only the first character until making the map from word 
to abbreviation become unique. In other words, a final abbreviation cannot map to more 
than one original words.
If the abbreviation doesn't make the word shorter, then keep it as original.
Example:

Input: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
Note:
Both n and the length of each word will not exceed 400.
The length of each word is greater than 1.
The words consist of lowercase English letters only.
The return answers should be in the same order as the original array.
Similar Questions
Valid Word Abbreviation Easy
Minimum Unique Word Abbreviation Hard

'''
import collections

class TrieNode(object):
    def __init__(self):
        self.children =  [None] * 26
        self.count = 0

class IndexdWord(object):
    def __init__(self, w, i):
        self.word = w
        self.index = i



class Solution(object):
    def wordsAbbreviationTLE(self, dict):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        # brute force TLE at lintcode
        
        def abbreviate(s, k):
            return s if k >= len(s) - 2 else s[:k] + str(len(s) - k - 1) + s[-1]
        n = len(dict)
        pre = [1]*n
        res = ['']*n
        for i in range(n):
            res[i] = abbreviate(dict[i], pre[i])
        for i in range(n):
            while True:
                st = set()
                for j in range(i+1, n):
                    if res[i] == res[j]: st.add(j)
                if not st: break
                st.add(i)
                for a in st:
                    pre[a] += 1 
                    res[a] = abbreviate(dict[a], pre[a])
        return res

    def wordsAbbreviation(self, dict):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        words = dict
        def longest_common_prefix(a, b):
            i = 0
            while i < len(a) and i < len(b) and a[i] == b[i]:
                i += 1
            return i

        ans = [None for _ in words]

        groups = collections.defaultdict(list)
        for index, word in enumerate(words):
            groups[len(word), word[0], word[-1]].append((word, index))

        for (size, first, last), enum_words in groups.items():
            enum_words.sort()
            lcp = [0] * len(enum_words)
            for i, (word, _) in enumerate(enum_words):
                if i:
                    word2 = enum_words[i-1][0]
                    lcp[i] = longest_common_prefix(word, word2)
                    lcp[i-1] = max(lcp[i-1], lcp[i])

            for (word, index), p in zip(enum_words, lcp):
                delta = size - 2 - p
                if delta <= 1:
                    ans[index] = word
                else:
                    ans[index] = word[:p+1] + str(delta) + last

        return ans
    
    


    def wordsAbbreviationTrieTLE(self, dict):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        def abbreviate(s, k):
            return s if k >= len(s) - 2 else s[:k] + str(len(s) - k - 1) + s[-1]
        words = dict
        groups = collections.defaultdict(list)
        ans = [None for _ in words]
        for i,word in enumerate(words):
            abbr = abbreviate(word, 1)
            groups[abbr].append(IndexdWord(word, i))
        for group in groups.values():
            root = TrieNode()
            for iw in group:
                cur = root
                for c in iw.word[1:]:
                    idx = ord(c)-ord('a')
                    if not cur.children[idx]:  
                        cur.children[idx] = TrieNode()
                    cur.count += 1
                    cur = cur.children[idx]
            for iw in group:
                cur = root
                i = 1
                for c in iw.word[1:]:
                    if cur.count == 1: break                    
                    cur = cur.children[ord(c)-ord('a')]
                    i += 1
                ans[iw.index] = abbreviate(iw.word, i)

        return ans

    def wordsAbbreviationTrie(self, dict):
        # write your code here
        words = dict
        groups = collections.defaultdict(list)
        for index, word in enumerate(words):
            groups[len(word), word[0], word[-1]].append((word, index))

        ans = [None] * len(words)
        Trie = lambda: collections.defaultdict(Trie)
        COUNT = False
        for group in groups.itervalues():
            trie = Trie()
            for word, _ in group:
                cur = trie
                for letter in word[1:]:
                    cur[COUNT] = cur.get(COUNT, 0) + 1
                    cur = cur[letter]

            for word, index in group:
                cur = trie
                for i, letter in enumerate(word[1:], 1):
                    if cur[COUNT] == 1: break
                    cur = cur[letter]
                if len(word) - i - 1 > 1:
                    ans[index] = word[:i] + str(len(word) - i - 1) + word[-1]
                else:
                    ans[index] = word
        return ans






if __name__ == "__main__":
    words = ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
    print(Solution().wordsAbbreviation(words))
    print(Solution().wordsAbbreviationTrie(words))