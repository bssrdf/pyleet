'''
-Hard-

*DP*


Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

 

Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we don't need any insertions.
Example 2:

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
Example 3:

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".
Example 4:

Input: s = "g"
Output: 0
Example 5:

Input: s = "no"
Output: 1
 

Constraints:

1 <= s.length <= 500
All characters of s are lower case English letters.

'''

class Solution(object):
    def minInsertionsMemo(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        Let's imagine matching the characters of the string like a palindrome, from the begining and the end with 2 pointers i and j.
        We may encounter 2 scenarios:

        The character at i matches character at j.
        The characters don't match each other
        In case of 1 we just increase the pointer i and decrease the pointer j, i++ and j-- 
        respectively.

        In the second case we have 2 options:

        Insert one character at j to match the character at i.

        Or

        Insert one character at i to match the character at j.

        Since we are not actually adding the characters in the string but just calculating 
        the cost,
        In case 1 we increase the pointer i by 1 and j stays as it is, as we still need a 
        character to match at j

        and in case 2 we decrease the pointer j by 1 and i stays as it is, as we still need 
        a character to match at i.

        both the cases adds cost 1 since we are inserting a letter.

        We can then use these two different pairs of new i and j values (i+1, j and i, j-1) to 
        again repeat the process and use the minimum result of these as our result for current 
        pair of i, j.
        We can see that this is recursive and thus we can use recursion with caching to store the repeated values.
        """
        n = len(s)
        def dp(i,j):
            if i>=j: return 0
            if memo[i][j] != -1: return memo[i][j]
            memo[i][j] = dp(i+1,j-1) if s[i] == s[j] else \
                         1+min(dp(i,j-1), dp(i+1,j))
            return memo[i][j]
        memo = [[-1 for _ in range(n)] for _ in range(n)] 
        return dp(0, len(s)-1)

    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0]*n
        for i in range(n-2, -1, -1):
            prev = 0 #                         //This stores the value at memo[i+1][j-1];
            for j in range(i, n):
                temp = dp[j] #                 //Get the value of memo[i+1][j].
                #  memo[j]=memo[i+1][j], memo[j-1]=memo[i][j-1], prev=memo[i+1][j-1].
                dp[j] = prev if s[i]==s[j] else 1+min(dp[j],dp[j-1])
                # Store the value of memo[i+1][j] to use it as memo[i+1][j-1] in the next iteration.
                prev = temp        
        return dp[n-1]


if __name__ == "__main__":
    print(Solution().minInsertionsMemo("mbadm"))
    print(Solution().minInsertions("mbadm"))
    print(Solution().minInsertions("leetcode"))