'''
-Medium-

Given a string S, return the number of substrings of length K with no repeated 
characters.

 

Example 1:

Input: S = "havefunonleetcode", K = 5
Output: 6
Explanation: 
There are 6 substrings they are : 'havef','avefu','vefun','efuno','etcod','tcode'.
Example 2:

Input: S = "home", K = 5
Output: 0
Explanation: 
Notice K can be larger than the length of S. In this case is not possible to find 
any substring.
 

Note:

1 <= S.length <= 10^4
All characters of S are lowercase English letters.
1 <= K <= 10^4

'''
from collections import defaultdict

class Solution(object):

    def numKLenSubstrNoRepeats(self, S,  K):
        n = len(S)
        left, right = 0, 0
        ans = 0
        m = defaultdict(int)
        while right < n:
            c = S[right]
            m[c] += 1
            right += 1
            while left < right and (m[c] > 1 or right-left > K):
                d = S[left]
                left += 1
                m[d] -= 1
                if m[d] == 0:
                    m.pop(d)
            if right-left == K:
                print(S[left:right])
                ans += 1
        return ans 

if __name__ == "__main__":
    print(Solution().numKLenSubstrNoRepeats("havefunonleetcode", 5))
    print(Solution().numKLenSubstrNoRepeats("haeevefunoenlecetcacoade", 5))
    print(Solution().numKLenSubstrNoRepeats("home", 5))


