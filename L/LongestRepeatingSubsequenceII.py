'''

-Medium-

Given a string str, find the longest substring with no fewer than k repetitions 
and return the length. The substring can have overlapping parts, but cannot 
completely overlap.

1 <= str.length <= 1000
1 < k < str.length
We guarantee that the problem will certainly can be solved
样例
Example 1:

Input: str = "aaa", k = 2, 
Output: 2.
Explanation:
The longest subsequence with no fewer than k repetitions is "aa", and the length is 2.
Example 2:

Input: str = "aabcbcbcbc", k = 2, 
Output: 6.
Explanation:
Subsequences repeat no fewer than twice are "a", "bc", "bcbc" and "bcbcbc", and the longest is "bcbcbc", and the length is 6.


'''

class SuffixArray:
    """ by Karp, Miller, Rosenberg 1972

        s is the string to analyze.

        P[k][i] is the pseudo rank of s[i:i+K] for K = 1<<k
        among all strings of length K. Pseudo, because the pseudo rank numbers are
        in order but not necessarily consecutive.
    
        Initialization of the data structure has complexity O(n log^2 n).
    """
    def __init__(self, s):
        self.n = len(s)
        if self.n == 1:                                         # special case: single char strings
            self.P = [[0]]
            self.suf_sorted = [0]
            return
        self.P = [list(map(ord, s))]
        k = 1
        length = 1                                              # length is 2 ** (k - 1)
        while length < self.n:
            L = []                                              # prepare L
            for i in range(self.n - length):
                L.append((self.P[k - 1][i], self.P[k - 1][i + length], i))
            for i in range(self.n - length, self.n):            # pad with -1
                L.append((self.P[k - 1][i], -1, i))
            L.sort()                                            # bucket sort would be quicker
            self.P.append([0] * self.n)                         # produce k-th row in P
            for i in range(self.n):
                if i > 0 and L[i-1][:2] == L[i][:2]:            # same as previous
                    self.P[k][ L[i][2] ] = self.P[k][ L[i-1][2] ]
                else:
                    self.P[k][ L[i][2] ] = i
            k += 1
            length <<= 1                                        # or *=2 as you prefer
        self.suf_sorted = [0] * self.n                          # generate the inverse:
        for i, si in enumerate(self.P[-1]):                     # lexic. sorted suffixes
            self.suf_sorted[si] = i

    def longest_common_prefix(self, i, j):
        """returns the length of 
        the longest common prefix of s[i:] and s[j:].
        complexity: O(log n), for n = len(s).
        """
        if i == j:
            return self.n - i                       # length of suffix
        answer = 0
        length = 1 << (len(self.P) - 1)             # length is 2 ** k
        for k in range(len(self.P) - 1, -1, -1):
            length = 1 << k
            if self.P[k][i] == self.P[k][j]:        # aha, s[i:i+length] == s[j:j+length]
                answer += length
                i += length
                j += length
                if i == self.n or j == self.n:      # not needed if s is appended by $
                    break
            length >>= 1
        return answer    

    def longestRepeatingSubsequenceII(self, k):        
        res = 0
        lcp = self.longest_common_prefix(0, 1)
        print('lcp', lcp)
        for i in range(self.n-k):
            lcp = self.longest_common_prefix(i, i+k-1)
            res = max(res, lcp)
            lcp = self.longest_common_prefix(i, i+k)
            res = max(res, lcp)
        return res



class Solution:
    """
    @param str: The input string
    @param k: The repeated times
    @return: The answer
    """
    def longestRepeatingSubsequenceII(self, str, k):
        # Write your code here
        n = len(str)
        count = {}
        # enumerate every substring: 
        # each substring of str is a prefix of a suffix of str       
        for i in range(n):
            hashValue = 0
            for j in range(i, n):
                hashValue = (31 * hashValue + ord(str[j]) - ord('a')) % 1000000007
                if (hashValue, j - i + 1) in count:
                    count[(hashValue, j - i + 1)] += 1
                else:
                    count[(hashValue, j - i + 1)] = 1
        ans = 0
        for key, value in count.items():
            if value >= k:
                ans = max(ans, key[1])
        return ans
    
    def longestRepeatingSubsequenceII2(self, str, k):
        sa = SuffixArray(str)
        return sa.longestRepeatingSubsequenceII(k)



if __name__ == "__main__":
    print(Solution().longestRepeatingSubsequenceII(str = "aabcbcbcbc", k = 2))
    print(Solution().longestRepeatingSubsequenceII2(str = "aabcbcbcbc", k = 2))
    print(Solution().longestRepeatingSubsequenceII2(str = "aaa", k = 2))
    s = "ccbbcbaabcccbabcbcaaaacabbaccccacaabcbbacacaacabcbccbaabcabbbccaabbcbbcacabcaaacacabacbccbaacbcbcaacacbaaaaccacccbaacaaabacaccabcbcbabbbacbabcaaccbccacbcbacacacbcaccabaccbccbaaaaabbacbacacbccbabcaacbbcccaccbcbacbacbcabaababccaaaacccccbbaabbccbcccabbacacaacbcccbaaacacabccabcccccabcaaaabbbcbbbaabccacccabacbcbbcbabacabbbbbbabbcabcbcbcaabcbcccbabaccccabbabbbacbbacbcccaaacaccababcccbcaccbcbcaacacbccbacbccbccaccbcbcabbbccabaacaccbcccbccaccbbcbcccbbccbacbcbcbbcbabcbacbbababcbcacbaaabbabacabbcbccbaccbbc"
    print(Solution().longestRepeatingSubsequenceII2(s, 2))