'''


'''
from typing import List
import collections
from itertools import accumulate
class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        A = strength
        mod = 10 ** 9 + 7
        n = len(A)
        
        # next small on the right
        right = [n] * n
        stack = []
        for i in range(n):
            while stack and A[stack[-1]] > A[i]:
                right[stack.pop()] = i
            stack.append(i)

        # next small on the left
        left = [-1] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and A[stack[-1]] >= A[i]:
                left[stack.pop()] = i
            stack.append(i)

        # for each A[i] as minimum, calculate sum
        res = 0
        acc = list(accumulate(accumulate(A), initial = 0))
        # How do we get the "sum of all subarrays including strength[i] in range (left, right)"?
        # Let's list the indices:
        # ...left-1, left, left + 1, left + 2, ... i-1, i, i+1, ... right-1, right, right+1...

        # Let prefix[i] be the prefix sum of first i elements in strength.

        # The sum of subarrays including i are:

        # the subarrays that start with left+1:
        # sum(left+1, ... i) = prefix[i + 1] - prefix[left + 1]
        # sum(left+1, ... i+1) = prefix[i + 2] - prefix[left + 1]
        # ...
        # sum(left+1, ... right-1) = prefix[right] - prefix[left + 1]
        # the subarrays that start with left+2:
        # sum(left+2, ... i) = prefix[i + 1] - prefix[left + 2]
        # sum(left+2, ... i+1) = prefix[i + 2] - prefix[left + 2]
        # ...
        # sum(left+2, ... right-1) = prefix[right] - prefix[left + 2]
        # ...

        # the subarrays that start with i:
        # sum(i, ... i) = prefix[i + 1] - prefix[i]
        # sum(i, ... i+1) = prefix[i + 2] - prefix[i]
        # ...
        # sum(i, ... right-1) = prefix[right] - prefix[i]
        # Then we combine all above terms, we have:

        # positive parts:
        # (prefix[i + 1] + prefix[i + 2] + ... + prefix[right]) * (i - left)
        # negative parts:
        # (prefix[left + 1] + prefix[left + 2] + ... + prefix[i]) * (right - i)
        # The range sum of prefix can be optimized by pre-compute prefix-sum of prefix.
        print(acc)
        for i in range(n):
            l, r = left[i], right[i]
            lacc = acc[i] - acc[max(l, 0)]
            racc = acc[r] - acc[i]
            ln, rn = i - l, r - i
            res = (res + A[i] * (racc * ln - lacc * rn)) % mod
        return res
       
       
        

print(Solution().totalStrength(strength = [1,3,1,2]))
print(Solution().totalStrength(strength = [1,3,3,2,4]))