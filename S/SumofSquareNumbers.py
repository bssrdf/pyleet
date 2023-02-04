''''
-Medium-

*Two Pointers*

Given a non-negative integer c, decide whether there're two integers a 
and b such that a2 + b2 = c.

 

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false
Example 3:

Input: c = 4
Output: true
Example 4:

Input: c = 2
Output: true
Example 5:

Input: c = 1
Output: true
 

Constraints:

0 <= c <= 2^31 - 1

'''

class Solution(object):
    def judgeSquareSumMap(self, c):
        """
        :type c: int
        :rtype: bool
        """
        m = set()
        for i in range(int(c**0.5)+1):
            i2 = i*i
            m.add(i2)
            if c - i2 in m:
                return True
        return False
    
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        l, r = 0, int(c**0.5)
        while l <= r:
            n = l*l + r*r
            if n == c: return True
            elif n < c: l += 1
            else: r -= 1
           # print(l, r)
        return False    

            


if __name__ == '__main__': 
    print(Solution().judgeSquareSum(5))
    print(Solution().judgeSquareSum(4))
    print(Solution().judgeSquareSum(3))
    print(Solution().judgeSquareSum(2))
    print(Solution().judgeSquareSum(1))
    print(Solution().judgeSquareSum(100000000))
    print(Solution().judgeSquareSum(200000000))

