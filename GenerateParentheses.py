'''
-Medium-

Given n pairs of parentheses, write a function to generate all combinations 
of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8

'''

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def dfs(s, left, right):
            if left > right: return
            if len(s) == 2*n:
                ans.append(s[:])
            if left > 0:
                dfs(s+'(', left-1, right)
            if right > 0:
                dfs(s+')', left, right-1)
        dfs('', n, n)
        return ans


if __name__ == "__main__":
    print(Solution().generateParenthesis(3))