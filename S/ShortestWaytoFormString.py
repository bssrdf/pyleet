'''
-Medium-


From any string, we can form a subsequence of that string by deleting some number of 
characters (possibly no deletions).

Given two strings source and target, return the minimum number of subsequences 
of source such that their concatenation equals target. If the task is impossible, return -1.

 

Example 1:

Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
Example 2:

Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.
Example 3:

Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
 

Constraints:

Both the source and target strings consist of only lowercase English letters from "a"-"z".
The lengths of source and target string are between 1 and 1000.

'''

class Solution:
    def shortestWay(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        def longestSubseq(source, target, startIndex):
            i, j = 0, startIndex
            while i < n and j < m:
                if source[i] == target[j]:
                    j += 1
                i += 1
            if j == startIndex:
                return -1
            return j
        ans, i = 0, 0
        while i < m:
            i = longestSubseq(s, t, i)
            if i < 0 : return -1
            ans += 1
        return ans 
        




if __name__ == "__main__":
    print(Solution().shortestWay(s = "abc", t = "abcbc"))
    print(Solution().shortestWay(s = "abc", t = "acdbc"))
    print(Solution().shortestWay("xyz", "xzyxz"))