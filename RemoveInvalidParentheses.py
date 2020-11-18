'''
-Hard-
*BFS*

Remove the minimum number of invalid parentheses in order to make the input string 
valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]

'''

from collections import deque

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        dq = deque()
        visited = set()        
        def isValid(st):
            cnt = 0     
            for c in st:
                if c == '(':   cnt += 1                
                elif c == ')': cnt -= 1
                if cnt < 0: return False                    
            return cnt == 0
        visited.add(s)
        dq.append(s)        
        found = False
        while dq:
            cur = dq.popleft()
            if isValid(cur):   
                res.append(cur)
                found = True
            # if a valid one already is found, there is no need to try
            # next level with one more paranthese removed: skip    
            # the current level ones can still proceed
            if found: continue    
            for i,c in enumerate(cur):
                if c in '()':
                    nxt = cur[:i]+cur[i+1:]
                    if nxt not in visited:
                        visited.add(nxt)
                        dq.append(nxt)
        if len(res) == 0: return [""]
        return res



if __name__ == "__main__":
    print(Solution().removeInvalidParentheses("()())()"))
    print(Solution().removeInvalidParentheses("(a)())()"))
    print(Solution().removeInvalidParentheses(")("))

