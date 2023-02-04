'''
-Medium-

Given a string s and an array of strings words, return the number of words[i] that is 
a subsequence of s.

A subsequence of a string is a new string generated from the original string with some 
characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
Example 2:

Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2
 

Constraints:

1 <= s.length <= 5 * 10^4
1 <= words.length <= 5000
1 <= words[i].length <= 50
s and words[i] consist of only lowercase English letters.


'''
import collections
class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        def match(str, sub):
            i = j = 0
            while i < len(str):
                if str[i] == sub[j]: 
                    j += 1
                i += 1
                if j == len(sub):
                    return True
            return False
        succ, fail = set(), set()
        res = 0
        for w in words:
            if w in succ: 
                res += 1
                continue
            elif w in fail: continue
            if match(s, w):
                succ.add(w)
                res += 1
            else:
                fail.add(w)
        return res

    def numMatchingSubseqFast(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        waiting = collections.defaultdict(list)
        for w in words:
            waiting[w[0]].append(iter(w[1:]))
        for c in s:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)
            #for ch in waiting.keys():
            #   print(ch,waiting[ch])
        return len(waiting[None])
        





if __name__ == "__main__":
    #print(Solution().numMatchingSubseq(s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]))
    #print(Solution().numMatchingSubseq(s = "abcde", words = ["a","bb","acd","ace"]))
    print(Solution().numMatchingSubseqFast(s = "abcde", words = ["a","bb","acd","ace"]))
    #print(Solution().numMatchingSubseq("qlhxagxdqh", ["qlhxagxdq","qlhxagxdq","lhyiftwtut","yfzwraahab"]))