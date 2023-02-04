'''
-Medium-

We define the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", 
so s will look like this:

"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
Given a string p, return the number of unique non-empty substrings of p are present in s.

 

Example 1:

Input: p = "a"
Output: 1
Explanation: Only the substring "a" of p is in s.
Example 2:

Input: p = "cac"
Output: 2
Explanation: There are two substrings ("a", "c") of p in s.
Example 3:

Input: p = "zab"
Output: 6
Explanation: There are six substrings ("z", "a", "b", "za", "ab", and "zab") of p in s.
 

Constraints:

1 <= p.length <= 10^5
p consists of lowercase English letters.


'''

class Solution:
    def findSubstringInWraproundStringTLE(self, p: str) -> int:
        dp = [0]*len(p)
        dp[0] = 0
        res = {p[0]}
        for i in range(1, len(p)):
            if (ord(p[i])+26-ord(p[i-1]))%26 == 1:
                dp[i] = dp[i-1]
                res.add(p[i])
                for j in range(dp[i], i):
                    res.add(p[j:i+1])
                #res += 1 + (i-dp[i])
            else:
                #res += 1
                res.add(p[i])
                dp[i] = i
        return len(res)

    def findSubstringInWraproundString(self, p: str) -> int:
        dp = [0]*26
        curMaxLen = 0
        for i in range(len(p)):
            if i > 0 and (ord(p[i])+26-ord(p[i-1]))%26 == 1:
                curMaxLen += 1
            else:
                curMaxLen = 1
            idx = ord(p[i])-ord('a')
            # To avoid duplicate substring, for each letter "a,b,c,d..." we only try to find the 
            # longest substring which end with them, and record in dp[].
            dp[idx] = max(dp[idx], curMaxLen)
        return sum(dp)







        

if __name__ == "__main__":
    print(Solution().findSubstringInWraproundString("zab"))
    print(Solution().findSubstringInWraproundString("cac"))