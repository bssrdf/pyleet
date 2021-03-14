''''
-Hard-

Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a 
subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "". 
If there are multiple such minimum-length windows, return the one with the smallest 
starting index.

All the strings in the input will only contain lowercase letters.
The length of S will be in the range [1, 20000].
The length of T will be in the range [1, 100].

Example 1:

Input：S="jmeqksfrsdcmsiwvaovztaqenprpvnbstl"，T="u"
Output：""
Explanation： unable to match
Example 2:

Input：S = "abcdebdde"， T = "bde"
Output："bcde"
Explanation："bcde" is the answer and "deb" is not a smaller window because the 
elements of T in the window must occur in order.


'''
from collections import defaultdict
import sys

class Solution:
    """
    @param S: a string
    @param T: a string
    @return: the minimum substring of S
    """
    def minWindow(self, S, T):
        m, n, start, minLen = len(S), len(T), -1, sys.maxsize
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1): dp[i][0] = i
        for i in range(1, m+1):
            for j in range(1, min(i+1, n+1)):
                dp[i][j] = dp[i - 1][j - 1] if S[i - 1] == T[j - 1] else dp[i - 1][j]
            if dp[i][n] != -1:
                lth = i - dp[i][n]
                if minLen > lth:
                    minLen = lth
                    start = dp[i][n]
        return S[start:start+minLen] if start != -1 else ""

if __name__ == "__main__":
    #print(Solution().minWindow(S="abcdebdde", T="bde"))
    S = "spbmtkwqpftyahhnughzxscpavtqymtbanjyybdlhbphfrycpytsgzoeunvxaxuwbmecthomrjgmbvaoyjxxefmtxaxgwswdjdjlkpzsuirbujvhesfzdklgkulkmfnlofytaszwtxacnffvszmobxwmlhaxporskwzrvgmdpneggxqidqsdgvcprcnkdrxtsktibilbtggpazwuddhrgsmaspelglhausmfnyksdfyrwtpftrgtw"
    T = "asgvamuyus"
    print(Solution().minWindow(S, T))
    