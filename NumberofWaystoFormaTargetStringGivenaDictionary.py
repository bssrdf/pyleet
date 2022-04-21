'''

-Hard-


You are given a list of strings of the same length words and a string target.

Your task is to form target using the given words under the following rules:

target should be formed from left to right.
To form the ith character (0-indexed) of target, you can choose the kth character of the jth string in words if target[i] = words[j][k].
Once you use the kth character of the jth string of words, you can no longer use the xth character of any string in words where x <= k. In other words, all characters to the left of or at index k become unusuable for every string.
Repeat the process until you form the string target.
Notice that you can use multiple characters from the same string in words provided the conditions above are met.

Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: words = ["acca","bbbb","caca"], target = "aba"
Output: 6
Explanation: There are 6 ways to form target.
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")
Example 2:

Input: words = ["abba","baab"], target = "bab"
Output: 4
Explanation: There are 4 ways to form target.
"bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
"bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
"bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
"bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 1000
All strings in words have the same length.
1 <= target.length <= 1000
words[i] and target contain only lowercase English letters.


'''

from typing import List
from collections import Counter
from functools import lru_cache

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n, m = len(words[0]), len(target)
        freq = [Counter() for _ in range(n)]        
        # pos = [set() for _ in range(26)]
        MOD = 10**9+7
        for word in words:
            for i in range(n):
                freq[i][word[i]] += 1
                # pos[ord(word[i]) - ord('a')].add(i) 
        # for i in range(26):
        #    pos[i] = sorted(list(pos[i]))
        @lru_cache(None) 
        def dp(i, j):
            if i == m: return 1
            if j == n: return 0            
            ans = 0
            # l = n-m+i+1
            for k in range(j, n-m+i+1):
            # for k in pos[ord(target[i]) - ord('a')]:

                # ret = dp(i+1, k+1)    
                # if i == 0:
                #     print(k, ret, freq[k][target[i]])
                # ans += freq[k][target[i]] * ret
                # if j <= k <l and target[i] in freq[k]:
                if target[i] in freq[k]:
                    ans = (ans + freq[k][target[i]] * dp(i+1, k+1)) % MOD
            return ans
        return dp(0, 0)

    def numWays2(self, words: List[str], target: str) -> int:
        n, m = len(words[0]), len(target)
        freq = [Counter() for _ in range(n)]        
        MOD = 10**9+7
        for word in words:
            for i in range(n):
                freq[i][word[i]] += 1
        @lru_cache(None) 
        def dp(i, j):
            if i == m: return 1
            if j == n: return 0
            if n-j < m-i: return 0
            ans = dp(i, j+1)            
            if target[i] in freq[j]:
                ans = (ans + freq[j][target[i]] * dp(i+1, j+1)) % MOD
            return ans
        return dp(0, 0)


if __name__ == "__main__":   
    print(Solution().numWays(words = ["acca","bbbb","caca"], target = "aba"))
    print(Solution().numWays(words = ["abba","baab"], target = "bab"))

        