'''
-Hard-
*KMP*
*Z Algorithm*


You are building a string s of length n one character at a time, prepending each new character to the front of the string. The strings are labeled from 1 to n, where the string with length i is labeled si.

For example, for s = "abaca", s1 == "a", s2 == "ca", s3 == "aca", etc.
The score of si is the length of the longest common prefix between si and sn (Note that s == sn).

Given the final string s, return the sum of the score of every si.

 

Example 1:

Input: s = "babab"
Output: 9
Explanation:
For s1 == "b", the longest common prefix is "b" which has a score of 1.
For s2 == "ab", there is no common prefix so the score is 0.
For s3 == "bab", the longest common prefix is "bab" which has a score of 3.
For s4 == "abab", there is no common prefix so the score is 0.
For s5 == "babab", the longest common prefix is "babab" which has a score of 5.
The sum of the scores is 1 + 0 + 3 + 0 + 5 = 9, so we return 9.
Example 2:

Input: s = "azbazbzaz"
Output: 14
Explanation: 
For s2 == "az", the longest common prefix is "az" which has a score of 2.
For s6 == "azbzaz", the longest common prefix is "azb" which has a score of 3.
For s9 == "azbazbzaz", the longest common prefix is "azbazbzaz" which has a score of 9.
For all other si, the score is 0.
The sum of the scores is 2 + 3 + 9 = 14, so we return 14.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.


'''


class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)
        lps = [0]*n
        k = 0
        for q in range(1,n):
            while k > 0 and s[k] != s[q]:
                k = lps[k-1]
            if s[k] == s[q]:
                k += 1
            lps[q] = k
        print(lps)
        # we use the cnt array to count the number of times each character 
        # appears in a prefix. Summing up cnt will give us the length of all prefixes.
        cnt = []
        for j in lps:
            cnt.append(0 if j == 0 else cnt[j-1]+1)
        print(cnt)
        return sum(cnt)+len(s)
    
    def sumScores2(self, s: str) -> int:
        def zarray(s):
            n = len(s)
            z = [0]*n
            # [L,R] make a window which matches
            # with prefix of s
            left, right, k = 0, 0, 0
            for i in range(1, n):        
                # if i>R nothing matches so we will calculate.
                # Z[i] using naive way.
                if i > right:
                    left, right = i, i
        
                    # R-L = 0 in starting, so it will start
                    # checking from 0'th index.
                    while right < n and s[right - left] == s[right]:
                        right += 1
                    z[i] = right - left
                    right -= 1
                else:
                    # k = i-L so k corresponds to number which
                    # matches in [L,R] interval.
                    k = i - left
                    # if Z[k] is less than remaining interval
                    
                    if z[k] < right - i + 1:
                        z[i] = z[k]
                    else:
                        # else start from R and check manually
                        left = i
                        while right < n and s[right - left] == s[right]:
                            right += 1
                        z[i] = right - left
                        right -= 1
            return z
        return sum(zarray(s))+len(s)


if __name__ == "__main__":
    print(Solution().sumScores("babab"))
    print(Solution().sumScores("bababbababb"))
        