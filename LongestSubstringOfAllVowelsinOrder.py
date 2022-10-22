'''

-Medium-

A string is considered beautiful if it satisfies the following conditions:

Each of the 5 English vowels ('a', 'e', 'i', 'o', 'u') must appear at least once in it.
The letters must be sorted in alphabetical order (i.e. all 'a's before 'e's, all 'e's before 'i's, etc.).
For example, strings "aeiou" and "aaaaaaeiiiioou" are considered beautiful, but "uaeio", "aeoiu", and "aaaeeeooo" are not beautiful.

Given a string word consisting of English vowels, return the length of the longest beautiful substring of word. If no such substring exists, return 0.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
Output: 13
Explanation: The longest beautiful substring in word is "aaaaeiiiiouuu" of length 13.
Example 2:

Input: word = "aeeeiiiioooauuuaeiou"
Output: 5
Explanation: The longest beautiful substring in word is "aeiou" of length 5.
Example 3:

Input: word = "a"
Output: 0
Explanation: There is no beautiful substring, so return 0.
 

Constraints:

1 <= word.length <= 5 * 105
word consists of characters 'a', 'e', 'i', 'o', and 'u'.


'''

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        needed = {'a':'e', 'e':'i', 'i':'o', 'o':'u'}
        S = word
        n, ans, r = len(word), 0, 0
        while r < n:            
            while r < n and S[r] != 'a':
                r += 1
            l, c = r, 'a'
            while r < n:
                if S[r] == c:
                    r += 1
                elif c != 'u' and S[r] == needed[c]:
                    c = needed[c]
                    r += 1
                else:
                    break
            if c == 'u':
                ans = max(ans, r-l)      
        return ans


        

if __name__ == "__main__":
    print(Solution().longestBeautifulSubstring(word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"))
    print(Solution().longestBeautifulSubstring(word = "aeeeiiiioooauuuaeiou"))
    print(Solution().longestBeautifulSubstring(word = "a"))