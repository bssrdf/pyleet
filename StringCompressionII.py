'''
-Hard-

Run-length encoding is a string compression method that works by replacing 
consecutive identical characters (repeated 2 or more times) with the concatenation 
of the character and the number marking the count of the characters 
(length of the run). For example, to compress the string "aabccc" we replace 
"aa" by "a2" and replace "ccc" by "c3". Thus the compressed string becomes "a2bc3".

Notice that in this problem, we are not adding '1' after single characters.

Given a string s and an integer k. You need to delete at most k characters from 
s such that the run-length encoded version of s has minimum length.

Find the minimum length of the run-length encoded version of s after deleting 
at most k characters.

 

Example 1:

Input: s = "aaabcccd", k = 2
Output: 4
Explanation: Compressing s without deleting anything will give us "a3bc3d" of length 6. Deleting any of the characters 'a' or 'c' would at most decrease the length of the compressed string to 5, for instance delete 2 'a' then we will have s = "abcccd" which compressed is abc3d. Therefore, the optimal way is to delete 'b' and 'd', then the compressed version of s will be "a3c3" of length 4.
Example 2:

Input: s = "aabbaa", k = 2
Output: 2
Explanation: If we delete both 'b' characters, the resulting compressed string would be "a4" of length 2.
Example 3:

Input: s = "aaaaaaaaaaa", k = 0
Output: 3
Explanation: Since k is zero, we cannot delete anything. The compressed string is "a11" of length 3.
 

Constraints:

1 <= s.length <= 100
0 <= k <= s.length
s contains only lowercase English letters.


'''


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        def calcLen(len):
            if len == 0: return 0
            elif len == 1: return 1
            elif len < 10: return 2
            elif len < 100: return 3
            else: return 4
        n = len(s)
        dp = [[float('inf')]*(k+1) for _ in range(n+1)]
        for i in range(k+1):
           dp[0][i] = 0 
        for i in range(1, n+1):
            for j in range(k+1):
                if j > 0: dp[i][j] = dp[i - 1][j - 1]
                removed, cnt = 0, 0
                for p in range(i, 0, -1):
                    if s[p - 1] == s[i - 1]: cnt +=1                    
                    else:
                        removed += 1
                        if removed > j: 
                           break
                    
                    dp[i][j] = min(dp[i][j], dp[p - 1][j - removed] + calcLen(cnt))
        return dp[n][k]

        

if __name__ == "__main__":
    print(Solution().getLengthOfOptimalCompression(s = "aaabcccd", k = 2))        