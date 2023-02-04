'''
-Medium-

Given a string s, return the number of distinct substrings of s.

A substring of a string is obtained by deleting any number of characters 
(possibly zero) from the front of the string and any number (possibly zero) 
from the back of the string.

 

Example 1:

Input: s = "aabbaba"
Output: 21
Explanation: The set of distinct strings is ["a","b","aa","bb","ab","ba","aab","abb","bba","aba","aabb","abba","bbab","baba","aabba","abbab","bbaba","aabbab","abbaba","aabbaba"]
Example 2:

Input: s = "abcdefg"
Output: 28
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
 

Follow up: Can you solve this problem in O(n) time complexity?


Hint 1

Calculate the prefix hashing array for s.

Hint 2

Use the prefix hashing array to calculate the hashing value of each substring.

Hint 3

Compare the hashing values to determine the unique substrings.

Hint 4

There could be collisions if you use hashing, what about double hashing.

'''




class SuffixArray:
    """ by Karp, Miller, Rosenberg 1972

        s is the string to analyze.

        P[k][i] is the pseudo rank of s[i:i+K] for K = 1<<k
        among all strings of length K. Pseudo, because the pseudo rank numbers are
        in order but not necessarily consecutive.
    
        Initialization of the data structure has complexity O(n log^2 n).
    """
    def __init__(self, s):
        self.n = len(s)
        if self.n == 1:                                         # special case: single char strings
            self.P = [[0]]
            self.suf_sorted = [0]
            return
        self.P = [list(map(ord, s))]
        k = 1
        length = 1                                              # length is 2 ** (k - 1)
        while length < self.n:
            L = []                                              # prepare L
            for i in range(self.n - length):
                L.append((self.P[k - 1][i], self.P[k - 1][i + length], i))
            for i in range(self.n - length, self.n):            # pad with -1
                L.append((self.P[k - 1][i], -1, i))
            L.sort()                                            # bucket sort would be quicker
            self.P.append([0] * self.n)                         # produce k-th row in P
            for i in range(self.n):
                if i > 0 and L[i-1][:2] == L[i][:2]:            # same as previous
                    self.P[k][ L[i][2] ] = self.P[k][ L[i-1][2] ]
                else:
                    self.P[k][ L[i][2] ] = i
            k += 1
            length <<= 1                                        # or *=2 as you prefer
        self.suf_sorted = [0] * self.n                          # generate the inverse:
        for i, si in enumerate(self.P[-1]):                     # lexic. sorted suffixes
            self.suf_sorted[si] = i    

    def minimal_lexicographical_rotation(s):
        """ returns i such that s[i:]+s[:i] is minimal,
        for n = len(s).
        Could an be solved in linear time,
        but this is an easy O(n log^2 n) solution.
        Uses the observation, that solution i also minimizes (s+s)[i:]
        """
        A = SuffixArray(s + s)
        # find index 0 <= i < len(s) with smallest rank
        best = 0
        for i in range(1, len(s)):
            if A.P[-1][i] < A.P[-1][best]:
                best = i
        return best
    
    def longest_common_prefix(self, i, j):
        """returns the length of 
        the longest common prefix of s[i:] and s[j:].
        complexity: O(log n), for n = len(s).
        """
        if i == j:
            return self.n - i                       # length of suffix
        answer = 0
        length = 1 << (len(self.P) - 1)             # length is 2 ** k
        for k in range(len(self.P) - 1, -1, -1):
            length = 1 << k
            if self.P[k][i] == self.P[k][j]:        # aha, s[i:i+length] == s[j:j+length]
                answer += length
                i += length
                j += length
                if i == self.n or j == self.n:      # not needed if s is appended by $
                    break
            length >>= 1
        return answer

    def number_substrings(self):
        answer = self.n - self.suf_sorted[0] 
        for i in range(1, self.n):
            r = self.longest_common_prefix(self.suf_sorted[i-1], self.suf_sorted[i])
            answer += self.n - self.suf_sorted[i] - r
        return answer

class Node(object): 
    def __init__(self):
        self.children =  [None]*26
        self.count = 0

def LCP(a,b):
	ai = len(a)
	ac = 0
	bc = 0
	maxLength = 0
	while(ac < ai):
		if(a[ac] == b[bc]):
			maxLength +=1
			ac += 1
			bc += 1
		else:
			return maxLength
	return maxLength


class Solution(object):

    def __init__(self):
        self.trie = Node()
        self.result = 0
        
    def countDistinct(self, s):

        for i in range(len(s)):
            self.insert(self.trie, s, i)

        for i in range(len(s)):
            self.find(self.trie, s, i)

        return self.result

    def insert(self,  trie,  s, index) :
        if index >= len(s):
            return
        i = ord(s[index]) - ord('a')
        if not trie.children[i]: 
            trie.children[i] = Node()

        self.insert(trie.children[i], s, index + 1)

    def find(self, trie, s, index):
        if index >= len(s):
            return        

        i = ord(s[index]) - ord('a')
        trie.children[i].count += 1

        if trie.children[i].count == 1:
            self.result += 1

        self.find(trie.children[i], s, index + 1)
    
    def countDistinct2(self, a):
        SuffixArray =  [a[i:] for i in range(len(a))]
        SuffixArray.sort()
        count = 0
        for i in range(len(SuffixArray)):
            #Characters not part of the LCP contribute to unique substrings
            count += len(SuffixArray[i]) - LCP(SuffixArray[i-1],SuffixArray[i])
        return count


if __name__ == "__main__":
    print(Solution().countDistinct("aabbaba"))
    print(Solution().countDistinct("abcdefg"))
    print(Solution().countDistinct2("aabbaba"))
    print(Solution().countDistinct2("abcdefg"))