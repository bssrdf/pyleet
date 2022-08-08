'''

-Medium-

You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

 

Example 1:

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.
Example 2:

Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.
Example 3:

Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".
 

Constraints:

1 <= words.length <= 105
words[i].length == 2
words[i] consists of lowercase English letters.


'''

from typing import List
from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = Counter(words)
        a, b, used = 0, 0, False
        for word, cnt in counter.items():
            if word[0] == word[1]:
                if cnt % 2 == 1:
                    if not used:
                        a += cnt * 2
                        used = True
                    else:
                        a += (cnt-1) * 2
                else:
                    a += cnt * 2
            else:                
                b += 2 * min(cnt, counter[word[::-1]])  
        return a + b

                
                



        

if __name__ == "__main__":
    print(Solution().longestPalindrome(words = ["lc","cl","gg"]))
    print(Solution().longestPalindrome(words = ["ab","ty","yt","lc","cl","ab"]))
    print(Solution().longestPalindrome(words = ["cc","ll","xx"]))
    words = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]
    print(Solution().longestPalindrome(words = words))