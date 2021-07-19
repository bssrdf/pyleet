'''
-Medium-
*Backtracking*
You are given a string of digits num, such as "123456579". We can split it into a 
Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list f of non-negative integers such that:

0 <= f[i] < 2^31, (that is, each integer fits in a 32-bit signed integer type),
f.length >= 3, and
f[i] + f[i + 1] == f[i + 2] for all 0 <= i < f.length - 2.
Note that when splitting the string into pieces, each piece must not have extra 
leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from num, or return [] if it cannot be done.

 

Example 1:

Input: num = "123456579"
Output: [123,456,579]
Example 2:

Input: num = "11235813"
Output: [1,1,2,3,5,8,13]
Example 3:

Input: num = "112358130"
Output: []
Explanation: The task is impossible.
Example 4:

Input: num = "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
Example 5:

Input: num = "1101111"
Output: [11,0,11,11]
Explanation: The output [11, 0, 11, 11] would also be accepted.
 

Constraints:

1 <= num.length <= 200
num contains only digits.

'''

class Solution(object):
    def splitIntoFibonacci(self, num):
        """
        :type num: str
        :rtype: List[int]
        """
        INT_MAX= 2**31
        self.res, out = None, []
        def helper(num, start, out):
            #if self.res: return
            if start >= len(num) and len(out) >= 3:
                self.res = out[:]
                return
            for i in range(start, len(num)):
                cur = num[start:i+1]
                if (len(cur) > 1 and cur[0] == '0') or len(cur) > 10: break
                t = int(cur)
                length = len(out)
                if t > INT_MAX: break
                if length >= 2 and t != out[length - 1] + out[length - 2]: continue
                out.append(t)
                helper(num, i + 1, out)
                out.pop()
        helper(num, 0, out)
        return self.res

if __name__ == "__main__":  
    print(Solution().splitIntoFibonacci("123456579"))   