'''

-Hard-

Given a list of words, list of  single letters (might be repeating) and score of every character.

Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).

It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.

 

Example 1:

Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
Output: 23
Explanation:
Score  a=1, c=9, d=5, g=3, o=2
Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
Words "dad" and "dog" only get a score of 21.
Example 2:

Input: words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
Output: 27
Explanation:
Score  a=4, b=4, c=4, x=5, z=10
Given letters, we can form the words "ax" (4+5), "bx" (4+5) and "cx" (4+5) with a score of 27.
Word "xxxz" only get a score of 25.
Example 3:

Input: words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
Output: 0
Explanation:
Letter "e" can only be used once.
 

Constraints:

1 <= words.length <= 14
1 <= words[i].length <= 15
1 <= letters.length <= 100
letters[i].length == 1
score.length == 26
0 <= score[i] <= 10
words[i], letters[i] contains only lower case English letters.

'''
from typing import List
from collections import Counter
from functools import lru_cache


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        n = len(words)
        count = Counter(letters)
        ans = [0]
        def scores(c):
            return score[ord(c)-ord('a')] 
        @lru_cache(None)
        def backtrack(cur_score, mask):
            ans[0] = max(ans[0], cur_score)
            for i in range(n):
                if mask & (1 << i) == 0: 
                    can_form, stop, s = True, 0, 0
                    for j,c in enumerate(words[i]):
                        if count[c] <= 0:
                            can_form = False
                            stop = j
                            break
                        count[c] -= 1                        
                        s += scores(c)
                    if can_form:
                        mask |= 1 << i
                        backtrack(cur_score+s, mask)
                        # backtracking
                        mask &= ~(1 << i)
                        for c in words[i]:
                            count[c] += 1
                    else: # backtracking
                        for j in range(stop):
                            count[words[i][j]] += 1
        backtrack(0, 0)         
        return ans[0]   

    def maxScoreWords2(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # gives wrong answer
        n = len(words)
        def scores(c):
            return score[ord(c)-ord('a')] 
        def word_score(word):
            s = 0
            for c in word:
                s += scores(c)
            return s
        words.sort(key=word_score, reverse=True)
        count = Counter(letters)
        ans = [0]
        
        @lru_cache(None)
        def backtrack(cur, cur_score, mask):
            if cur == n: return
            ans[0] = max(ans[0], cur_score)
            for i in range(cur, n):
                if mask & (1 << i) == 0: 
                    can_form, stop, s = True, 0, 0
                    for j,c in enumerate(words[i]):
                        if count[c] <= 0:
                            can_form = False
                            stop = j
                            break
                        count[c] -= 1                        
                        s += scores(c)
                    if can_form:
                        mask |= 1 << i
                        backtrack(i+1, cur_score+s, mask)
                        # backtracking
                        mask &= ~(1 << i)
                        for c in words[i]:
                            count[c] += 1
                    else: # backtracking
                        for j in range(stop):
                            count[words[i][j]] += 1
        backtrack(0, 0, 0)         
        return ans[0]   

if __name__ == "__main__":
    words = ["dog","cat","dad","good"]
    letters = ["a","a","c","d","d","d","g","o","o"]
    score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
    print(Solution().maxScoreWords(words, letters, score)) 
    print(Solution().maxScoreWords2(words, letters, score)) 
    words = ["xxxz","ax","bx","cx"]
    letters = ["z","a","b","c","x","x","x"]
    score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
    print(Solution().maxScoreWords(words, letters, score)) 
    print(Solution().maxScoreWords2(words, letters, score)) 
    words = ["leetcode"]
    letters = ["l","e","t","c","o","d"]
    score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
    print(Solution().maxScoreWords(words, letters, score)) 
    print(Solution().maxScoreWords2(words, letters, score)) 