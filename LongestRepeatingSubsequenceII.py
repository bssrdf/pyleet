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


if __name__ == "__main__":
    print(Solution().longestRepeatingSubsequenceII(str = "aabcbcbcbc", k = 2))