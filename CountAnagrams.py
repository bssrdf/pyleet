'''

-Hard-

You are given a string s containing one or more words. Every consecutive pair of words is separated by a single space ' '.

A string t is an anagram of string s if the ith word of t is a permutation of the ith word of s.

For example, "acb dfe" is an anagram of "abc def", but "def cab" and "adc bef" are not.
Return the number of distinct anagrams of s. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: s = "too hot"
Output: 18
Explanation: Some of the anagrams of the given string are "too hot", "oot hot", "oto toh", "too toh", and "too oht".
Example 2:

Input: s = "aa"
Output: 1
Explanation: There is only one anagram possible for the given string.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters and spaces ' '.
There is single space between consecutive words.



'''
from collections import Counter
from math import factorial
class Solution:
    def countAnagrams(self, s: str) -> int:
        mod = 10**9 + 7
        def count(word):
            cnt = Counter(word)
            x = factorial(len(word))
            for c in cnt:
                x //= factorial(cnt[c])
            return x   
        words = s.split()
        ans = 1
        for word in words:
            ans = ans * count(word) % mod
        return ans   
    
    def countAnagrams2(self, s: str) -> int:
        mod = 10**9 + 7
        table = {}
 
        def count(word):
            cnt = Counter(word)
            if len(word) in table:                
               x = table[len(word)]
            else:
                x = factorial(len(word))
                table[len(word)] = x
            for c in cnt:
                if cnt[c] in table:
                    x //= table[cnt[c]]
                else:
                    d = factorial(cnt[c])
                    x //= d
                    table[cnt[c]] = d
            return x   
        words = s.split()
        ans = 1
        for word in words:
            ans = ans * count(word) % mod
        return ans   




if __name__ == "__main__":
    print(Solution().countAnagrams(s = "too hot"))
    print(Solution().countAnagrams(s = "aa"))