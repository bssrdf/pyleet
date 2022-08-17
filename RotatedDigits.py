'''
-Medium-

An integer x is a good if after rotating each digit individually by 180 degrees, we get a valid number that is different from x. Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. For example:

0, 1, and 8 rotate to themselves,
2 and 5 rotate to each other (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),
6 and 9 rotate to each other, and
the rest of the numbers do not rotate to any other number and become invalid.
Given an integer n, return the number of good integers in the range [1, n].

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
Example 2:

Input: n = 1
Output: 0
Example 3:

Input: n = 2
Output: 1
 

Constraints:

1 <= n <= 104



'''

import functools

class Solution:
    def rotatedDigits(self, n: int) -> int:
        N = list(map(int, str(N)))
        rotatings = {2, 5, 6, 9}
        nonrotatings = {0, 1, 8}

        @functools.lru_cache(None)
        def dp(pos, isPrefix, isBigger, hasRotating):
            if pos == len(N): return 0
            result = 0
            for i in range(0 if pos > 0 else 1, 10):
                if i not in rotatings and i not in nonrotatings:
                    continue
                _isPrefix = isPrefix and i == N[pos]
                _isBigger = isBigger or (isPrefix and i > N[pos])

                _hasRotating = hasRotating or i in rotatings
                if _hasRotating and not (pos == len(N) - 1 and _isBigger):
                    result += 1
                result += dp(pos + 1, _isPrefix, _isBigger, _hasRotating)
            return result
        return dp(0, True, False, False)
        


