'''

-Medium-

*DP*
*Combinatorics*

Given a string word, return the sum of the number of vowels ('a', 'e', 'i', 'o', and 'u') in every substring of word.

A substring is a contiguous (non-empty) sequence of characters within a string.

Note: Due to the large constraints, the answer may not fit in a signed 32-bit integer. Please be careful during the calculations.

 

Example 1:

Input: word = "aba"
Output: 6
Explanation: 
All possible substrings are: "a", "ab", "aba", "b", "ba", and "a".
- "b" has 0 vowels in it
- "a", "ab", "ba", and "a" have 1 vowel each
- "aba" has 2 vowels in it
Hence, the total sum of vowels = 0 + 1 + 1 + 1 + 1 + 2 = 6. 
Example 2:

Input: word = "abc"
Output: 3
Explanation: 
All possible substrings are: "a", "ab", "abc", "b", "bc", and "c".
- "a", "ab", and "abc" have 1 vowel each
- "b", "bc", and "c" have 0 vowels each
Hence, the total sum of vowels = 1 + 1 + 1 + 0 + 0 + 0 = 3.
Example 3:

Input: word = "ltcd"
Output: 0
Explanation: There are no vowels in any substring of "ltcd".
 

Constraints:

1 <= word.length <= 105
word consists of lowercase English letters.

'''

class Solution:
    def countVowels(self, word: str) -> int:
        # For each vowels s[i],
        # it could be in the substring starting at s[x] and ending at s[y],
        # where 0 <= x <= i and i <= y < n,
        # that is (i + 1) choices for x and (n - i) choices for y.

        # So there are (i + 1) * (n - i) substrings containing s[i].

        n = len(word)
        return sum((i + 1) * (n - i) for i, c in enumerate(word) if c in 'aeiou')
    
    def countVowels2(self, word: str) -> int:
        dp = [0] * len(word)  # dp[i] is number of vowels from substrings _ending_ at i
        dp[0] = 1 if word[0] in "aeiou" else 0
        for i in range(1,len(word)):
            if word[i] in "aeiou":
                dp[i] = dp[i-1] + (i+1)
            else:
                dp[i] = dp[i-1]
            # print(i, word[i], dp)
        return sum(dp)
    
    def countVowels3(self, word: str) -> int:
        cnt = 1 if word[0] in "aeiou" else 0
        ans = cnt
        for i in range(1,len(word)):
            if word[i] in "aeiou":
                cnt += i+1
            ans += cnt
        return ans
        
    
if __name__ == "__main__":
    print(Solution().countVowels('aba'))
    print(Solution().countVowels('eaaba'))
    print(Solution().countVowels("noosabasboosa"))
    print(Solution().countVowels2('aba'))
    print(Solution().countVowels2('eaaba'))
    print(Solution().countVowels2("noosabasboosa"))