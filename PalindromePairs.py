'''

-Hard-
*Hash Table*
*Trie*

Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given 
list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

 

Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]
 

Constraints:

1 <= words.length <= 5000
0 <= words[i].length <= 300
words[i] consists of lower-case English letters.


'''

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        m = {}
        def isValid(t):
            l, r = 0, len(t)-1
            while l <= r:
                if t[l] != t[r]: return False
                l += 1
                r -= 1
            return True
        for i,v in enumerate(words): m[v] = i
        for i in range(len(words)):
            l, r = 0, 0
            while l <= r:
                t = ''.join(reversed(words[i][l:r]))                
                left = r if l == 0 else 0
                lth = len(words[i])-r if l == 0 else l
                if t in m and i != m[t] and isValid(words[i][left:left+lth]):
                    if l == 0: res.append([i, m[t]])
                    else: res.append([m[t], i])
                if r < len(words[i]): r += 1
                else: l += 1
        return res

    

    def palindromePairsFast(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def is_palindrome(check):
            return check == check[::-1]
        words = {word: i for i, word in enumerate(words)}
        valid_pals = []
        for word, k in words.iteritems():
            n = len(word)
            for j in range(n+1):
                pref = word[:j]
                suf = word[j:]
                if is_palindrome(pref):
                    back = suf[::-1]
                    #if back != word and back in words:
                    if back in words and words[back] != k: # slightly faster
                        valid_pals.append([words[back],  k])
                if j != n and is_palindrome(suf):
                    back = pref[::-1]
                    #if back != word and back in words:
                    if back in words and words[back] != k: # slightly faster
                        valid_pals.append([k, words[back]])
        return valid_pals
    

if __name__ == "__main__":
    print(Solution().palindromePairs(["abcd","dcba","lls","s","sssll"]))