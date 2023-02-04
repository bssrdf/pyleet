'''
-Medium-
*Greedy*
*Backtracking*

You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.

A 0-indexed string num of length n + 1 is created using the following conditions:

num consists of the digits '1' to '9', where each digit is used at most once.
If pattern[i] == 'I', then num[i] < num[i + 1].
If pattern[i] == 'D', then num[i] > num[i + 1].
Return the lexicographically smallest possible string num that meets the conditions.

 

Example 1:

Input: pattern = "IIIDIDDD"
Output: "123549876"
Explanation:
At indices 0, 1, 2, and 4 we must have that num[i] < num[i+1].
At indices 3, 5, 6, and 7 we must have that num[i] > num[i+1].
Some possible values of num are "245639871", "135749862", and "123849765".
It can be proven that "123549876" is the smallest possible num that meets the conditions.
Note that "123414321" is not possible because the digit '1' is used more than once.
Example 2:

Input: pattern = "DDD"
Output: "4321"
Explanation:
Some possible values of num are "9876", "7321", and "8742".
It can be proven that "4321" is the smallest possible num that meets the conditions.
 

Constraints:

1 <= pattern.length <= 8
pattern consists of only the letters 'I' and 'D'.


'''

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        candi = ''.join(str(i) for i in range(1,n+2))
        res = '9'*(n+1)
        def helper(p, s, used):
            nonlocal res
            if len(s) == n+1:
                res = min(res, s)
            for i,c in enumerate(candi):
                if not used[i]:
                    used[i] = True
                    if p[0] == 'I' and c > s[-1]:                        
                          helper(p[1:], s+c, used)
                    if p[0] == 'D' and c < s[-1]:                        
                          helper(p[1:], s+c, used)
                    used[i] = False             
        used = [False]*(n+1) 
        for i,c in enumerate(candi):            
            used[i] = True
            helper(pattern, c, used)
            used[i] = False
        return res
    
    def smallestNumber2(self, s: str) -> str:
        res = []
        for i,c in enumerate(s + 'I', 1):
            if c == 'I':
                res += range(i, len(res), -1)
        return ''.join(map(str,res))
    
    def smallestNumber3(self, s):
        res, stack = [], []
        for i,c in enumerate(s + 'I', 1):
            stack.append(str(i))
            if c == 'I':
                res += stack[::-1]
                stack = []
        return ''.join(res)
