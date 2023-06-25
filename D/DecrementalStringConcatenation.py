'''

-Medium-

You are given a 0-indexed array words containing n strings.

Let's define a join operation join(x, y) between two strings x and y as concatenating them into xy. However, if the last character of x is equal to the first character of y, one of them is deleted.

For example join("ab", "ba") = "aba" and join("ab", "cde") = "abcde".

You are to perform n - 1 join operations. Let str0 = words[0]. Starting from i = 1 up to i = n - 1, for the ith operation, you can do one of the following:

Make stri = join(stri - 1, words[i])
Make stri = join(words[i], stri - 1)
Your task is to minimize the length of strn - 1.

Return an integer denoting the minimum possible length of strn - 1.

 

Example 1:

Input: words = ["aa","ab","bc"]
Output: 4
Explanation: In this example, we can perform join operations in the following order to minimize the length of str2: 
str0 = "aa"
str1 = join(str0, "ab") = "aab"
str2 = join(str1, "bc") = "aabc" 
It can be shown that the minimum possible length of str2 is 4.
Example 2:

Input: words = ["ab","b"]
Output: 2
Explanation: In this example, str0 = "ab", there are two ways to get str1: 
join(str0, "b") = "ab" or join("b", str0) = "bab". 
The first string, "ab", has the minimum length. Hence, the answer is 2.
Example 3:

Input: words = ["aaa","c","aba"]
Output: 6
Explanation: In this example, we can perform join operations in the following order to minimize the length of str2: 
str0 = "aaa"
str1 = join(str0, "c") = "aaac"
str2 = join("aba", str1) = "abaaac"
It can be shown that the minimum possible length of str2 is 6.
 
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 50
Each character in words[i] is an English lowercase letter



'''

from typing import List
from collections import deque
from math import inf
from functools import lru_cache
import heapq

class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        # TLE or MLE
        n = len(words)
        ans = inf
        @lru_cache(None)
        def dfs(i, s):
            nonlocal ans
            if i == n:                
                ans = min(ans, len(s)) 
                # print(ans, len(s), s)
                return 
            # print(s, words[i])
            if s[-1] == words[i][0]:
                dfs(i+1, s[:-1]+words[i])
            else:
                dfs(i+1, s+words[i])    
            if words[i][-1] == s[0]:   
                dfs(i+1, words[i][:-1]+s)
            else:                
                dfs(i+1, words[i]+s)
        dfs(1, words[0])
        return ans
    
    def minimizeConcatenatedLength2(self, words: List[str]) -> int:
        #TLE
        n = len(words)
        pq = [(len(words[0]), words[0], 1)]
        while pq:
            l, s, i = heapq.heappop(pq)
            # print(l, s, i)
            if i == n: 
                # print(s)
                return l
            if s[-1] == words[i][0]:
                heapq.heappush(pq, (l+len(words[i])-1, s[:-1]+words[i], i+1))
            else:
                heapq.heappush(pq, (l+len(words[i]), s+words[i], i+1))
            if s[0] == words[i][-1]:
                heapq.heappush(pq, (l+len(words[i])-1, words[i][:-1]+s, i+1))
            else:
                heapq.heappush(pq, (l+len(words[i]), words[i]+s, i+1))
        return inf
    
    def minimizeConcatenatedLength3(self, words: List[str]) -> int:
        n = len(words)
        @lru_cache(None)
        def dfs(i, first, last):
            if i == n:                
                return 0
            ret = inf
            if last == words[i][0]:
                ret = min(ret, len(words[i])-1+dfs(i+1, first, words[i][-1]))
            else:
                ret = min(ret, len(words[i])+dfs(i+1, first, words[i][-1]))
            if first == words[i][-1]:
                ret = min(ret, len(words[i])-1+dfs(i+1, words[i][0], last))
            else:
                ret = min(ret, len(words[i])+dfs(i+1, words[i][0], last))
            return ret
        return len(words[0]) + dfs(1, words[0][0], words[0][-1])







                               




        

if __name__ == "__main__":
    # print(Solution().minimizeConcatenatedLength(words = ["aa","ab","bc"]))
    # print(Solution().minimizeConcatenatedLength(words = ["ab","b"]))
    # print(Solution().minimizeConcatenatedLength(words = ["aaa","c","aba"]))
    print(Solution().minimizeConcatenatedLength(words = ["a","cba", "a"]))
    print(Solution().minimizeConcatenatedLength3(words = ["a","cba", "a"]))

    print(Solution().minimizeConcatenatedLength(words = ["ab","cc","bc","b"]))
    print(Solution().minimizeConcatenatedLength2(words = ["ab","cc","bc","b"]))
    print(Solution().minimizeConcatenatedLength3(words = ["ab","cc","bc","b"]))
    words = ["bhb","hded","d","b","ahbji","jgg","eegj","gi","g","ja","hihca","cdej","igahd","c","jdj","gia","fg","aaic","g"]
    # print(Solution().minimizeConcatenatedLength(words = words))
    print(Solution().minimizeConcatenatedLength3(words = words))
    words = ["chhef","hhd","bh","ghg","aade","ceeh","d","cgg","eabb","fhgd","aia","ifce","d","jjjhb","dgdcc","jdbd","i","ac","jjehc","hgec","jgj"]
    # print(Solution().minimizeConcatenatedLength2(words = words))
    print(Solution().minimizeConcatenatedLength3(words = words))
    