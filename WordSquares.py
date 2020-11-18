'''
Given a set of words (without duplicates), find all word squares you 
can build from them.

A sequence of words forms a valid word square if the kth row and 
column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a 
word square because each word reads the same both horizontally and 
vertically.

b a l l
a r e a
l e a d
l a d y
Note:
There are at least 1 and at most 1000 words.
All words will have the exact same length.
Word length is at least 1 and at most 5.
Each word contains only lowercase English alphabet a-z.

Example 1:

Input:
["area","lead","wall","lady","ball"]
Output:
[
[  "wall",
   "area",
   "lead",
   "lady"
],
[  "ball",
   "area",
   "lead",
   "lady"
]
]


Explanation:
The output consists of two word squares. The order of output does not 
matter (just the order of words in each word square matters).

Example 2:

Input:
["abat","baba","atan","atal"]
Output:
[
[ "baba",
"abat",
"baba",
"atan"
],
[ "baba",
"abat",
"baba",
"atal"
]
]


Explanation:
The output consists of two word squares. The order of output does not 
matter (just the order of words in each word square matters).

'''
from collections import defaultdict

class Node(defaultdict):
    def __init__(self):
        super().__init__(Node)
        #self.terminal = False
        self.wordlist = set()

class Solution(object):
    def findSquare(self, words):
        """        
        :type wordDict: List[str]
        :rtype: List(List[str]))        
        """
        trie = Node()
        n = len(words[0])
        cur = trie['']
        cur.wordlist = set(words)        
        for w in words:
            cur = trie
            for c in w:
                cur = cur[c]
                cur.wordlist.add(w)
        
        def exist(word):
            cur = trie
            for c in word:
                if c not in cur:
                    return False
                cur = cur[c]
            return True

        def search(word):
            cur = trie
            if not word:
                cur = trie['']
            else:
                for c in word:
                   cur = cur[c]
            return cur.wordlist        
        
        mat = [['' for _ in range(n)] for _ in range(n)]    
        res = []        
        # helper function fills in the mat array layer by layer 
        # each layer is represented by (i,i), (i,i+1..n) and
        # (i+1..n,i)
        def helper(i):
            if i == n:                       
                temp = [''.join(mat[j]) for j in range(n)]
                res.append(temp)
                return
            key = ''.join(mat[i][0:i])            
            for s in search(key):                
                mat[i][i] = s[i]                   
                for j in range(i+1,n):
                    mat[i][j] = s[j]
                    mat[j][i] = s[j]                                     
                    if not exist(''.join(mat[j][:i+1])):                       
                       break
                else:                    
                    helper(i+1)
        helper(0)
        return res

if __name__ == "__main__":
    print(Solution().findSquare(["area","lead","wall","lady","ball"]))
