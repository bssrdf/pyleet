'''
-Hard-

*DP*

You are given a string s containing lowercase letters and an integer k. You need to :

First, change some characters of s to other lowercase English letters.
Then divide s into k non-empty disjoint substrings such that each substring is a palindrome.
Return the minimal number of characters that you need to change to divide the string.

 

Example 1:

Input: s = "abc", k = 2
Output: 1
Explanation: You can split the string into "ab" and "c", and change 1 character in "ab" to make it palindrome.
Example 2:

Input: s = "aabbc", k = 3
Output: 0
Explanation: You can split the string into "aa", "bb" and "c", all of them are palindrome.
Example 3:

Input: s = "leetcode", k = 8
Output: 0
 

Constraints:

1 <= k <= s.length <= 100.
s only contains lowercase English letters.
'''


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        memo = {}
        
        def cost(s,i,j): #calculate the cost of transferring one substring into palindrome string
            r = 0
            while i < j:
                if s[i] != s[j]:
                    r += 1
                i += 1
                j -= 1
            return r
        
        def dfs(i, k):
            if (i, k) in memo: return memo[(i, k)] #case already in memo
            if n - i == k: #base case that each substring just have one character
                return 0
            if k == 1:    #base case that need to transfer whole substring into palidrome
                return cost(s, i, n - 1)
            res = float('inf')
            for j in range(i + 1, n - k + 2): # keep making next part of substring into palidrome
                res = min(res, dfs(j, k - 1) + cost(s,i, j - 1)) #compare different divisions to get the minimum cost
            memo[(i, k)] = res
            return res
        return dfs(0 , k)
    

    def palindromePartition2(self, s: str, k: int) -> int:
        n = len(s)
        memo = {}
        c = [[0]*n for _ in range(n)]
        def cost(s,i,j): #calculate the cost of transferring one substring into palindrome string
            r = 0
            while i < j:
                if s[i] != s[j]:
                    r += 1
                i += 1
                j -= 1
            return r

        for i in range(n):
            for j in range(n):
                c[i][j] = cost(s, i, j)

        
        def dfs(i, k):
            if (i, k) in memo: return memo[(i, k)] #case already in memo
            if n - i == k: #base case that each substring just have one character
                return 0
            if k == 1:    #base case that need to transfer whole substring into palidrome
                return c[i][n - 1]
            res = float('inf')
            for j in range(i + 1, n - k + 2): # keep making next part of substring into palidrome
                res = min(res, dfs(j, k - 1) + c[i][j - 1]) #compare different divisions to get the minimum cost
            memo[(i, k)] = res
            return res
        return dfs(0, k)


if __name__ == "__main__":
    print(Solution().palindromePartition(s = "abc", k = 2))
    print(Solution().palindromePartition2(s = "abc", k = 2))