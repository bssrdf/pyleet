'''
-Medium-

*Hash Table*
*Bijection*

Given a list of strings words and a string pattern, return a list of words[i] 
that match pattern. You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that 
after replacing every letter x in the pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every 
letter maps to another letter, and no two letters map to the same letter.

 

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.
Example 2:

Input: words = ["a","b","c"], pattern = "a"
Output: ["a","b","c"]
 

Constraints:

1 <= pattern.length <= 20
1 <= words.length <= 50
words[i].length == pattern.length
pattern and words[i] are lowercase English letters.

'''

class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def match(s, t):
            m, q = {}, set()
            for c, p in zip(s, t):
                if p not in m:
                    if c not in q:
                        m[p] = c
                        q.add(c)
                    else:
                        return False
                elif m[p] != c: return False    
            return True
        return [w for w in words if match(w, pattern)]
        


if __name__ == "__main__":
    print(Solution().findAndReplacePattern(words = ["abc","deq","mee",
                                               "aqq","dkd","ccc"], pattern = "abb"))
    print(Solution().findAndReplacePattern(["ef","fq","ao","at","lx"], "ya"))