'''

-Medium-
$$$


Given an array of keywords words and a string s, make all appearances of all keywords words[i] in s bold. Any letters between <b> and </b> tags become bold.

Return s after adding the bold tags. The returned string should use the least number of tags possible, and the tags should form a valid combination.

 

Example 1:

Input: words = ["ab","bc"], s = "aabcd"
Output: "a<b>abc</b>d"
Explanation: Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.
Example 2:

Input: words = ["ab","cb"], s = "aabcd"
Output: "a<b>ab</b>cd"
 

Constraints:

1 <= s.length <= 500
0 <= words.length <= 50
1 <= words[i].length <= 10
s and words[i] consist of lowercase English letters.


'''

from typing import List

class Solution(object):

    def boldWords(self, words: List[str], s: str) -> str:
        n = len(s)
        res = ''
        bold = set()
        '''
        the idea is a brute force string matching 
        '''
        for word in words:
            wl = len(word)
            for i in range(n-wl+1):
                if s[i] == word[0] and s[i:i+wl] == word:
                    for j in range(i, i+wl): bold.add(j)        
        for i in range(n):
            if i in bold and i-1 not in bold: res += '<b>'
            res += s[i]
            if i in bold and i+1 not in bold: res += '</b>'
        return res


if __name__ == "__main__": 
    print(Solution().boldWords(words = ["ab","bc"], s = "aabcd"))
    print(Solution().boldWords(words = ["ab","cb"], s = "aabcd"))