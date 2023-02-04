'''
-Hard-
*DP*
*Greedy*
*Sorting*

Given an array of digits digits, return the largest multiple of three 
that can be formed by concatenating some of the given digits in any 
order. If there is no answer return an empty string.

Since the answer may not fit in an integer data type, return the 
answer as a string. Note that the returning answer must not contain 
unnecessary leading zeros.

 

Example 1:

Input: digits = [8,1,9]
Output: "981"
Example 2:

Input: digits = [8,6,7,1,0]
Output: "8760"
Example 3:

Input: digits = [1]
Output: ""
 

Constraints:

1 <= digits.length <= 10^4
0 <= digits[i] <= 9


'''
from typing import Counter, List
import collections
class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        A = digits
        A.sort() # use quick sort
        remain1Indices, remain2Indices  = [], []
        for i,d in enumerate(A):
            if d % 3 == 1 and len(remain1Indices) < 2:
                remain1Indices.append(i)
            if d % 3 == 2 and len(remain2Indices) < 2:
                remain2Indices.append(i)
        remainSum = sum(A) % 3
        def getResult(ban1, ban2):
            sb = []
            for i in range(len(A) - 1, -1, -1):
                if i == ban1 or i == ban2: continue # Skip banned digits
                sb.append(str(A[i]))
            if len(sb) > 0 and sb[0] == '0': return "0" # Remove leading 0 case [0,...,0]
            return ''.join(sb)
        if remainSum == 1:  # Delete 1 smallest digit with remainder = 1 or Delete 2 smallest digits the remainder = 2
            if len(remain1Indices) >= 1: 
                return getResult(remain1Indices[0], -1)
            else: 
                return getResult(remain2Indices[0], remain2Indices[1])
        elif remainSum == 2: # Delete 1 smallest digit with remainder = 2 or Delete 2 smallest digits with remainder = 1
            if len(remain2Indices) >= 1: 
                return getResult(remain2Indices[0], -1)
            else: 
                return getResult(remain1Indices[0], remain1Indices[1])
        return getResult(-1, -1)
    
    def largestMultipleOfThree2(self, digits: List[int]) -> str:
        count = collections.Counter(digits)
        A = [] 
        # use count sort
        for c in sorted(count.keys()):
            A += [c]*count[c]
        remain1Indices, remain2Indices  = [], []
        for i,d in enumerate(A):
            if d % 3 == 1 and len(remain1Indices) < 2:
                remain1Indices.append(i)
            if d % 3 == 2 and len(remain2Indices) < 2:
                remain2Indices.append(i)
        remainSum = sum(A) % 3
        def getResult(ban1, ban2):
            sb = []
            for i in range(len(A) - 1, -1, -1):
                if i == ban1 or i == ban2: continue # Skip banned digits
                sb.append(str(A[i]))
            if len(sb) > 0 and sb[0] == '0': return "0" # Remove leading 0 case [0,...,0]
            return ''.join(sb)
        if remainSum == 1:  # Delete 1 smallest digit with remainder = 1 or Delete 2 smallest digits the remainder = 2
            if len(remain1Indices) >= 1: 
                return getResult(remain1Indices[0], -1)
            else: 
                return getResult(remain2Indices[0], remain2Indices[1])
        elif remainSum == 2: # Delete 1 smallest digit with remainder = 2 or Delete 2 smallest digits with remainder = 1
            if len(remain2Indices) >= 1: 
                return getResult(remain2Indices[0], -1)
            else: 
                return getResult(remain1Indices[0], remain1Indices[1])
        return getResult(-1, -1)
    
    def largestMultipleOfThree3(self, digits: List[int]) -> str:
        # DP solution
        # dp[i]: i = 0, 1, 2 the maximum that has remainder of i 
        dp = [-1,-1,-1]
        for a in sorted(digits)[::-1]:
            for x in dp[:] + [0]:
                y = x * 10 + a
                dp[y % 3] = max(dp[y % 3], y)
        return str(dp[0]) if dp[0] >= 0 else ""

        


if __name__ == "__main__":
    print(Solution().largestMultipleOfThree([8,6,7,1,0]))
    print(Solution().largestMultipleOfThree2([8,6,7,1,0]))